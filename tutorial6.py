import numpy as np
import cv2

img = cv2.imread('assets/maze.png', -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)

# for i in range(len(corners)):
#     for j in range(i + 1, len(corners)):
#         color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
#         cv2.line(img, corners[i][0], corners[j][0], color, 1)



cv2.imshow('image', img)



cv2.waitKey(0)
cv2.destroyAllWindows()

