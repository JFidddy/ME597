import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Time(Node):
    def __init__(self):
        super().__init__('time_pub')
        self.publisher_ = self.create_publisher(String, 'my_first_topic', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.time_call)
        self.i = 0
        self.start_time = self.get_clock.now()
    
    def time_call(self): 
        msg = String()
        time_alive = self.get_clock.now() - self.start_time
        msg.data = "Time Alive: %d" % time_alive
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    time_pub = Time()

    rclpy.spin(time_pub)
    time_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


    
