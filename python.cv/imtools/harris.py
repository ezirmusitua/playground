import numpy as np
import pylab
from scipy import ndimage

def compute_response(img, sigma=3):
  im = np.array(img.convert('L'))
  imx = np.zeros(im.shape)
  ndimage.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
  imy = np.zeros(im.shape)
  ndimage.gaussian_filter(im, (sigma, sigma), (1, 0), imy)
  wxx = ndimage.gaussian_filter(imx * imx, sigma)
  wxy = ndimage.gaussian_filter(imx * imy, sigma)
  wyy = ndimage.gaussian_filter(imy * imy, sigma)
  wdet = wxx * wyy - wxy ** 2
  wtr = wxx + wyy
  return np.nan_to_num(wdet / wtr)

def get_points(harrisim, min_dist=10, threshold=0.1):
  corner_threshold = harrisim.max() * threshold
  harrisim_t = (harrisim > corner_threshold) * 1
  coords = np.array(harrisim_t.nonzero()).T
  candiates = [harrisim[c[0], c[1]] for c in coords]
  indexes = np.argsort(candiates)
  allowed_locations = np.zeros(harrisim.shape)
  allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1
  filtered_coords = []
  for i in indexes:
    if allowed_locations[coords[i, 0], coords[i, 1]] == 1:
      filtered_coords.append(coords[i])
      allowed_locations[(coords[i, 0] - min_dist):(coords[i, 0] + min_dist),
      (coords[i, 1] - min_dist):(coords[i, 0] + min_dist)] = 0
  return filtered_coords

def plot_points(image, filtered_coords):
  pylab.figure()
  pylab.gray()
  pylab.imshow(np.array(image.convert('L')))
  pylab.plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords],
             'r*')
  pylab.axis('off')
  pylab.show()

def get_descriptor(image, filtered_coords, wid=5):
  im = np.array(image.convert('L'))
  desc = []
  for coords in filtered_coords:
    patch = im[coords[0] - wid:coords[0] + wid + 1,
            coords[1] - wid:coords[1] + wid + 1].flatten()
    desc.append(patch)
  return desc

def match_descriptor(desc1, desc2, threshold=0.5):
  n = len(desc1[0])
  d = -np.ones((len(desc1), len(desc2)))
  counter = 1
  for i in range(len(desc1)):
    for j in range(len(desc2)):
      print(counter)
      d1 = (desc1[i] - np.mean(desc1[i])) / np.std(desc1[i])
      d2 = (desc2[j] - np.mean(desc2[j])) / np.std(desc2[j])
      ncc_value = np.sum(d1 * d2) / (n - 1)
      if ncc_value > threshold:
        d[i, j] = ncc_value
      counter += 1
  ndx = np.argsort(-d)
  return ndx[:, 0]

def match_descriptor_twosided(desc1, desc2, threshold=0.5):
  matches_12 = match_descriptor(desc1, desc2, threshold)
  matches_21 = match_descriptor(desc2, desc1, threshold)
  ndx_12 = np.where(matches_12 >= 0)[0]
  for n in ndx_12:
    if matches_21[matches_12[n]] != n:
      matches_12[n] = -1
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
  for i, m in enumerate(matchscores):
    if m > 0:
      pylab.plot([locs1[i][1], locs2[m][1] + cols1], [locs1[i][0], locs2[m][0]],
                 'c')
  pylab.axis('off')
