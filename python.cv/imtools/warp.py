import pylab
import numpy as np
from scipy import ndimage
from imtools import homography
from matplotlib import tri

def image_in_image(im1, im2, tp):
  m, n = im1.shape[:2]
  fp = np.array([[0, m, m, 0], [0, 0, n, n], [1, 1, 1, 1]])
  H = homography.Haffine_from_points(tp, fp)
  im1_t = ndimage.affine_transform(im1, H[:2, :2], (H[0, 2], H[0, 2]),
                                   im2.shape[:2])
  alpha = (im1_t > 0)
  return (1 - alpha) * im2 + alpha * im1_t

def alpha_for_triangle(points, m, n):
  alpha = np.zeros((m, n))
  for i in range(min(points[0]), max(points[0])):
    for j in range(min(points[1]), max(points[1])):
      x = np.linalg.solve(points, [i, j, 1])
      if min(x) > 0:
        alpha[i, j] = 1
  return alpha

def triangulate_points(x, y):
  return tri.Triangulation(x, y).triangles

def pw_affine(fromim, toim, fp, tp, tri):
  im = toim.copy()
  is_color = len(fromim.shape) == 3
  im_t = np.zeros(im.shape, 'uint8')
  for t in tri:
    H = homography.Haffine_from_points(tp[:, t], fp[:, t])
    if is_color:
      for col in range(fromim.shape[2]):
        im_t[:, :, col] = ndimage.affine_transform(fromim[:, :, col], H[:2, :2],
                                                   (H[0, 2], H[1, 2]),
                                                   im.shape[:2])
    else:
      im_t = ndimage.affine_transform(fromim, H[:2, :2], (H[0, 2], H[1, 2]),
                                      im.shape[:2])
    alpha = alpha_for_triangle(tp[:, t], im.shape[0], im.shape[1])
    im[alpha > 0] = im_t[alpha > 0]
  return im

def plot_mesh(x, y, tri):
  for t in tri:
    t_ext = [t[0], t[1], t[2], t[0]]
    pylab.plot(x[t_ext], y[t_ext], 'r')

def panorama(H, fromim, toim, padding=2400, delta=2400):
  is_color = len(fromim.shape) == 3

  def transf(p):
    p2 = np.dot(H, [p[0], p[1], 1])
    return (p2[0] / p2[2], p2[1] / p2[2])

  if H[1, 2] < 0:
    print('warp - right')
    if is_color:
      toim_t = np.hstack((toim, np.zeros((toim.shape[0], padding, 3))))
      fromim_t = np.zeros(
        (toim.shape[0], toim.shape[1] + padding, toim.shape[2]))
      for col in range(3):
        fromim_t[:, :, col] = ndimage.geometric_transform(fromim[:, :, col],
                                                          transf, (
                                                            toim.shape[0],
                                                            toim.shape[
                                                              1] + padding))
    else:
      toim_t = np.hstack((toim, np.zeros((toim.shape[0], padding, 3))))
      fromim_t = ndimage.geometric_transform(fromim, transf, (
        toim.shape[0], toim.shape[1] + padding))
  else:
    print('warp - left')
    H_delta = np.array([[1, 0, 0], [0, 1, -delta], [0, 0, 1]])
    H = np.dot(H, H_delta)
    if is_color:
      toim_t = np.hstack((np.zeros((toim.shape[0], padding, 3)), toim))
      fromim_t = np.zeros(
        (toim.shape[0], toim.shape[1] + padding, toim.shape[2]))
      for col in range(3):
        fromim_t[:, :, col] = ndimage.geometric_transform(fromim[:, :, col],
                                                          transf, (
                                                            toim.shape[0],
                                                            toim.shape[
                                                              1] + padding))
    else:
      toim_t = np.hstack((toim, np.zeros((toim.shape[0], padding, 3))))
      fromim_t = ndimage.geometric_transform(fromim, transf, (
        toim.shape[0], toim.shape[1] + padding))
  if is_color:
    alpha = ((fromim_t[:, :, 0] * fromim_t[:, :, 1] * fromim_t[:, :, 2]) > 0)
    for col in range(3):
      toim_t[:, :, col] = fromim_t[:, :, col] * alpha + toim_t[:, :, col] * (
        1 - alpha)
  else:
    alpha = (fromim_t > 0)
    toim_t = fromim_t * alpha + toim_t * (1 - alpha)
  return toim_t
