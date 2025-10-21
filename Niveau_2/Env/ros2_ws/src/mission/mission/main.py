import rclpy
from solution import Solution

def main():
    rclpy.init()
    node = Solution()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()