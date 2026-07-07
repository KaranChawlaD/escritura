import cv2
from skimage.morphology import skeletonize
import numpy as np

path = "stock_drawing2.png"

img = cv2.imread(f"./test_images/{path}", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("could not load image at path")

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

bool_img = binary > 0

skeleton = skeletonize(bool_img)

cv2.namedWindow('cv2 output', cv2.WINDOW_KEEPRATIO)

cv2.imshow('cv2 output', (skeleton * 255).astype(np.uint8))

cv2.imwrite(f"./output_images/{path}", (skeleton * 255).astype(np.uint8))

cv2.waitKey(0)