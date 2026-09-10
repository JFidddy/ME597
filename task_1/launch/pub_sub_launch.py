from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_desc():
    return LaunchDescription([
        Node( 
            package = 'task_1',
            namespace = 'task_1',
            executable ='my_pub',
            name ='task',
            arguments =['--ros-args', '--log-level','info']
        ),
        Node( 
            package = 'task_1',
            namespace = 'task_1',
            executable ='my_pub',
            name ='task',
            output = 'screen',
            arguments =['--ros-args', '--log-level','info']
        ) 
    ])