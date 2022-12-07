from utils import find_total_circles
import cv2
import json
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
f = open("file.txt",'r')
lines = f.readlines()
i =0 
label_x = []
label_y = []
for line in lines:
    print("line",line)
    if i<25:
        label_x.append(float(line))
    else:
        label_y.append(float(line))
    i+=1


new_label_x = [abs(label) for label in label_x]
new_label_y = [abs(label) for label in label_y]
label_x_max = max(new_label_x)
print(label_x_max)
label_y_max = max(new_label_y)
print(label_y_max)
label_x= [i/label_x_max for i in label_x]
label_y= [i/label_y_max for i in label_y]



img = cv2.imread(r"tmp/new.jpg")
circles, image = find_total_circles(img)
x = [circle[0] for circle in circles]
y = [circle[1] for circle in circles]

x = [641, 788, 934, 1079, 1226, 640, 787, 937, 1087, 1234, 640, 790, 942, 1092, 1243, 645, 794, 946, 1098, 1249, 652, 802, 953, 1102, 1254] 
y = [406, 402, 398, 395, 394, 619, 614, 611, 609, 607, 841, 832, 832, 831, 828, 1066, 1065, 1060, 1058, 1053, 1292, 1289, 1290, 1283, 1276]
print(len(x))
plt.scatter(y,label_y)
plt.show()
x_max = max(x)
y_max = max(y)
x = [i/x_max for i in x]
y = [i/y_max for i in y]

x_train, x_test, label_x_train, label_x_test = train_test_split(x, label_x, test_size=0.25, random_state=42)
y_train, y_test, label_y_train, label_y_test = train_test_split(y, label_y, test_size=0.25, random_state=42)


# Data to be written
data1 = {
    "x_train": x_train,
    "label_x_train": label_x_train,
    "x_test": x_test,
    "label_x_test": label_x_test,
    "y_train": y_train,
    "label_y_train": label_y_train,
    "y_test": y_test,
    "label_y_test": label_y_test,
    'label_x_max':label_x_max,
    'label_y_max':label_y_max,
    'x_max':x_max,
    'y_max':y_max
}
 
with open("data_json\data.json", "w") as outfile:
    json.dump(data1, outfile)
