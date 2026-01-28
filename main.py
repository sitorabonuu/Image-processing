import cv2
color_image =cv2.imread('snow.jpg')
print (color_image.shape)
grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

#cv2.imshow('grayscale image',grayscale_image)
_, binary_image = cv2.threshold(grayscale_image, 100,150, cv2.THRESH_BINARY)
#cv2.imshow('grayscale image',grayscale_image)
cv2.imshow('binary image',binary_image)
cv2.waitKey(0)

