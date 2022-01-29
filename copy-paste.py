import cv2
import random

img = cv2.imread('assets/wallpaper.jpg', 1)
# copy pasting part of the image
# tag = img[300:500, 600:800]
# img[100:300, 700:900] = tag
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


cv2.imshow('cp', img)
cv2.waitKey(0)
cv2.destroyAllWindows()