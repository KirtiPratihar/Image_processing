import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT'in i ]
print(events)

def click_event(event,x, y, flags,param):
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x,', ',y)
    #     font =cv2.FONT_HERSHEY_COMPLEX
    #     strXY =str(x)+','+str(y)
    #     cv2.putText(img,strXY,(x,y),font,1,(233,212,54),2)
    #     cv2.imshow('image',img)
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img,(x,y),3,(233,212,54),-1)
    #     points.append((x,y))
    #     if len(points)>=2:
    #         cv2.line(img,points[-1],points[-2],(255,0,0),4)
    #         cv2.imshow('image',img)
           
 #  if event == cv2.EVENT_RBUTTONDOWN: 
 #       blue = img [y,x,0]
  #      green = img[y,x,1]
   #     red= img [y,x,2]
    #    font= cv2.FONT_HERSHEY_COMPLEX
    #    strBGR= str(blue)+','+str(green)+','+str(red)   
   #     cv2.putText(img,strBGR,(x,y),font,0.5,(100,122,254),1)
     if event == cv2.EVENT_RBUTTONDOWN:
        blue = img [y,x,0]
        green = img[y,x,1]
        red= img [y,x,2]
        cv2.circle(img,(x,y),3,(233,212,54),-1)
        mycolimg =np.zeros((512,512,3), np.uint8)
        mycolimg[:]= [blue,green,red]
        cv2.imshow('image1',mycolimg)
        
#img =np.zeros((512,512,3), np.uint8)
img =cv2.imread('lena.jpg')   
#points=[]
cv2.imshow('image',img )

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
