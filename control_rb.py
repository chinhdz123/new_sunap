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
        self.state = dType.ConnectDobot(self.api, "COM4", 115200)[0]
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
    def grip(self,coordinates_rb):
        print(len(coordinates_rb))
        for count, coordinate in enumerate(coordinates_rb):
            if len(coordinate)!= 0 :
                x = coordinate[0]
                y = coordinate[1]
                for x_item,y_item in zip(x,y):
                    if x_item<310:
                        if count == 0:
                            print("count",count)
                            print("x_item, y_item",x_item,y_item)
                            # for y_item in y:
                            
                            # dType.SetPTPCoordinateParams(self.api,500,500,500,500,0)
                            # dType.SetPTPCommonParams(self.api, 500, 500, isQueued = 0)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,30,10, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,-25,10, isQueued=1)
                            # dType.SetWAITCmd(api, 200, isQueued=1)
                            dType.SetEndEffectorSuctionCup(self.api, True,  True, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,50,10, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, -20,-245,30,10, isQueued=1)
                            # dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetEndEffectorSuctionCup(self.api, True,  False, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                        elif count ==1:
                            print("count",count)

                            print("x_item, y_item",x_item,y_item)
                            # for y_item in y:
                            
                            # dType.SetPTPCoordinateParams(self.api,500,500,500,500,0)
                            # dType.SetPTPCommonParams(self.api, 500, 500, isQueued = 0)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,30,10, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,-15,10, isQueued=1)
                            # dType.SetWAITCmd(api, 200, isQueued=1)
                            dType.SetEndEffectorSuctionCup(self.api, True,  True, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,50,10, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, -40,-155,30,10, isQueued=1)
                            # dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetEndEffectorSuctionCup(self.api, True,  False, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                        elif count ==2:
                            print("count",count)

                            print("x_item, y_item",x_item,y_item)
                            # for y_item in y:
                            
                            # dType.SetPTPCoordinateParams(self.api,500,500,500,500,0)
                            # dType.SetPTPCommonParams(self.api, 500, 500, isQueued = 0)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,30,10, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,-7,10, isQueued=1)
                            # dType.SetWAITCmd(api, 200, isQueued=1)
                            dType.SetEndEffectorSuctionCup(self.api, True,  True, isQueued=1)
                            dType.SetWAITCmd(self.api, 500, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, x_item,y_item,70,10, isQueued=1)
                            dType.SetPTPCmd(self.api,  dType.PTPMode.PTPMOVJXYZMode, 80,185,30,10, isQueued=1)
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



