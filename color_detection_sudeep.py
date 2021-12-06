# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:49:50 2021

@author: sudeep_kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:10:35 2021

@author: sudeep_kumar
"""

import pandas as pd
import cv2

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv('C:\cloudxlab\color_detection\Color detection\Color detection/colors.csv',names=index,header=None)
#print(df)

img = cv2.imread('C:\cloudxlab\color_detection\Color detection\Color detection/pic3.jpg')
img = cv2.resize(img,(800,600))
#print(img)
#print(len(df))
#print(df.loc[1,'G'])

clicked= False
r = g = b = xpos = ypos = 0

def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i,'color_name']
    return cname

#print(get_color_name(255,0,0))
            
                                                                  
def draw_function(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r,g,b,xpos,ypos
        clicked = True
        xpos = x
        ypos = y
        #print(x,y)
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        #print(b,g,r)
        
        
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)
            
while True:
	cv2.imshow('image', img)
	if clicked:
		#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
		cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)

		#Creating text string to display( Color name and RGB values )
		text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)

		#For very light colours we will display text in black colour
		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()
#cv2.imshow('image',img)
#cv2.waitKey(0)
cv2.destroyAllWindows()




