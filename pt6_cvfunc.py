import numpy as np
import cv2

img = cv2.imread('lena.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
#img=cv2.merge(())

#to copy a part of a photo and paste it somewhere else
#ball=img(280:340,330:390)
#img(273:333,100:160)=ball
img= cv2.imread('starry_night.jpg')
img2=cv2.imread('opencv-logo-white.png')
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
#dst = cv2.add(img,img2)
dst=cv2.addWeighted(img,.9,img2,.3,0)
cv2.imshow('image3',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()