import numpy as np
import scipy.ndimage
from skimage import io, img_as_float32

image = img_as_float32(io.imread('q3img1.png'))
kernel = np.array([[25, 0, -25], [25, 0, -25], [25, 0, -25], [25, 0, -25], [25, 0, -25], [25, 0, -25], [25, 0, -25], [25, 0, -25], [25, 0, -25]])
image1 = scipy.ndimage.convolve(image, kernel)
io.imshow(image1)
io.show()
