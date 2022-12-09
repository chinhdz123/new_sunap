import torch
import math
import cv2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from loguru import logger
logger.info("start_md")
cfg = get_cfg()
cfg.merge_from_file(r'output/config.yaml')
predicts = DefaultPredictor(cfg)
logger.info("stop_md")
class Predict():
    def __init__(self) -> None:
        self.outputs = predicts(img)
        self.boxes = self.outputs["instances"].to("cpu").pred_boxes if self.outputs["instances"].to("cpu").has("pred_boxes") else None
        self.classes = self.outputs["instances"].pred_classes if self.outputs["instances"].has("pred_classes") else None
    def np_boxes (boxes):
        return boxes.tensor.numpy()
    def detect(self,img,w_s,w_e):
        logger.info("start_p")
        self.outputs = predicts(img)
        logger.info("stop_p")
        print(self.outputs)
        if boxes is not None:
            boxes = Predict.np_boxes(boxes)
        circle_1 = []
        circle_2 = []
        rec_3 = []
        for box,classs in zip (boxes,self.classes):
            if classs == 1:
                x0,y0,x1,y1 = box
                center_x = int((x1+x0)/2)
                center_y = int((y1+y0)/2)
                r = int((x1-x0)/2)
                if center_x-r >0 and center_x+r <w_e:
                    circle_1.append([center_x,center_y,r])
            if classs == 2:
                x0,y0,x1,y1 = box
                center_x = int((x1+x0)/2)
                center_y = int((y1+y0)/2)
                r = int((x1-x0)/2)
                if center_x-r >0 and center_x+r <w_e:
                    circle_2.append([center_x,center_y,r])
            if classs == 3:
                x0,y0,x1,y1 = box
                width = int(x1-x0)
                height = int(y1-y0)
                center_x = int((x1+x0)/2)
                center_y = int((y1+y0)/2)
                #if center_x-r >0 and center_x+r <w_e:
                rec_3.append([width,height,center_x,center_y])
        print(len(rec_3))
        print(circle_1[0][1])
        return circle_1,circle_2,rec_3

    def find_line_circles(circles):
        a = circles[0][1]
        group_lines = []
        group_line = []
        for i in range(len(circles)):
            if circles[i][1]+4/5*circles[i][2] > a and circles[i][1]-4/5*circles[i][2] < a:
                group_line.append(circles[i])
            else:
                group_lines.append(group_line)
                group_line = []
                group_line.append(circles[i])
                a = circles[i][1]
        group_lines.append(group_line)
        return group_lines

    def find_circle(self,img):
        h,w = img.shape[:2]
        total_circles=Predict.detect(img,0,w) 
        print(total_circles)
        n_total_circles = []
        classes = ["c1","c2","c3"]
        for circles,classs,number in zip(total_circles,classes,self.classes):
            if len(circles) != 0:
                circles = sorted(circles, key=lambda b: b[1])
                group_lines = Predict.find_line_circles(circles)
                new_circle = []
                count = 0
                for group_line in group_lines:
                    group_line = sorted(group_line, key=lambda b: b[0])
                    for circle in  group_line:
                        # if count == 39 or count == 40:
                        if self.classes == 1 and self.classes == 2:
                            cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 1)
                            cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 1)
                            cv2.putText(img, classs+str(count), (circle[0], circle[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                            count +=1
                            new_circle.append(circle)
                        elif self.classes == 3:
                             cv2.rectangle(img,(0,0,255),2)
                             cv2.putText(img, classs+str(count), (circle[0], circle[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                             count +=1
                             new_circle.append(circle)
                n_total_circles.append(new_circle)
            else:
                n_total_circles.append(circles)
        return n_total_circles,img

img = cv2.imread(r'tmp\new.jpg')
w,h = img.shape[:2]
detect(img,0,w)
