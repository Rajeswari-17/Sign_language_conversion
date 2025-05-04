import os
import cv2
import numpy as np

# Define constants
DATA_DIR = 'data'
number_of_classes = 3
dataset_size = 100

# Create directories if not exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Create subdirectories for each class
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

print("Starting data collection...")

# Initialize the USB webcam
cap = cv2.VideoCapture(0)  # 0 for the default webcam
if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

count = 0
for j in range(number_of_classes):
    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        count += 1
        if count % 3 != 0:
            continue
        frame = cv2.flip(frame, -1)
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('FRAME', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        frame = cv2.flip(frame, -1)
        cv2.imshow('FRAME', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
        counter += 1

# Release the capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()