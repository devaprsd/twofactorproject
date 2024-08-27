import cv2
import  face_recognition
#import numpy as np  

def facerecon(path):
    imagepath=str(path)
    global user_encoding,user_image,failornot, facer
    failornot = False
    facer=True
    capture =  cv2.VideoCapture(0)
    user_image =face_recognition.load_image_file(imagepath)
    user_encoding = face_recognition.face_encodings(user_image)[0]
    s=True
    while True:
            ret,frame = capture.read()
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
                    print("True")
                else:
                    failornot=False
            else:
                print("No face Detected")
                failornot=False
    print("ok done")
