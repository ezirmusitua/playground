import pylab
import numpy as np
from PIL import Image
from scipy import ndimage

def gaussian_filter_color(img, delta):
  im = np.array(img)
  im_1 = np.zeros(im.shape)
  for i in range(3):
    im_1[:, :, i] = ndimage.gaussian_filter(im[:, :, i], delta)
  return np.uint8(im_1)

def gaussian_filter_grey(img, delta):
  im_1 = np.array(img.convert('L'))
  return ndimage.gaussian_filter(im_1, delta)

def test_gaussian_filter():
  img = Image.open(r'./examples/Rak/1.png')
  deltas = [2, 5, 10, 25]
  pylab.figure()
  for idx, delta in enumerate(deltas):
    pylab.subplot(2, 4, idx + 1)
    pylab.imshow(gaussian_filter_color(img, delta))
  for idx, delta in enumerate(deltas):
    pylab.subplot(2, 4, idx + 5)
    pylab.imshow(gaussian_filter_grey(img, delta))
  pylab.show()

# test_gaussian_filter()

def sobel_derivative_filter_grey(img):
  im = np.array(img.convert('L'))
  imdx = ndimage.sobel(im, 1)  # TODO: what is axis mean?
  imdy = ndimage.sobel(im, 0)
  magnitude = np.sqrt(imdx ** 2 + imdy ** 2)
  print(imdx.shape, imdy.shape, magnitude.shape)
  return imdx, imdy, np.uint8(magnitude)

def test_sobel_derivative_filter_grey():
  img = Image.open(r'./examples/Rak/1.png')
  pylab.figure()
  pylab.subplot(1, 4, 1)
  pylab.imshow(np.array(img))
  imdx, imdy, magnitude = sobel_derivative_filter_grey(img)
  pylab.subplot(1, 4, 2)
  pylab.imshow(imdx)
  pylab.subplot(1, 4, 3)
  pylab.imshow(imdy)
  pylab.subplot(1, 4, 4)
  pylab.imshow(magnitude)
  pylab.show()

# test_sobel_derivative_filter_grey()

def do_morphology(img, structure, iterations, binary=None):
  im = 1 * (np.array(img.convert('L')) < 128)
  if binary == 'open':
    im = ndimage.binary_opening(im, structure, iterations)
  if binary == 'close':
    im = ndimage.binary_closing(im, structure, iterations)
  labels, nbr_objects = ndimage.label(im)
  return labels, nbr_objects

def test_morphology():
  img = Image.open(r'./examples/Rak/1.png')
  binaries = [None, 'open', 'close']
  structures = [np.ones((4, 4)), np.ones((20, 20)), np.ones((100, 100))]
  iterations = [2, 5, 10]
  pylab.figure()
  counter = 1
  for binary in binaries:
    for iteration in iterations:
      for structure in structures:
        labels, nbr_objects = do_morphology(img, structure, iteration, binary)
        pylab.subplot(3, 9, counter)
        pylab.imshow(labels)
        counter += 1
  pylab.show()

test_morphology()
