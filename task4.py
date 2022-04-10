''' lgm vip internship
Data science internship
task 4:image to pencil sketch using python
'''
#import cv2
import cv2
# give the image location from your pc
img_location = 'C:/Users/Prasanna Reddy/Desktop/'
# give the image name
file_name = 'puppy.jpg'
#read the image
image = cv2.imread(img_location+file_name)
# converting the image into gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#converting the gray image to inverted gray image
inverted_gray_image = 255 - gray_image
#now blurr image using gaussian blur
blurr = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)
inverted_blurred_img = 255 - blurr
#now converting into pencil sketch dividing the gray_image by inverted blurred image
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
#finally displaying the original image and pencil sketch image
cv2.imshow('Original Image', image)
cv2.imshow('pencil sketch', pencil_sketch_IMG )
cv2.waitKey(0)
