import cv2
import numpy as np

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

cv2.namedWindow("integrate")
cv2.namedWindow("live")

img_counter = 0
inited = False
average = None
live = True

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break


    k = cv2.waitKey(1)
   # print(k)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 114:
        inited = False
        img_counter = 0
        live = False
        cv2.waitKey(2000)

    if live == False:
        if(inited == False):
            average = np.zeros(frame.shape,np.uint64)
            inited = True
        
        average += frame# cv2.cvtColor(frame,cv2.CV_8U)
        img_counter +=1
        out = average.copy()
        out //= int(img_counter)
        out = out.astype('uint8') # * 255
      #  out =  cv2.cvtColor(out,cv2.COLOR_RGB2BGR)
    # cv2.normalize(out,  out, 0, 255, cv2.NORM_MINMAX)
    #if(live):
    cv2.imshow("live", frame)
    #else:
    if(inited):
        cv2.imshow("integrate",out )

    if(img_counter>100):
        live = True
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, out)
        print("{} written!".format(img_name))
        img_counter =0


cam.release()

cv2.destroyAllWindows()