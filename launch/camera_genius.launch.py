from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    cam_front_node = Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam_front_node',
            namespace='camera/front',
            parameters=[
              {"video_device": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:3:1.0-video-index0"},
              {"image_width": 640},
              {"image_height": 480},
              {"framerate": 30.0},	
              {"pixel_format": "mjpeg2rgb"}, #Possible values are mjpeg2rgb (default), yuyv2rgb(ps3 cam ...)
              {"camera_frame_id": "camera"},
              {"camera_info_url": "" },
              {"camera_name": "genius"},
              {"autoexposure": False},
              {"best_effort": True}
            ]
    )
    ld.add_action(cam_front_node)

    return ld