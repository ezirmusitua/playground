from PIL import Image
import numpy as np
import pylab
import imtools

image = Image.open(r'examples/Rak/1.png')
image.thumbnail((500, 500))
im = np.array(image)
print('RGB image, uint8 type: ', im.shape, im.dtype)

im1 = np.array(image.convert('L'), 'f')
print('Grey image, float type: ', im1.shape, im1.dtype)

print('row: 1->3, col: 1->20: ', im1[1:2, 1:20])

im2 = 255 - im1
im3 = (100.0 / 255) * im1 + 100
im4 = 255.0 * (im1 / 255.0) ** 2

pil_img = Image.fromarray(np.uint8(im1))
# pil_img.show()
pil_img = Image.fromarray(np.uint8(im2))
# pil_img.show()
pil_img = Image.fromarray(np.uint8(im3))
# pil_img.show()
pil_img = Image.fromarray(np.uint8(im4))
# pil_img.show()

im5_array, cdf = imtools.histeq(im4)
im5 = Image.fromarray(im5_array)
# im5.show()
# pylab.plot(cdf)
# pylab.show()

image_filenames = [r'examples/Rak/2B_1_(' + str(i) + ').jpg' for i in
                   range(1, 10)]

im6_array = imtools.compute_average(image_filenames)
# im6 = Image.fromarray(im6_array)
# im6.show()

im_tmp = np.array(Image.open(image_filenames[0]))
m, n = im_tmp.shape[:2]
imnbr = len(image_filenames)
immatrix = np.array(
  [np.array(Image.open(filename).convert('L')).flatten() for filename in
   image_filenames],
  'f')
V, S, immean = imtools.pca(immatrix)
pylab.figure()
pylab.gray()
pylab.subplot(2, 6, 1)
pylab.imshow(immean.reshape(m, n))
for i in range(9):
  pylab.subplot(2, 6, i + 2)
  pylab.imshow(V[i].reshape(m, n))

pylab.show()
