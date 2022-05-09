from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    genius_front = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('francor_launch'), '/launch/camera_genius.launch.py'])
        )
    genius_back = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('francor_launch'), '/launch/camera_genius_back.launch.py'])
        )

    genius_front_tele = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('francor_launch'), '/launch/camera_genius_tele.launch.py'])
        )
    ylidar = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('francor_launch'), '/launch/ydlidar.launch.py'])
        )

    #topics to multiplex
    front_cam_topic ="camera/front/image_raw/compressed"
    back_cam_topic ="camera/back/image_raw/compressed"

    mux_drive_img = Node(package='topic_tools',   
                executable='mux',
                name='mux_drive_img', 
                arguments=[
                    "camera/drive/image_raw/compressed",
                    front_cam_topic,
                    back_cam_topic
                ],
            )
    
    sensor_head_driver = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('francor_servo_lx16a'), '/launch/default.launch.py'])
        )
    
    robot_base_driver = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('francor_frank_base'), '/launch/frank.launch.py'])
        )
        
    return LaunchDescription([
        genius_front,
        genius_back,
        genius_front_tele,
        sensor_head_driver,
        mux_drive_img,
        ylidar,
        robot_base_driver
    ])