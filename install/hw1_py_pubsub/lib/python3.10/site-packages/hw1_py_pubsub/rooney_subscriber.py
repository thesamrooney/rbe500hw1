
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class RooneySubscriber(Node):

    def __init__(self):
        super().__init__("rooney_subscriber")
        self.subscription = self.create_subscription(
                String,
                "rooneytest",
                self.listener_callback,
                10)
        self.subscription #suppress warning

    def listener_callback(self, msg):
        num = msg.data
        evenodd = ""
        if int(num) % 2 == 0:
            evenodd = "even"
        else:
            evenodd = "odd"
        self.get_logger().info("I recieved %s. It is an %s number." % (num, evenodd))

def main(args=None):
    rclpy.init(args=args)

    rooney_subscriber = RooneySubscriber()

    rclpy.spin(rooney_subscriber)

    rooney_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
