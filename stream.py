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
