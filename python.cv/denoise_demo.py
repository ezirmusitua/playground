import pylab
import numpy as np
from PIL import Image
from scipy import ndimage

import imtools

im = np.zeros((500, 500))
im[100:400, 100:400] = 128
im[200:300, 200:300] = 255
im = im + 30 * np.random.standard_normal((500, 500))

U, T = imtools.denoise_roe(Image.fromarray(im))
G = ndimage.gaussian_filter(im, 10)
pylab.figure()
pylab.gray()
pylab.subplot(1, 3, 1)
pylab.imshow(T)
pylab.subplot(1, 3, 2)
pylab.imshow(G)
pylab.subplot(1, 3, 3)
pylab.imshow(U)
pylab.show()
