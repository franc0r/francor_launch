#!/bin/bash

# Run docker image
docker run -it --rm  --env ROS_IP=localhost --network=host francor_motion
