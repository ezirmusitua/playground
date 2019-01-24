import numpy as np
from scipy import ndimage
from imtools import homography

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
