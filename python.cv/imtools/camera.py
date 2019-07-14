import numpy as np
from scipy import linalg

class Camera(object):

  def __init__(self, P):
    self.P = P
    self.K = None
    self.R = None
    self.t = None
    self.c = None

  def project(self, X):
    x = np.dot(self.P, X)
    for i in range(3):
      x[i] /= x[2]
    return x

  def factor(self):
    K, R = linalg.rq(self.P[:, :3])
    T = np.diag(np.sign(np.diag(K)))
    if linalg.det(T) < 0:
      T[1, 1] *= -1
    self.K = np.dot(K, T)
    self.R = np.dot(T, R)
    self.t = np.dot(linalg.inv(self.K), self.P[:, 3])
    return self.K, self.R, self.t

  def center(self):
    if self.c is not None:
      return self.c
    else:
      self.factor()
      self.c = -np.dot(self.R.T, self.t)
      return self.c

def calibration(sz):
  row, col = sz
  fx = 2555 * col / 2592
  fy = 2586 * row / 1936
  K = np.diag([fx, fy, 1])
  K[0, 2] = 0.5 * col
  K[1, 2] = 0.5 * row
  return K

def cube_points(c, wid):
  p = []
  # bottom
  p.append([c[0] - wid], c[1] - wid, c[2] - wid)
  p.append([c[0] - wid], c[1] + wid, c[2] - wid)
  p.append([c[0] - wid], c[1] + wid, c[2] - wid)
  p.append([c[0] + wid], c[1] + wid, c[2] - wid)
  p.append([c[0] + wid], c[1] - wid, c[2] - wid)
  p.append([c[0] - wid], c[1] - wid, c[2] - wid)
  # top
  p.append([c[0] - wid], c[1] - wid, c[2] + wid)
  p.append([c[0] - wid], c[1] + wid, c[2] + wid)
  p.append([c[0] + wid], c[1] + wid, c[2] + wid)
  p.append([c[0] + wid], c[1] - wid, c[2] + wid)
  p.append([c[0] - wid], c[1] - wid, c[2] + wid)

  p.append([c[0] - wid], c[1] - wid, c[2] + wid)
  p.append([c[0] - wid], c[1] + wid, c[2] + wid)
  p.append([c[0] - wid], c[1] + wid, c[2] - wid)
  p.append([c[0] + wid], c[1] + wid, c[2] - wid)
  p.append([c[0] + wid], c[1] + wid, c[2] + wid)
  p.append([c[0] + wid], c[1] - wid, c[2] + wid)
  p.append([c[0] + wid], c[1] - wid, c[2] - wid)
  return np.array(p).T

def rotate_matrix(a):
  R = np.eye(4)
  R[:3, :3] = linalg.expm(
    [[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
  return R
