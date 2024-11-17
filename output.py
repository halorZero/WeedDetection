from ultralytics import YOLO
import csv
import os
 
model_path = r'runs\detect\\train25\weights\\last.pt'
input_folder_path = 'datasets\mq_test\images\\val'
model = YOLO(model=model_path)


i=0
out = []
for filename in os.listdir(input_folder_path):
    if filename.endswith('.png'):
        img_path = os.path.join(input_folder_path, filename)
    else:
        continue
    filename =(int)(filename.replace('.png', ''))
        
    results = model.predict(source=img_path)
    
    # 把tensor转为numpy格式
    boxes = results[0].boxes.cpu().numpy()
    
    
    # # 遍历每个检测结果
    for box in boxes:
        loc=box.xyxy[0].tolist()
        scores=float(box.conf)
        if scores<0.3:
            continue
        classes=int(box.cls)#results[0].names[int(box.cls)]
        i = i+1
        data = {
        "ID": i,
        "image_id": filename,
        "class_id": 1-classes,
        "x_min": loc[0],
        "y_min": loc[1],
        "width": loc[2]-loc[0],
        "height": loc[3]-loc[1]
        }
        out.append(data)
while i<4999:
    i=i+1
    data = {
        "ID": i,
        "image_id": 99999,
        "class_id": 9,
        "x_min": 0,
        "y_min": 0,
        "width": 0,
        "height": 0
        }
    out.append(data)

with open('output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=out[0].keys())
    writer.writeheader()
    writer.writerows(out)
