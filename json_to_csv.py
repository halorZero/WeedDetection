import json
import os
import math
import csv
out = []
i=0


# 指定输入文件夹路径和输出文件夹路径
input_folder_path = 'weed-detection\\test\labels'

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder_path):
    if filename.endswith('.json'):
        json_path = os.path.join(input_folder_path, filename)

        with open(json_path, 'r') as file:
            data = json.load(file)

        # 访问字段
        shapes = data['shapes']
        for shape in shapes:
            label = shape['label']
            clas = 1
            if label == 'mq':
                clas = 0
            points = shape['points']
            point = points[0]
            width = height = 2*math.sqrt((point[0] - points[1][0]) ** 2 + (point[1] - points[1][1]) ** 2)
            
            # 指定输出TXT文件名
            filename = filename.replace('.json', '')
            i = i+1
            data = {
            "ID": i,
            "image_id": filename,
            "class_id": 1-clas,
            "x_min": point[0]-width/2,
            "y_min": point[1]-height/2,
            "width": width,
            "height": height
            }
            out.append(data)



with open('val.csv', mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=out[0].keys())
    writer.writeheader()
    writer.writerows(out)

print("success all")