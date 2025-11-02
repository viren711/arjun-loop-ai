from ultralytics import YOLO
model = YOLO('backend/best.pt') 

path = "ISIC_0053515.jpg"
results = model(path)


result = results[0]
result.save('result/ISIC_0085644.jpg')

print(result)