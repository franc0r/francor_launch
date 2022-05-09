from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    cam_front_node = Node(
            package='usb_cam',   
            executable='usb_cam_node_exe',
            name='back_cam',                  
            parameters=[
              {"video_device": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:4.2:1.0-video-index0"},
              {"image_width": 800},
              {"image_height": 600},
              {"framerate": 30},	
              {"pixel_format": "mjpeg"}, #Possible values are mjpeg (default), yuyv(ps3 cam ...), uyvy
              {"camera_frame_id": "camera"},
              {"camera_info_url": "" },
              {"camera_name": "genius"},
              {"autoexposure": False}
            ]
    )
    ld.add_action(cam_front_node)

    return ld