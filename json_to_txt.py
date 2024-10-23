import json
import os
import math

def j2t(path,output_folder_path, filename):
    with open(path, 'r') as file:
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
        txt_filename = filename.replace('.json', '.txt')
        txt_path = os.path.join(output_folder_path, txt_filename)

        # 将字段写入文本文件
        with open(txt_path, 'a') as file:
            file.write(f"{clas} {point[0]/568.0} {point[1]/528.0} {width/568.0} {height/528.0}\n")

        print(f"success{filename}")



# 指定输入文件夹路径和输出文件夹路径
input_folder_path = 'weed-detection\\train\labels'
output_folder_path = 'train'

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder_path, exist_ok=True)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder_path):
    if filename.endswith('.json'):
        json_path = os.path.join(input_folder_path, filename)
        
        j2t(json_path,output_folder_path, filename)


print("success all")