import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState

class JointService(Node):
    def __init__(self):
        super().__init__('service')
        self.srv = self.create_service(JointState, 'joint_service', self.handle_service)

    def handle_service(self, request, response):
        total = request.x + request.y + request.z #Sum 

        response.valid = total >= 0.0 #IF total < = valid==false
        
        self.get_logger().info(f'Received request: ({request.x}, {request.y}, {request.z}) -> Sum: {total} | Valid: {response.valid}')
        return response

def main(args=None):
    rclpy.init(args=args)

    node = JointService()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()