from ultralytics import YOLO
import cv2

pose_model = YOLO("yolov8n-pose.pt")

def detect_pose(frame):
    results = pose_model(frame)
    return results[0].keypoints.xy  # keypoints of detected people
