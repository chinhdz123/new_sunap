import cv2
import numpy as np
img = cv2.imread(r'tmp\new.jpg',0)
ret,thresh1 = cv2.threshold(img,140,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5, 5))
mask = cv2.dilate(thresh1, kernel, iterations=2)  # lấp đầy trắng(mất nhiễu đen)
mask = cv2.erode(thresh1, kernel, iterations=1)  # lấp đầy trắng(mất nhiễu đen)

contours, hierarchy = cv2.findContours(mask, 1,2)

i = 0
xs = []
ys = []
ncnt = []
def find_line_circles(ncnt):
    a = ncnt[0][1]
    group_lines = []
    group_line = []
    for i in range(len(ncnt)):
        print(ncnt[i][1],a)
        if ncnt[i][1]+40 > a and ncnt[i][1]-40 < a:
            group_line.append(ncnt[i])
        else:
            group_lines.append(group_line)
            group_line = []
            group_line.append(ncnt[i])
            a = ncnt[i][1]
    group_lines.append(group_line)
    return group_lines


for cnt in contours:
    area = cv2.contourArea(cnt)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    ncnt.append([x,y])
    # cv2.drawContours(img, [approx], -1, (255, 0, 0), 3)
    # cv2.putText(img, str(i), (x,y + 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(255,0,0) , 1)
ncnt = sorted(ncnt, key=lambda b: b[1])
group_lines = find_line_circles(ncnt)
new_cnt = []
count = 0
for group_line in group_lines:
    group_line = sorted(group_line, key=lambda b: b[0])
    for circle in group_line:
        print("circle",circle)
        # if count == 39 or count == 40:
        cv2.putText(img, str(count), (circle[0], circle[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
        cv2.circle(img, (circle[0], circle[1]), 3, (0, 0, 0), 1)
        count +=1
        new_cnt.append(circle)
cv2.imwrite('tmp/result.jpg',img)
x = [cnt[0] for cnt in new_cnt][2:]
y = [cnt[1] for cnt in new_cnt][2:]
print(len(x))
print(x,y)

