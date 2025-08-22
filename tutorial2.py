import cv2
import random

img = cv2.imread('assets/mosquito.jpg', -1)

# print(type(img))
# print(img.shape)

# Image Pixel Representation
# [
# [[0, 0, 0],[128, 56, 9]]
# [[0, 6, 1],[18, 6, 9]]
# ]

# print(img[300][45:400])
# print(img[300][300])


for i in range(100):
    for j in range(300):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


tag = img[50:200, 200:300]
img[100:250, 400:500] = tag

cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()