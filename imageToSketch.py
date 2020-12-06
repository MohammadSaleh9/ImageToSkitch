import cv2

img_location = 'C:/Users/GTS/Desktop/'
filename = '3.jpg'

img = cv2.imread(img_location+filename)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

bluured_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)


inverted_bluured = 255 - bluured_image

pencil_sketch_IMG = cv2.divide(gray_image, inverted_bluured, scale=256.0)
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_IMG)
cv2.waitKey(0)