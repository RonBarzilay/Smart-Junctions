import cv2

camera = cv2.VideoCapture(0)

while camera.isOpened():
    check, frame = camera.read()
    cv2.imshow("Current Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera.release()
        cv2.destroyAllWindows()

