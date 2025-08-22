import cv2

img = cv2.imread('assets/mosquito.jpg', -1)
# img = cv2.resize(img, (400,400))
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


# cv2.imwrite('new_img.jpg', img)



# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency will be NEGLECTED. it is the default flag.
# 0, cv2.IMREAD_GRAYSTYLE : Loads image in gray-scale mode. 
# 1 cv2.IMREAD_UNCHANGED : Loads image as such alpha channel.

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()