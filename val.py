from ultralytics import YOLO
import csv
import os
 
model_path = r'runs\detect\\train\weights\\last.pt'
# input_folder_path = 'datasets\mq\images\\val'
model = YOLO(model=model_path)

if __name__ == '__main__':

    # Train the model
    # results = model.train(data="mq.yaml", epochs=100, imgsz=640, workers = 0, device = "cuda")
    results = model.val(data="mq.yaml", workers = 0, device = "cuda")