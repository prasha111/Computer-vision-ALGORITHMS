import cv2              #this is computer vision library
#inport cv
from google.colab.patches import cv2_imshow      #this is specifaclly designed for the google collab 

cap = cv2.VideoCapture('file_example_AVI_480_750kB.avi');  #this is the avi file that is used as test case for video subtraction
while(1):
    # read frames
    #ret, img = cap.read();
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))           #some techniques for morphing of the image
    fgbg = cv2.createBackgroundSubtractorMOG2();                          # background subtraction technique that using guassian based background forground segmentation algorithm
    ret, frame = cap.read()
    if ret == True:

       fgmask = fgbg.apply(frame)                                       # apply these on the each frames of the video
       fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

       cv2_imshow(fgmask)                                                #function to show it in the collab


       if cv2.waitKey(30) & 0xFF == ord('q'):                            #key to come out of the loop 
            break

    else:
        break

    if cv2.waitKey(0) & 0xff == 27:
      cv2.destroyAllWindows()