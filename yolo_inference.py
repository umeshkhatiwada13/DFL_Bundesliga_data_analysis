from ultralytics import YOLO

model = YOLO('yolov8x')

results = model.predict('input_video/08fd33_5.mp4', save=True)

print(results[0])
print("-------------------------------")
for box in results[0].boxes:
    print(box)
