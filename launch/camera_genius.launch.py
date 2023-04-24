from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    cam_front_node = Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam_front_node',
            namespace='camera/front',
            parameters=[
              {"video_device": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:3:1.0-video-index0"},
              #Supported video formats:
              #Motion-JPEG: 1920 x 1080 (30 Hz)
              #Motion-JPEG: 1280 x 720 (60 Hz)
              #Motion-JPEG: 1024 x 768 (30 Hz)
              #Motion-JPEG: 640 x 480 (120 Hz)
              #Motion-JPEG: 800 x 600 (60 Hz)
              #Motion-JPEG: 1280 x 1024 (30 Hz)
              #Motion-JPEG: 320 x 240 (120 Hz)
              #YUYV 4:2:2: 1920 x 1080 (6 Hz)
              #YUYV 4:2:2: 1280 x 720 (9 Hz)
              #YUYV 4:2:2: 1024 x 768 (6 Hz)
              #YUYV 4:2:2: 640 x 480 (30 Hz)
              #YUYV 4:2:2: 800 x 600 (20 Hz)
              #YUYV 4:2:2: 1280 x 1024 (6 Hz)
              #YUYV 4:2:2: 320 x 240 (30 Hz)
              {"image_width": 1920},
              {"image_height": 1080},
              {"framerate": 30.0},	
              {"pixel_format": "mjpeg2rgb"}, #Possible values are mjpeg2rgb (default), yuyv2rgb(ps3 cam ...)
              {"frame_id": "camera_front"},
              {"camera_info_url": "" },
              {"camera_name": "genius"},
              {"autoexposure": False},
              {"best_effort": True},
              {"do_scale": True},
              {"scale_width": 960},
              {"scale_height": 540},
            ]
    )

    return LaunchDescription([
        cam_front_node
    ])