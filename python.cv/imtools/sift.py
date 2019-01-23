import os
import pylab
import numpy as np
from PIL import Image

def process_image(imagename, resultname,
                  params='--edge-thresh 10 --peak-thresh 5'):
  to_process = imagename
  if to_process[-3:] != 'pgm':
    im = Image.open(to_process).convert('L')
    im.save('tmp.pgm')
    to_process = 'tmp.pgm'
  cmd = str('sift ' + to_process + ' --output=' + resultname + ' ' + params)
  os.system(cmd)
  if to_process == 'tmp.pgm':
    os.remove(to_process)
  print(imagename + ' processed, result is ', resultname)

def read_feature_from_file(filename):
  f = np.loadtxt(filename)
  return f[:, :4], f[:4:]

def write_feature_to_file(filename, locs, desc):
  np.savetxt(filename, np.hstack(locs, desc))

def plot_features(img, locs, circle=False):
  def draw_circle(c, r):
    t = np.arange(0, 1.01, 0.01) * 2 * np.pi
    x = r * np.cos(t) + c[0]
    y = r * np.sin(t) + c[1]
    pylab.plot(x, y, 'b', linewidth=2)

  pylab.imshow(np.array(img.convert('L')))
  if circle:
    for p in locs:
      draw_circle(p[:2], p[2])
  else:
    pylab.plot(locs[:0], locs[:1], 'ob')
  pylab.axis('off')

def match_descriptor(desc1, desc2):
  desc1 = np.array([d / np.linalg.norm(d) for d in desc1])
  print(desc1[0][0], desc2[0][0])
  desc2 = np.array([d / np.linalg.norm(d) for d in desc2])
  dist_ratio = 0.99
  desc1_size = desc1.shape
  matchscores = np.zeros(desc1_size[0], 'int')
  print('init match scores: ', matchscores)
  desc2t = desc2.T
  for i in range(desc1_size[0]):
    dotprods = np.dot(desc1[i, :], desc2t)
    dotprods = 0.9999 * dotprods
    indx = np.argsort(np.arccos(dotprods))
    print('indx: ', indx)
    if np.arccos(dotprods)[indx[0]] < dist_ratio * np.arccos(dotprods)[indx[1]]:
      print('selected indx: ', indx[0])
      matchscores[i] = int(indx[0])
  return matchscores

def match_descriptor_twosided(desc1, desc2):
  matches_12 = match_descriptor(desc1, desc2)
  matches_21 = match_descriptor(desc2, desc1)
  ndx_12 = matches_12.nonzero()[0]
  for n in ndx_12:
    if matches_21[int(matches_12[n])] != n:
      matches_12 = 0
  return matches_12

def append_images(img1, img2):
  im1 = np.array(img1.convert('L'))
  im2 = np.array(img2.convert('L'))
  rows1 = im1.shape[0]
  rows2 = im2.shape[0]

  if rows1 < rows2:
    im1 = np.concatenate((im1, np.zeros((rows2 - rows1, im1.shape[1]))), axis=0)
  elif rows1 > rows2:
    im2 = np.concatenate((im2, np.zeros((rows1 - rows2, im2.shape[1]))), axis=0)

  return np.concatenate((im1, im2), axis=1)

def plot_matches(img1, img2, locs1, locs2, matchscores, show_below=True):
  im1 = np.array(img1.convert('L'))
  im3 = append_images(img1, img2)
  if show_below:
    im3 = np.vstack((im3, im3))
  pylab.imshow(im3)
  cols1 = im1.shape[1]
  print(matchscores)
  for i, m in enumerate(matchscores):
    print('i: ', i, ' match score: ', m)
    if m > 0:
      pylab.plot([locs1[i][1], locs2[m][1] + cols1], [locs1[i][0], locs2[m][0]],
                 'c')
  pylab.axis('off')
