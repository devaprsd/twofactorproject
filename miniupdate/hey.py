

import cv2
import  face_recognition
import os
global user_encoding,user_image,failornot,facer
facer=True
def facerecon(imagepath):
    failornot = False
    user_image_list=[]
    known_face_encoding=[]
    capture = cv2.VideoCapture(0)
    user_image =face_recognition.load_image_file(imagepath)
    user_encoding = face_recognition.face_encodings(user_image)[0]
    print(user_encoding)
    s=True
    while True:
            #print("starting live feed")
        ret,frame = capture.read()
        cv2.imshow('webcam',frame)
        small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
                #rgb_small_frame = small_frame[:,:,::-1]
                #face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(small_frame)    
        if facer==False:
            break
        elif len(face_encodings)>0: 
            matches = face_recognition.compare_faces(user_encoding,face_encodings)
            if matches[0]:
                failornot=True
            else:
                failornot=False
        else:     
            print("No face Detected")
    print("ok done")
facerecon("/home/blackcrypt/miniupdate/imagebase/known_face.jpg")
    