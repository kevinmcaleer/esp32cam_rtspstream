# ESP32Cam Streaming to Python

This Python code will take the video stream from an ESP32Cam and process it for faces on another, connected computer.

Libraries needed on the host computer:
`pip install mediapipe cvzone opencv-python`

---

## Face Detection

```python
import cv2
import cvzone
from cvzone import FaceDetectionModule
face_detector = FaceDetectionModule.FaceDetector()


# Replace with your RTSP stream URL
rtsp_url = 'http://192.168.4.1:81/stream'

# Capture the video stream
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Process the frame with OpenCV here
    frame, list_faces = face_detector.findFaces(frame)
    cv2.imshow("Face Detection", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

```

## Hand Detection

``` python 
import cv2
import cvzone
from cvzone import  HandTrackingModule
hand_tracker = HandTrackingModule.HandDetector(detectionCon=0.8, maxHands=2)

# Replace with your RTSP stream URL
rtsp_url = 'http://192.168.4.1:81/stream'

# Capture the video stream
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Process the frame with OpenCV here

    frame, list_hands = hand_tracker.findHands(frame)

    cv2.imshow("Hands", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if job is finished

cap.release()
cv2.destroyAllWindows()
```