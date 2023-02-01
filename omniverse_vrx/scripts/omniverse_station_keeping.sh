#!/bin/bash
set -e

source /opt/ros/noetic/setup.bash
source /home/$USER/VRX_Workspace/devel/setup.bash

roslaunch omniverse_vrx omniverse_station_keeping.launch
