from imtools import sift

featname = [r'./examples/Rak/2B_1_(' + str(1) + r').sift' for i in range(1, 6)]
imname = [r'./examples/Rak/2B_1_(' + str(1) + r').jpg' for i in range(1, 6)]

l = {}
d = {}

for i in range(5):
  sift.process_image(imname[i], featname[i])
  l[i], d[i] = sift.read_feature_from_file(featname[i])

matches = {}
for i in range(4):
  matches[i] = sift.match_descriptor(d[i + 1], d[i])


