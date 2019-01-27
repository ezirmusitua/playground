import pylab
import numpy as np
from PIL import Image
from matplotlib import tri

from imtools import warp
from imtools import homography
#
# x, y = np.array(np.random.standard_normal((2, 100)))
# tria = tri.Triangulation(x, y)
#
# pylab.figure()
# for t in tria.triangles:
#   t_ext = [t[0], t[1], t[2], t[0]]
#   pylab.plot(x[t_ext], y[t_ext], 'r')
#
# pylab.plot(x, y, '*')
# pylab.axis('off')
# pylab.show()

fromim = np.array(Image.open(r'./examples/Rak/1.png'))
x, y = np.meshgrid(range(5), range(6))
x = (fromim.shape[1] / 4) * x.flatten()
y = (fromim.shape[0] / 5) * y.flatten()

tri = warp.triangulate_points(x, y)
im = np.array(Image.open(r'./examples/Rak/1_1.png'))
tp = np.loadtxt(r'./examples/Rak/1_1_points.txt')
fp = np.uint8(np.vstack((y, x, np.ones((1, len(x))))))
tp = np.uint8(np.vstack((tp[:, 1], tp[:, 0], np.ones((1, len(tp))))))
print(tp, fp)
im = warp.pw_affine(fromim, im, fp, tp, tri)
pylab.figure()
pylab.imshow(im)
warp.plot_mesh(tp[1], tp[0], tri)
pylab.axis('off')
pylab.show()
