import DobotDllType as dType

class Control_robot():
    def __init__(self) -> None:
        self.api = None
    def start(self):
        CON_STR = {
            dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
            dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
            dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
        self.api =  dType.load()
        self.state = dType.ConnectDobot(self.api, "COM3", 115200)[0]
        if (self.state == dType.DobotConnect.DobotConnect_NoError):
            print("connect")
            #Clean Command Queued
            dType.SetQueuedCmdClear(self.api)
            dType.SetPTPCoordinateParams(self.api,500,500,500,500,0)
            dType.SetPTPCommonParams(self.api, 500, 500, isQueued = 0)
            dType.SetHOMEParams(self.api, 250, 0, 50, 0, isQueued = 0)
            dType.SetPTPJointParams(self.api, 500, 500, 500, 500, 500, 500, 500, 500, isQueued = 0)
            dType.SetHOMECmd(self.api, temp = 0, isQueued = 0)
            return True
        else: 
            return False
    def grip(self,x,y):
        for x_item,y_item in zip(x,y):
            if x_item<310:
                print("x_item, y_item",x_item,y_item)
                # for y_item in y:
                
                # dType.SetPTPCoordinateParams(self.api,500,500,500,500,0)
                # dType.SetPTPCommonParams(self.api, 500, 500, isQueued = 0)
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,30,10, isQueued=1)
                dType.SetWAITCmd(self.api, 500, isQueued=1)
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,-20,10, isQueued=1)
                # dType.SetWAITCmd(api, 200, isQueued=1)
                dType.SetEndEffectorSuctionCup(self.api, True,  True, isQueued=1)
                dType.SetWAITCmd(self.api, 500, isQueued=1)
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,75,10, isQueued=1)
                dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, 51,-247,75,10, isQueued=1)
                # dType.SetWAITCmd(self.api, 500, isQueued=1)
                dType.SetEndEffectorSuctionCup(self.api, True,  False, isQueued=1)
                dType.SetWAITCmd(self.api, 500, isQueued=1)
    def home(self):
        dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, 0,-250,50,10, isQueued=1)
    def stop(self):
        dType.DisconnectDobot(self.api)
        print("stop")
    def up(self):
        x_pose,y_pose,z_pose = dType.GetPose(self.api)[:3]
        dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_pose,y_pose,z_pose+20,10, isQueued=1)
    def down(self):
        x_pose,y_pose,z_pose = dType.GetPose(self.api)[:3]
        dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_pose,y_pose,z_pose-20,10, isQueued=1)
    def right(self):
        x_pose,y_pose,z_pose = dType.GetPose(self.api)[:3]
        dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_pose,y_pose+20,z_pose,10, isQueued=1)
    def left(self):
        x_pose,y_pose,z_pose = dType.GetPose(self.api)[:3]
        dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_pose,y_pose-20,z_pose+10,10, isQueued=1)
    # def main(self,x,y):
    #     for x_item,y_item in zip(x,y):
    #         if x_item<315:
    #             print("x_item, y_item",x_item,y_item)
    #             # for y_item in y:
    #             dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
    #             dType.SetWAITCmd(self.api, 200, isQueued=1)
    #             dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,30,10, isQueued=1)
    #             # dType.SetWAITCmd(api, 200, isQueued=1)
    #             dType.SetEndEffectorSuctionCup(self.api, True,  True, isQueued=1)
    #             dType.SetWAITCmd(self.api, 500, isQueued=1)
    #             dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
    #             dType.SetWAITCmd(self.api, 5000, isQueued=1)
    #             dType.SetEndEffectorSuctionCup(self.api, True,  False, isQueued=1)
    # def print(self):
    #     print(self.x_pose)
    #     print(self.z_pose)
    # def luilai(self):
    #     print(self.x_pose,self.y_pose,self.z_pose)
    #     dType.SetPTPCmd(self.api,dType.PTPMode.PTPMOVLXYZMode,self.x_pose-10,self.y_pose-10,self.z_pose,10,isQueued=1) 
    # def tienlen(self):
    #     print(self.x_pose,self.y_pose,self.z_pose)
    #     dType.SetPTPCmd(self.api,dType.PTPMode.PTPMOVLXYZMode,self.x_pose+10,self.y_pose+10,self.z_pose,10,isQueued=1) 
    #     #print("up")
    # def up(self):
    #     print(self.x_pose,self.y_pose,self.z_pose+50)
    #     dType.SetPTPCmd(self.api,dType.PTPMode.PTPMOVLXYZMode,self.x_pose,self.y_pose,self.z_pose+10,10,isQueued=1) 
    #     #print("up")
    # def down(self):
    #     dType.SetPTPCmd(self.api,dType.PTPMode.PTPMOVLXYZMode,self.x_pose,self.y_pose,self.z_pose-10,10,isQueued=1) 
    #     #print("down")




""" 
def control(key,x,y):
    import DobotDllType as dType

    CON_STR = {
        dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
        dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
        dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

    #将dll读取到内存中并获取对应的CDLL实例
    #Load Dll and get the CDLL object
    api = dType.load()
    #建立与dobot的连接
    #Connect Dobot
    state = dType.ConnectDobot(api, "COM6", 115200)[0]
    if (state == dType.DobotConnect.DobotConnect_NoError):
        print("connect")
        #Clean Command Queued
        dType.SetQueuedCmdClear(api)

        #设置运动参数
        #Async Motion Params Setting
        dType.SetPTPCommonParams(api, 500, 500, isQueued = 0)
        dType.SetHOMEParams(api, 250, 0, 50, 0, isQueued = 0)
        dType.SetPTPJointParams(api, 50, 50, 50, 50, 50, 50, 50, 50, isQueued = 0)
        dType.SetHOMECmd(api, temp = 0, isQueued = 0)
        pose = dType.GetPose(api)
        x_pose = pose[0]
        y_pose = pose[1]
        z_pose = pose[2]
        if key =='main':
            for x_item,y_item in zip(x,y):
                if x_item<315:
                    print("x_item, y_item",x_item,y_item)
                    # for y_item in y:
                    dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
                    dType.SetWAITCmd(api, 200, isQueued=1)
                    dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,30,10, isQueued=1)
                    # dType.SetWAITCmd(api, 200, isQueued=1)
                    dType.SetEndEffectorSuctionCup(api, True,  True, isQueued=1)
                    dType.SetWAITCmd(api, 500, isQueued=1)
                    dType.SetPTPCmd(api,  dType.PTPMode.PTPMOVLXYZMode, x_item,y_item,60,10, isQueued=1)
                    dType.SetWAITCmd(api, 5000, isQueued=1)
                    dType.SetEndEffectorSuctionCup(api, True,  False, isQueued=1)
        if key == 'up':
           dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose,z_pose+10,10,isQueued=1) 
        if key == 'down':
           dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose,z_pose-10,10,isQueued=1) 
        if key == 'right':
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose+10,z_pose,10,isQueued=1)
        if key == 'left':
            dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x_pose,y_pose-10,z_pose,10,isQueued=1)

    #dType.DisconnectDobot(api)
for i in range (10):
    control('up',[500,125],[500,125]) """
