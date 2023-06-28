import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():


  return LaunchDescription([


        Node(
                package='self_driving_car_pkg',
                executable='video_recording_node',
                name='video_recorder',
                output='screen'),

        Node(
                package='self_driving_car_pkg',
                executable='computer_vision_node',
                name='computer_vision',
                output='screen'),


        

    ])
