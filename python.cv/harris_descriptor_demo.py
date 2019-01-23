import pylab
from PIL import Image
import imtools
from imtools import harris
WID = 5
img = Image.open(r'./examples/Rak/1.png')
harrisim = harris.compute_response(img)
filtered_coords = harris.get_points(harrisim, WID + 1)
# imtools.plot_harris_points(img, filtered_coords)
img1 = Image.open(r'./examples/Rak/1.png')
harrisim1 = harris.compute_response(img1)
filtered_coords1 = harris.get_points(harrisim1, WID + 1)

d1 = harris.get_descriptor(img, filtered_coords, WID)
d2 = harris.get_descriptor(img1, filtered_coords1, WID)

print('Start Matching ... ')
matches = harris.match_descriptor_twosided(d1, d2)
print('End Matching')
print('Start Plotting')
pylab.figure()
pylab.gray()
harris.plot_matches(img, img1, filtered_coords, filtered_coords1, matches)
pylab.show()
print('All Set')
