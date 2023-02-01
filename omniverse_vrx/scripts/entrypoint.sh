#!/bin/bash
set -e

source /opt/ros/noetic/setup.bash
source /home/$USER/VRX_Workspace/devel/setup.bash

x11vnc -forever -usepw -create & /bin/bash
