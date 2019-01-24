import numpy as np

def normalize(points):
  for row in points:
    row /= points[-1]
  return points

def make_homog(points):
  return np.vstack((points, np.ones(1, points.shape[1])))

def H_frompoints(fp, tp):
  if fp.shape != tp.shape:
    raise RuntimeError('number of points not matched')
  m = np.mean(fp[:2], axis=1)
  maxstd = np.max(np.std(fp[:2], axis=1)) + 1e-9
  C1 = np.diag([1 / maxstd, 1 / maxstd, 1])
  C1[0][2] = -m[0] / maxstd
  C1[1][2] = -m[1] / maxstd
  fp = np.dot(C1, fp)
  m = np.mean(tp[:2], axis=1)
  maxstd = np.max(np.std(fp[:2], axis=1)) + 1e-9
  C2 = np.diag([1 / maxstd, 1 / maxstd, 1])
  C2[0][2] = -m[0] / maxstd
  C2[1][2] = -m[1] / maxstd
  tp = np.dot(C2, tp)

  nbr_correspondences = fp.shape[1]
  A = np.zeros((2, nbr_correspondences))
  for i in range(nbr_correspondences):
    A[2 * i] = [-fp[0][i], -fp[1][i], -1, 0, 0, 0, tp[0][i] * fp[0][i],
                tp[0][i] * fp[1][i], tp[0][i]]
    A[2 * i + 1] = [0, 0, 0, -fp[0][i], -fp[1][i], -1, tp[1][i] * fp[0][i],
                    tp[1][i] * fp[1][i], tp[1][i]]

  U, S, V = np.linalg.svd(A)
  H = V[8].reshape((3, 3))
  H = np.dot(np.linalg.inv(C2), np.dot(H, C1))
  return H / H[2, 2]

def Haffine_from_points(fp, tp):
  if fp.shape != tp.shape:
    raise RuntimeError('Number of points not matched')
  m = np.mean(fp[:2], axis=1)
  maxstd = np.max(np.std(fp[:2], axis=1)) + 1e-9
  C1 = np.diag([1 / maxstd, 1 / maxstd, 1])
  C1[0][2] = -m[0] / maxstd
  C1[1][2] = -m[1] / maxstd
  fp_cond = np.dot(C1, fp)
  m = np.mean(tp[:2], axis=1)
  maxstd = np.max(np.std(tp[:2], axis=1)) + 1e-9
  C2 = np.diag([1 / maxstd, 1 / maxstd, 1])
  C2[0][2] = -m[0] / maxstd
  C2[1][2] = -m[1] / maxstd
  tp_cond = np.dot(C2, fp)

  A = np.concatenate((fp_cond[:2], tp_cond[:2]), axis=0)
  U, S, V = np.linalg.svd(A.T)
  tmp = V[:2].T
  B = tmp[:2]
  C = tmp[2:4]
  tmp2 = np.concatenate((np.dot(C, np.linalg.pinv(B)), np.zeros((2, 1))),
                        axis=1)
  H = np.vstack((tmp2, [0, 0, 1]))
  H = np.dot(np.linalg.inv(C2), np.dot(H, C1))
  return H / H[2, 2]
