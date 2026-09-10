import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class TimeSubscriber(Node):

    def __init__(self):

        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'my_first_topic',
            self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        doubletime = msg.data * 2
        self.get_logger().info('Publisher Time: "%f" Doubled: %f' % msg.data, doubletime)


def main(args=None):
    rclpy.init(args=args)

    my_sub = TimeSubscriber()

    rclpy.spin(my_sub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    my_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
