from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def main():
    model.train(data='/Users/yeshu/Desktop/Python/SpoofDetector/outDataset/data.yaml', epochs=3)

if __name__ == '__main__':
    main()
