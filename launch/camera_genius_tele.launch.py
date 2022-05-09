from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    cam_tele_node = Node(
            package='usb_cam',   
            executable='usb_cam_node',
            name='cam_tele',                  
            parameters=[
              {"video_device": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:4.3:1.0-video-index0"},
              {"image_width": 1920},
              {"image_height": 1080},
              {"framerate": 6},	
              {"pixel_format": "yuyv"}, #Possible values are mjpeg (default), yuyv(ps3 cam ...), uyvy
              {"camera_frame_id": "camera_tele"},
              {"camera_info_url": "" },
              {"camera_name": "tele"},
              {"autoexposure": False}
            ]
    )
    ld.add_action(cam_tele_node)

    return ld