import cv2

# Replace with your RTSP stream URL
rtsp_url = 'rtsp://your_esp32_cam_stream'

# Capture the video stream
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Process the frame with OpenCV here
    # ...

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
