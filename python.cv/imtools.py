import numpy as np
from PIL import Image

def imresize(im, sz):
  pil_im = Image.fromarray(np.uint8(im))
  return np.array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
  imhist, bins = np.histogram(im.flatten(), nbr_bins, density=True)
  cdf = imhist.cumsum()
  cdf = 255 * cdf / cdf[-1]
  im2 = np.interp(im.flatten(), bins[:-1], cdf)
  return im2.reshape(im.shape), cdf

def compute_average(image_filenames):
  avg_img = np.array(Image.open(image_filenames[0]), 'f')
  for filename in image_filenames[1:]:
    try:
      avg_img += np.array(Image.open(filename))
      avg_img /= 2
    except Exception:
      print('Can no open image: ', filename)
  return np.array(avg_img, 'uint8')

def pca(X):
  num_data, dim = X.shape
  print('matrix shape: ', num_data, dim)
  mean_X = X.mean(axis=0)
  X = X - mean_X
  print('mean X: ', X)
  if dim > num_data:
    M = np.dot(X, X.T)
    print('covariance matrix: ', M)
    e, EV = np.linalg.eigh(M)
    print('feature: ', e, EV)
    tmp = np.dot(X.T, EV).T
    V = tmp[::-1]
    S = np.sqrt(e)[::-1]
    print(V[:, 0].shape, S.shape)
    for i in range(V.shape[1]):
      V[:, i] /= S
  else:
    U, S, V = np.linalg.svd(X)
    V = V[:num_data]

  return V, S, mean_X
