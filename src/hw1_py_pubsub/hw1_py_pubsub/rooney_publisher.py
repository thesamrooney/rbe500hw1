
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class RooneyPublisher(Node):

    def __init__(self):
        super().__init__("rooney_hw1_publisher")
        self.publisher_ = self.create_publisher(String, "rooneytest", 10)
        timer_period = 1 #second
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = str(self.i)
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: '%s'" % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    rooney_publisher = RooneyPublisher()
    rclpy.spin(rooney_publisher)

    # destroy the node
    # the garbage collector can handle this as well, but we can do it explicitly
    rooney_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()







