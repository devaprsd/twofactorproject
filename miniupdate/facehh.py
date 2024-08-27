import face_recognition
import cv2

# Load known images (faces) and encode them
known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load unknown image (face) and encode it
unknown_image = face_recognition.load_image_file("unknown_face.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the encodings
results = face_recognition.compare_faces([known_encoding], unknown_encoding)

# Check if the unknown face matches the known face
if results[0]:
    print("The unknown face matches the known face!")
else:
    print("The unknown face does not match the known face!")

# Display the images with rectangles around detected faces
known_face_locations = face_recognition.face_locations(known_image)
unknown_face_locations = face_recognition.face_locations(unknown_image)

for top, right, bottom, left in known_face_locations:
    cv2.rectangle(known_image, (left, top), (right, bottom), (0, 255, 0), 2)

for top, right, bottom, left in unknown_face_locations:
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)

# Display the images
cv2.imshow("Known Face", known_image)
cv2.imshow("Unknown Face", unknown_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
