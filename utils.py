import math
import torch
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from loguru import logger
import cv2
import warnings
import numpy as np
from copy import deepcopy
import json
warnings.filterwarnings("ignore")
cfg = get_cfg()
cfg.merge_from_file(r"output\config.yaml")
logger.info("start_load_md")
predictor_circles = DefaultPredictor(cfg)
logger.info("end_load_md")
with open('data_json\data.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

#pre=processing for x data
label_x_max = json_object["label_x_max"]
label_y_max = json_object["label_y_max"]
y_max = json_object["y_max"]
x_max = json_object["x_max"]

def convert_boxes(boxes):
    return boxes.tensor.numpy()

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

def find_circles_in_small_img(img,w_s, w_en):
    logger.info("start predict")
    output = predictor_circles(img)
    logger.info("end predict")
    boxes = output["instances"].to("cpu").pred_boxes if output["instances"].to("cpu").has("pred_boxes") else None
    if boxes is not None:
        boxes = convert_boxes(boxes)
    circles= []
    for box in boxes:
        x0, y0, x1, y1 = box
        center_X =  int((x1+x0)/2)
        center_Y = int((y1+y0)/2)
        r = int((x1-x0)/2)
        if center_X-r > w_s and center_X+r < w_en: 
            circles.append([center_X,center_Y,r])
    return circles

def convert_to_x_y_robot(x,y):
    model_x = torch.load(r"model\model_x.pth")
    model_y = torch.load(r"model\model_y.pth")
    X = []
    xmax = x_max
    x = [i/xmax for i in x]
    for item in x:
        X.append([item,item**2,item**3,item**4])
    X = torch.tensor(X,dtype=torch.float32)
    
    predicteds_X = model_x(X).detach().numpy()
    predicteds_X = [math.floor(predicted_X.item()*label_x_max) for predicted_X in predicteds_X]
    ymax = y_max
    y = [i/ymax for i in y]
    Y = []
    for item in y:
        Y.append([item,item**2,item**3,item**4])
    Y = torch.tensor(Y,dtype=torch.float32)

    predicteds_Y = model_y(Y).detach().numpy()
    predicteds_Y = [math.floor(predicted_Y.item()*label_y_max) for predicted_Y in predicteds_Y]

    return predicteds_X,predicteds_Y

def find_total_circles(img):
    h,w= img.shape[:2]
    # img1 = np.ones_like(img)
    # img2 = np.ones_like(img)

    # img1[:,:int(5.2*w/10)] = img[:,:int(5.2*w/10)]
    # img2[:,int(4.8*w/10):] = img[:,int(4.8*w/10):]
    # circles1 = find_circles_in_small_img(img1, 0, int(5.2*w/10))
    # circles2 = find_circles_in_small_img(img2,int(4.8*w/10),w )
    # circles = circles1 + circles2
    # new_circles = deepcopy(circles)
    # for circle1 in  circles1:
    #     for circle2 in circles2:
    #         if ((circle2[0]-circle1[0])**2+(circle2[1]-circle1[1])**2)**(1/2) < 0.8*max(circle2[2],circle1[2]):
    #             if circle2[2] < circle1[2]:
    #                 new_circles.remove(circle2)
    #             else:
    #                 new_circles.remove(circle1)
    circles = find_circles_in_small_img(img,0,w)
    # circles = sorted(new_circles, key=lambda b: b[1])
    circles = sorted(circles, key=lambda b: b[1])
    group_lines = find_line_circles(circles)
    new_circle = []
    count = 0
    for group_line in group_lines:
        group_line = sorted(group_line, key=lambda b: b[0])
        for circle in group_line:
            # if count == 39 or count == 40:
            cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 255, 0), 1)
            cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 1)
            cv2.putText(img, str(count), (circle[0], circle[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            count +=1
            new_circle.append(circle)
    cv2.imwrite("tmp/result1.jpg",img)

    return new_circle,img


