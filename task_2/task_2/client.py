import sys
import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState

class JointClient(Node):
    def __init__(self):
        super().__init__('client')

        self.cli = self.create_client(JointState, 'joint_service')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

    def send_request(self):
        req = JointState.Request()
        req.x, req.y, req.z = 5.0, -7.0, -32.1
        return self.cli.call_async(req)

def main():
    rclpy.init()
    client = JointClient()
    ##Allows Node input on launch, defaults to 4,-6,1
    
    future = client.send_request()
    rclpy.spin_until_future_complete(client, future)

    res = future.result()
    client.get_logger().info(f'Result: {res.valid}')

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()