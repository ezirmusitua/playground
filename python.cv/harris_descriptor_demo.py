import pylab
from PIL import Image
import imtools
WID = 5
img = Image.open(r'./examples/Rak/1.png')
harrisim = imtools.compute_harris_response(img)
filtered_coords = imtools.get_harris_points(harrisim, WID + 1)
# imtools.plot_harris_points(img, filtered_coords)
img1 = Image.open(r'./examples/Rak/1.png')
harrisim1 = imtools.compute_harris_response(img1)
filtered_coords1 = imtools.get_harris_points(harrisim1, WID + 1)

d1 = imtools.get_harris_descriptor(img, filtered_coords, WID)
d2 = imtools.get_harris_descriptor(img1, filtered_coords1, WID)

print('Start Matching ... ')
matches = imtools.match_harris_descriptor_twosided(d1, d2)
print('End Matching')
print('Start Plotting')
pylab.figure()
pylab.gray()
imtools.plot_harris_matches(img, img1, filtered_coords, filtered_coords1, matches)
pylab.show()
print('All Set')
