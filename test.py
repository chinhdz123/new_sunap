from rembg import remove
import cv2
print("a")
input_path = 'data\s1.bmp'

input = cv2.imread(input_path)
output = remove(input)
cv2.imshow("out",output)
cv2.waitKey(0)