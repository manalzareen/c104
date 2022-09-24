import cv2 

img = cv2.imread("butterfly.jpg")

cv2.imshow("Display Image" , img  )

grayImg = cv2.cvtColor( img , cv2.COLOR_RGB2GRAY )

cv2.imshow("gray butterfly" , grayImg)

cv2.waitKey(5000)