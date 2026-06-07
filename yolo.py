from ultralytics import YOLO # it can detect and track
import cv2
model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture(r"C:\Users\Gunavathi\Downloads\dhoni .mp4")
while True:
    ret,frame=cap.read()
    if not ret:
        break
    results=model.track(
        frame,
        persist=True,
        classes=[0]
    )
    annotated_frame=results[0].plot()
    cv2.imshow("person annotated:",annotated_frame)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cap.release
cv2.destroyAllWindows()
