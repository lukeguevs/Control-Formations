import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from zenmav.core import Zenmav

class Solution(Node):
    def __init__(self):
        super().__init__('solution_Lucas')
        
        ##drone configuration
        self.declare_parameter("zenmav_ip", "tcp:127.0.0.1:5762")
        zenmav_ip = (
            self.get_parameter("zenmav_ip").get_parameter_value().string_value
        )
        self.drone = Zenmav(zenmav_ip, gps_thresh=0.2)
        
        self.balloon_position = self.create_subscription(
            PoseStamped,
            '/Ballon_pose',
            self.balloon_callback,
            10
        )
        
        

    def balloon_callback(self, msg):
        self.balloon_position = msg.pose

    def goToFirstPoint(self):
        self.drone.set_mode('GUIDED')
        self.drone.arm()
        self.drone.takeoff(10.0)
        self.drone.local_target((10, 20, -50))
    
