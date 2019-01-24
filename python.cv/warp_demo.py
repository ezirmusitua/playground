import pylab
import numpy as np
from PIL import Image
from scipy import ndimage
from imtools import warp, homography

im1 = np.array(Image.open(r'./examples/Rak/1.png').convert('L'))
im2 = np.array(Image.open(r'./examples/Rak/1_1.png').convert('L'))
tp = np.array([[200, 300, 400, 200], [40, 36, 400, 400], [1, 1, 1, 1]])

# im3 = warp.image_in_image(im1, im2, tp)

m, n = im1.shape[:2]
fp = np.array([[0, m, m, 0], [0, 0, n, n], [1, 1, 1, 1]])
tp2 = tp[:, :3]
fp2 = fp[:, :3]
H = homography.Haffine_from_points(tp2, fp2)
im1_t = ndimage.affine_transform(im1, H[:2, :2], (H[0, 2], H[1, 2]), im2.shape[:2])
alpha = warp.alpha_for_triangle(tp2, im2.shape[0], im2.shape[1])
im3 = (1 - alpha) * im2 + alpha * im1_t

tp2 = tp[:, [0, 2, 3]]
fp2 = fp[:, [0, 2, 3]]
H = homography.Haffine_from_points(tp2, fp2)
im1_t = ndimage.affine_transform(im1, H[:2, :2], (H[0, 2], H[1, 2]), im2.shape[:2])
alpha = warp.alpha_for_triangle(tp2, im2.shape[0], im2.shape[1])
im4 = (1 - alpha) * im3 + alpha * im1_t

pylab.figure()
pylab.gray()
pylab.imshow(im4)
pylab.show()
