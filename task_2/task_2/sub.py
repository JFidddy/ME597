import rclpy
from rclpy.node import Node
from task_2_interfaces.msg import JointData

class JointSub(Node):
    def __init__(self):
        super().__init__('listener') #Subscript to the joint_topic. 
        self.subscription = self.create_subscription(
            JointData,
            'joint_topic',
            self.listener_callback,10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received JointData -> Center: ({msg.center.x:.2f}, {msg.center.y:.2f}, {msg.center.z:.2f}), Vel: {msg.vel:.2f}')

def main(args=None):
    rclpy.init(args=args) #initialize

    node = JointSub() #define 

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()