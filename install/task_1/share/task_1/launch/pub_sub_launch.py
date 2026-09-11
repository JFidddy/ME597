from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='task_1',
            namespace='task1',
            executable='talker',
            name='talk',
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='task_1',
            namespace='task1',
            executable='listener',
            name='lis',
            output = 'screen', 
            ros_arguments=['--log-level', 'info']
        )
    ])