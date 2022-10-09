#Imports
import cv2
import pickle

#Variables
width,height=107,48
count=1
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
    
# posList=[]

#MousCLickFunction
def mouseClick(events, x, y,flag,params):
    global count
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
        count+=1
        
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                count-=1
    
    # with open('CarParkPos', 'wb') as f:
    #     pickle.dump(posList,f)
    
#Output
while True:
    img = cv2.imread('carParkImg.png')
    for i,pos in enumerate(posList):
       rect= cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
       num=str(count-len(posList)+i+69)
       cv2.putText(rect,num,(pos[0] + (width-10)//2, pos[1] + (height+20)//2), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    #    count+=1
       

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    
    key=cv2.waitKey(1)
    
    if key==ord('q'):
        break