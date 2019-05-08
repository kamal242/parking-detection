#Author : Ambani
#Date: 8/05/19
#copyright
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('IMG_20180326_003246.jpg', 0)
edge = cv.Canny(img, 100, 200)
img_gauss = cv.GaussianBlur(edge,(5,5), 0)

plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edge, cmap='gray')
plt.title('Edge image'), plt.xticks([]), plt.yticks([])

plt.imshow(img_gauss, cmap='gray')
plt.title('Gauss image'), plt.xticks([]), plt.yticks([])



plt.show()
