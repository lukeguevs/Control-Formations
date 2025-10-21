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
            20
        )
        
        self.declare_parameter("takeoff_alt", 10.0)
        self.takeoff_alt = (
            self.get_parameter("takeoff_alt").get_parameter_value().double_value
        )
        self.get_logger().info('Node initialized, ready to follow the balloon')
        self.goToFirstPoint()
        
    def balloon_callback(self, msg) -> None:
        self.balloon_position = msg.pose
        

    def goToFirstPoint(self) -> None:
        self.drone.set_mode('GUIDED')
        self.drone.arm()
        self.drone.takeoff(10.0)
        self.drone.local_target((10, 20, -50))
    
