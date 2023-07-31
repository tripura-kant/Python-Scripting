import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize the video capture using the default camera (0).
video_capture = cv2.VideoCapture(0)

# Load images and their corresponding encodings.
known_faces = {}

# Load "Harry.jpg" image and its encoding.
Harry_images = face_recognition.load_image_file("faces/Harry.jpg")
harry_encodings = face_recognition.face_encodings(Harry_images)
if len(harry_encodings) > 0:
    known_faces["Harry"] = harry_encodings[0]

# Load "rohan.jpg" image and its encoding.
rohan_images = face_recognition.load_image_file("faces/rohan.jpg")
rohan_encodings = face_recognition.face_encodings(rohan_images)
if len(rohan_encodings) > 0:
    known_faces["Rohan"] = rohan_encodings[0]

# Prepare data for attendance recording.
current_date = datetime.now().strftime("%Y-%m-%d")
attendance_csv_file = f"attendance/{current_date}.csv"
attendance_data = []

while True:
    # Capture video frame by frame.
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the current frame.
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Initialize an empty list to store recognized names in the current frame.
    recognized_names = []

    for face_encoding in face_encodings:
        # Compare each face encoding with known faces.
        if len(known_faces) > 0:
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
            face_distances = face_recognition.face_distance(list(known_faces.values()), face_encoding)

            # Find the index of the best match.
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                # If there is a match, get the corresponding name.
                recognized_name = list(known_faces.keys())[best_match_index]
                recognized_names.append(recognized_name)

    # Display recognized names on the frame.
    for name in recognized_names:
        cv2.putText(frame, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Attendance", frame)

    # Record attendance data in the CSV file.
    attendance_data.append([current_date, recognized_names])

    # Break the loop if 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Write attendance data to the CSV file.
with open(attendance_csv_file, "w+", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(attendance_data)

# Release the video capture and close all windows.
video_capture.release()
cv2.destroyAllWindows()
