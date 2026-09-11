import rclpy
from rclpy.node import Node
from task_2_interfaces.msg import JointData

class JointPub(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(JointData, 'joint_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = JointData() 
        msg.center.x = 5.0  #Set Data Values 
        msg.center.y = 2.5
        msg.center.z = 7.8
        msg.vel = 20.0
        self.publisher_.publish(msg) #Send Message 
        self.get_logger().info(f'Publishing: center=({msg.center.x}, {msg.center.y}, {msg.center.z}), vel={msg.vel}')
            #Note to logger
def main(args=None):
    rclpy.init(args=args) #initialize 
    
    node = JointPub() #define
    #Repaeat the Node
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()