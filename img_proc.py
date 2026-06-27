import cv2

img = cv2.imread("lebron.png", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('cv2 output', cv2.WINDOW_NORMAL)

cv2.imshow('cv2 output', img)

cv2.waitKey(0)