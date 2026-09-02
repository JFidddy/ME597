import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Time(Node):
    def __init__(self):
        super().__init__('time_pub')
        self.publisher_ = self.create_publisher(String, 'my_first_topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.time_call)
        self.t = 0
    
    def time_call(self): 
        msg = String()
        msg.data = "Time Alive: %d" % self.t
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.t += 1

def main(args=None):
    rclpy.init(args=args)

    time_pub = Time()

    rclpy.spin(time_pub)
    time_pub.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()


    
