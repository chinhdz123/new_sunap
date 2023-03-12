# from utils import find_total_circles
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
    if i<20:
        label_x.append(float(line))
    else:
        label_y.append(float(line))
    i+=1

print(label_x)
print(label_y)
new_label_x = [abs(label) for label in label_x]
new_label_y = [abs(label) for label in label_y]
label_x_max = max(new_label_x)
print(label_x_max)
label_y_max = max(new_label_y)
print(label_y_max)
label_x= [i/label_x_max for i in label_x]
label_y= [i/label_y_max for i in label_y]



# img = cv2.imre,ad(r"tmp/new.jpg",)
# circles, image = find_total_circles(img)
# x = [circle[0] for circle in circles]
# y = [circle[1] for circle in circles]

y = [340, 460, 577, 742, 901, 343, 461, 581, 745, 903, 344, 463, 582, 746, 904, 344, 463, 584, 745, 906]
x = [158, 157, 153, 151, 152, 276, 275, 271, 269, 270, 395, 392, 
390, 391, 388, 554, 552, 550, 548, 545]
print(len(x))
x_max = max(x)
y_max = max(y)
x = [i/x_max for i in x]
y = [i/y_max for i in y]

plt.scatter(y,label_y)
# plt.scatter(x,label_x)
plt.show()
x_train, x_test, label_x_train, label_x_test = train_test_split(x, label_x, test_size=0.25,random_state=42)
y_train, y_test, label_y_train, label_y_test = train_test_split(y, label_y, test_size=0.25,random_state=42)


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
