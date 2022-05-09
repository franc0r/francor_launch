from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    tf2_laser_2_base_link = Node(package='tf2_ros',   
                executable='static_transform_publisher',
                name='link_laser_2_base_link', 
                arguments=['-0.14', '0.17', '-0.185','0', '0', '0', '1','laser','base_link'],
                )

    tf2_base_linke_2_base_footprint = Node(package='tf2_ros',   
                executable='static_transform_publisher',
                name='link_base_link_2_base_footprint', 
                arguments=['0', '0', '-0.36','0', '0', '0', '1','base_link','base_footprint'],
                )


    ld.add_action(tf2_laser_2_base_link)
    ld.add_action(tf2_base_linke_2_base_footprint)

    return ld