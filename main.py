import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QDate, QTimer
from PyQt5.QtGui import QImage,QPixmap
from app import Ui_MainWindow
from PyQt5 import QtGui
# import imutils
import cv2
import os
from utils import *
from control_rb import Control_robot
import datetime
import time
from mypackage.speak_hear import *
from pypylon import pylon
import cv2
class MainWindow:
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.bt_start.clicked.connect(self.start)
        self.uic.bt_stop.clicked.connect(self.stop)
        self.uic.bt_camera.clicked.connect(self.capture)
        self.uic.bt_grid.clicked.connect(self.grid)
        self.uic.bt_mic.clicked.connect(self.mic)
        self.thread = {}
        self.uic.label_4.setText("Circles")
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.Update)
        self.timer.start()
        self.control = Control_robot()
        self.start_robot = False
        self.new_img_dt = None
        # self.uic.bt_grid.setEnabled(False)
    def show(self):
        self.main_win.show()
    def start(self):
        self.start_robot = self.control.start()
        if self.start_robot:
            self.uic.bt_start.setEnabled(False)

        print(self.start_robot)
    def mic(self):
        if self.start_robot:
            if self.uic.bt_grid.isEnabled():
                while True:
                    you = hear()
                    if you is None:
                        speak("Tôi không nghe rõ, bạn có thể nói lại được không")
                    elif "tạm biệt" in you:
                        speak("tạm biệt")
                        break
                    elif "lên" in you:
                        speak("ô kê, rô bốt sẽ bắt đầu trong ít giây")
                        self.control.up()
                    elif "xuống" in you:
                        speak("ô kê, rô bốt sẽ bắt đầu trong ít giây")
                        self.control.down()
                    elif "phải" in you:
                        speak("ô kê, rô bốt sẽ bắt đầu trong ít giây")
                        self.control.right()
                    elif "trái" in you:
                        speak("ô kê, rô bốt sẽ bắt đầu trong ít giây")
                        self.control.left()
    def grid(self):
        if self.start_robot:
            self.uic.bt_grid.setEnabled(False)
        if self.new_img_dt is not None:
            total_circles, image = find_total_circles(self.new_img_dt)
            new_img_show = image[280:1400,550:1400]
            image = cv2.resize(new_img_show,(931,561))
            image = QImage(image,image.shape[1],image.shape[0],image.strides[0],QImage.Format_RGB888)
            self.uic.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
            len1 = 0
            coordinates_rb = []
            for circles in total_circles:
                if len(circles)!=0:
                    print(circles)
                    len1+= len(circles)
                    x = [circle[0] for circle in circles]
                    y = [circle[1] for circle in circles]
                    x_robot,y_robot = convert_to_x_y_robot(x,y)
                    coordinates_rb.append([x_robot,y_robot])
                else:
                    coordinates_rb.append([])

            self.uic.label_5.setText(str(len1))
            print(x_robot,y_robot)

            # bước 3: điều khiển robot theo các vị trí
            # self.control.start(x_robot,y_robot)
            # self.control.start()
            self.control.grip(coordinates_rb)
            time.sleep(10)
            self.uic.bt_grid.setEnabled(True)
            print('a')
            


    def stop(self):
        self.start_robot = self.uic.bt_start.setEnabled(True)
        if self.start_robot:
            self.control.stop()
            self.start_robot = False

    def Update(self):
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.now().strftime("%I:%M %p")
        self.uic.label_date1.setText(current_date)
        self.uic.label_time_1.setText(current_time)

    def capture(self):
        self.control.home()
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

        # Grabing Continusely (video) with minimal delay
        camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        converter = pylon.ImageFormatConverter()

        # converting to opencv bgr format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        while camera.IsGrabbing():
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
                # Access the image data
                image = converter.Convert(grabResult)
                img = image.GetArray()
                new_img = img[280:1400,550:1400]# cần chỉnh
                new_img_dt = np.ones_like(img)
                new_img_dt[280:1400,550:1400] = img[280:1400,550:1400]
                cv2.imwrite("tmp/new.jpg",new_img_dt)
                self.new_img_dt = new_img_dt
                break
            grabResult.Release()
        camera.StopGrabbing()
        image = cv2.resize(new_img,(931,561))
        image = QImage(image,image.shape[1],image.shape[0],image.strides[0],QImage.Format_RGB888)
        self.uic.label_2.setPixmap(QtGui.QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())