import numpy as np
from matplotlib import pylab
from imtools.camera import Camera, rotate_matrix
from imtools import homography
from imtools import sift

points = np.loadtxt(r'examples/house.p3d').T
points = np.vstack((points, np.ones(points.shape[1])))
P = np.hstack((np.eye(3), np.array([[0], [0], [-10]])))
cam = Camera(P)
x = cam.project(points)

pylab.figure()
pylab.plot(x[0], x[1], 'k.')
pylab.show()

K = np.array([[1000, 0, 500], [0, 1000, 300], [0, 0, 1]])
tmp = rotate_matrix([0, 0, 1])[:3, :3]
Rt = np.hstack((tmp, np.array([[50], [40], [30]])))
cam = Camera(np.dot(K, Rt))
print(K, Rt)
print(cam.factor())

sift.process_image(r'examples/Rak/1.png', r'examples/Rak/1.png.sift')
l0, d0 = sift.read_feature_from_file(r'examples/Rak/1.png.sift')
sift.process_image(r'examples/Rak/1_1.png', r'examples/Rak/1_1.png.sift')
l1, d1 = sift.read_feature_from_file(r'examples/Rak/1_1.png.sift')
print(d0, d1)

matches = sift.match_descriptor_twosided(d0, d1)
ndx = matches.nonzero()[0]
fp = homography.make_homog(l0[ndx, :2].T)
ndx2 = matches.nonzero()[0]
tp = homography.make_homog(l1[ndx2, :2].T)

model = homography.RansacModel()
H = homography.H_from_ransac(fp, tp, model)
