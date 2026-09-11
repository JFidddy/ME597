import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Timer(Node):
    def __init__(self):
        super().__init__('time_pub')
        self.publisher_ = self.create_publisher(Float32, 'my_first_topic', 10)
        self.timer_period = 5  # seconds
        
        self.start_time = self.get_clock().now()
        self.i = 0
        self.timer = self.create_timer(self.timer_period, self.time_callback)
        
    
    def time_callback(self): 
        elapsed_time = (self.get_clock().now() - self.start_time).nanoseconds / 1e9 #Get current time, convert object to nansecods then to seconds

        msg = Float32()  #Set message type and fill data 
        msg.data = elapsed_time
        #Publish messages and log 
        self.publisher_.publish(msg) 
        self.get_logger().info('Publisher_Time: "%d"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    time_pub = Timer()

    rclpy.spin(time_pub)
    time_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


    
