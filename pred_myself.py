import pandas as pd

def calculate_iou(box1, box2):
    # 计算IOU
    x1_max = box1['x_min'] + box1['width']
    y1_max = box1['y_min'] + box1['height']
    x2_max = box2['x_min'] + box2['width']
    y2_max = box2['y_min'] + box2['height']

    inter_x_min = max(box1['x_min'], box2['x_min'])
    inter_y_min = max(box1['y_min'], box2['y_min'])
    inter_x_max = min(x1_max, x2_max)
    inter_y_max = min(y1_max, y2_max)

    inter_area = max(0, inter_x_max - inter_x_min) * max(0, inter_y_max - inter_y_min)
    box1_area = box1['width'] * box1['height']
    box2_area = box2['width'] * box2['height']

    return inter_area / (box1_area + box2_area - inter_area)

def compute_precision(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # 过滤异常数据
    df1 = df1[df1['image_id'] != 99999]
    df2 = df2[df2['image_id'] != 99999]

    TP, FP, FN = 0, 0, 0

    for _, row1 in df1.iterrows():
        matched = False
        ioumax = 0
        for _, row2 in df2.iterrows():
            if row1['image_id'] == row2['image_id'] and row1['class_id'] == row2['class_id']:
                iou = calculate_iou(row1, row2)
                if iou>ioumax:
                    ioumax = iou
                if iou >= 0.5:
                    TP += 1
                    matched = True
                    break
        
        if not matched:
            FN += 1
            print(f"fn:{row1['ID']},ioumax:{ioumax}")

    FP = len(df2) - TP  # 假设每个框在df2中都可能是FP
    print(f"fp:{FP},tp:{TP},fn:{FN}")

    precision = TP / (TP + FP + FN) if (TP + FP + FN) > 0 else 0
    return precision

# 使用函数
precision_value = compute_precision('test.csv', 'output.csv')
print(f'Precision: {precision_value}')
  