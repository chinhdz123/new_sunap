import matplotlib.pyplot as plt

# Điểm x và y
xs = [641, 788, 934, 1079, 1226, 640, 787, 937, 1087, 1234, 640, 790, 942, 1092, 1243, 645, 794, 946, 1098, 1249, 652, 802, 953, 1102, 1254]
x_max = max(xs)
x_new = [x/x_max for x in xs]
ys = [406, 402, 398, 395, 394, 619, 614, 611, 609, 607, 841, 832, 832, 831, 828, 1066, 1065, 1060, 1058, 1053, 1292, 1289, 1290, 1283, 1276]
y_max = max(ys)
y_new = [y/y_max for y in ys]

# Điểm x_robot và y_robot
x_robot = [303.9339, 276.0692, 247.6784, 218.2372, 189.0659, 304.0992, 275.5145, 247.4909, 218.4363, 189.3126, 303.5478, 275.2704, 247.0504, 218.9933, 189.2964, 303.8901, 275.94, 247.3395, 217.9077, 188.656, 303.5697, 275.414, 247.0972, 216.9659, 187.8995]
x_robot_max = max(x_robot)
x_robot_new = [x/x_robot_max for x in x_robot]

y_robot = [-83.0774, -83.8753, -85.9887, -86.1963, -85.0336, -41.7672, -42.1716, -40.8985, -42.8509, -42.2219, 1.4531, 1.452, 1.3112, -0.3683, 0.1847, 44.5546, 45.3275, 46.7514, 44.813, 45.0665, 88.9391, 88.7988, 87.9753, 88.4969, 88.8251]
y_robot_max = abs(max(y_robot))
y_robot_new = [y/y_robot_max for y in y_robot]

# Biểu diễn các điểm
plt.scatter(x_new, y_new, color='blue')
plt.scatter(x_robot_new, y_robot_new, color='red')

# Tên các trục và định dạng đồ thị
plt.title('Biểu đồ tọa độ robot và tọa độ ảnh sau khi chuyển về (0,1)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Hiển thị đồ thị
plt.show()