import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 for default webcam, you can change it if you have multiple cameras

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    cv2.imshow('Webcam', frame)  # Display the frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
