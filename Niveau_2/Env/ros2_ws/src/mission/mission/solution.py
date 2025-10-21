##Auteur: Lucas Guevremont, Zenith Polytechnique Montreal
##Date: 2025-10-21

from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from rclpy.subscription import Subscription
from rclpy.publisher import Publisher
from zenmav.core import Zenmav
from zenmav.zenpoint import wp
from std_msgs.msg import String

class Solution(Node):
    def __init__(self):
        super().__init__('solution_Lucas')
        
        ##arrival configuration
        self.arrival_pub : Publisher = self.create_publisher(String, '/arrival', 10)
        
        ##drone configuration
        self.declare_parameters()

        self.balloon_position : Subscription = self.create_subscription(
            PoseStamped,
            '/Ballon_pose',
            self.balloon_callback,
            20
        )
        self.follow : bool = True
        self.last_x : float = None
        self.last_y : float = None
        self.last_z : float = None

        self.get_logger().info('Node initialized, ready to follow the balloon')
        self.go_to_first_point()
        
    def balloon_callback(self, msg: PoseStamped) -> None:
        self.balloon_position = msg.header.stamp
        
        x : float = float(msg.pose.position.x)
        y : float = float(msg.pose.position.y)
        z : float = float(msg.pose.position.z)
        
        if self.first:
            self.first = False

            if self.follow:
                self.get_logger().info('Following the balloon')
                new_wp = wp(y, x, z - self.look_ahead)
                self.drone.local_target(new_wp, wait_to_reach=False)
                self.get_logger().info(f'SENDING TO {new_wp.coordinates} m NED')

        
        
        
    def declare_parameters(self) -> None:
        self.declare_parameter("zenmav_ip", "tcp:127.0.0.1:5762")
        zenmav_ip = (
            self.get_parameter("zenmav_ip").get_parameter_value().string_value
        )
        self.declare_parameter("takeoff_alt", 10.0)
        self.takeoff_alt = (
            self.get_parameter("takeoff_alt").get_parameter_value().double_value
        )
        self.declare_parameter("look_ahead", 1.0)
        self.look_ahead = (
            self.get_parameter("look_ahead").get_parameter_value().double_value
        )
        
        self.drone = Zenmav(zenmav_ip, gps_thresh=0.2)
        

    def go_to_first_point(self) -> None:
        self.drone.arm()
        self.drone.set_mode('GUIDED')
        self.drone.takeoff(self.takeoff_alt)
        self.drone.local_target((10, 20, -50))  # NED
        self.arrival_pub.publish(String(data='Lucas'))
        
        
        
        
        
    
