import rclpy
from rclpy.node import Node
from zenmav.core import Zenmav




class Solution(Node):
    def __init__(self):
        super().__init__('solutionLucas')
        self.declare_parameter("zenmav_ip", "tcp:127.0.0.1:5762")
        zenmav_ip = (
            self.get_parameter("zenmav_ip").get_parameter_value().string_value
        )
        self.drone = Zenmav(zenmav_ip, gps_thresh=0.2)

    
    def goToFirstPoint(self):
        self.drone.set_mode('GUIDED')
        self.drone.arm()
        self.drone.takeoff(10.0)
        self.drone.local_target((10, 20, -50))