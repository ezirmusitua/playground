import pylab
from PIL import Image
from imtools import sift

imname = r'./examples/Rak/1.png'
output = r'./examples/Rak/1.png.sift'
img = Image.open(imname)
sift.process_image(imname, output)
l1, d1 = sift.read_feature_from_file(output)
sift.plot_features(img, l1, circle=True)

imname1 = r'./examples/Rak/1.png'
output1 = r'./examples/Rak/1.png.sift'
img1 = Image.open(imname1)
sift.process_image(imname1, output1)
l2, d2 = sift.read_feature_from_file(output1)
sift.plot_features(img1, l2, circle=True)

print('Start Matching ... ')
matches = sift.match_descriptor_twosided(d1, d2)
print('End Matching')
print('Start Plotting')
pylab.figure()
pylab.gray()
sift.plot_matches(img, img1, l1, l2, matches)
pylab.show()
print('All Set')
