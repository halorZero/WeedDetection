import pandas as pd

# 读取CSV文件
df = pd.read_csv('val.csv')

# 统计class_id为0和1的数量
count_class_0 = len(df[df['class_id'] == 0])
count_class_1 = len(df[df['class_id'] == 1])

print(f'class_id为0的数量: {count_class_0}')
print(f'class_id为1的数量: {count_class_1}')
# 用于测试数据集中mq和其他类标注量分布，是否存在不均衡的情况
# 结果发现还行，虽然差了点，但是差不了多少