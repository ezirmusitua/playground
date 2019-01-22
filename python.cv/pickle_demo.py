import pickle
import imtools
import numpy as np
import pylab
from PIL import Image

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

DUMP_PATH = r'./examples/rak_2b_pca_modes.pkl'
with open(DUMP_PATH, 'wb') as wf:
  pickle.dump(immean, wf)
  pickle.dump(V, wf)
  pickle.dump(S, wf)

with open(DUMP_PATH, 'rb') as rf:
  immean_1 = pickle.load(rf)
  pylab.imshow(Image.fromarray(immean_1.reshape(m, n)))
  pylab.show()
