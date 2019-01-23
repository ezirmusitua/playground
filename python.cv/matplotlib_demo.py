import numpy as np
from pylab import (
  imshow, plot, title, show, figure, gray, contour, axis,
  hist,
  ginput,
)
from PIL import Image

image = Image.open(r'examples/Rak/1.png')

im = np.array(image)

imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r--*')
plot(x[:2], y[:2], 'g:+')
title('Plotting: "Rak/1.png"')
x = ginput(3)
print(x)
show()

figure()
gray()
grey_im = image.copy().convert('L')
contour(np.array(grey_im), origin='image')
axis('equal')
axis('off')
figure()
hist(np.array(grey_im).flatten(), 128)
show()
