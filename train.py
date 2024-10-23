from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

if __name__ == '__main__':

    # Train the model
    results = model.train(data="mq.yaml", epochs=100, imgsz=640, workers = 0, device = "cuda")
    results = model.val()