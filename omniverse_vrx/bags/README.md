# Omniverse-VRX
 | Bag Files

Record and playback bag files for all Omniverse-VRX
 simulation tasks with the `rosbag` command line interface (CLI). Note that the `record` launch files provided in the `Omniverse-VRX
` package will export recorded bag files to the `bags` directory and the `playback` launch files provided in the `Omniverse-VRX
` package will read recorded bag files from the `bags` directory.

## Recording New Bag Files

Launch Omniverse-VRX
 `record` launch files.
```bash
$ roslaunch omniverse_vrx record_<TASK_NAME>.launch

$ roslaunch omniverse_vrx record_station_keeping.launch
$ roslaunch omniverse_vrx record_wayfinding.launch
$ roslaunch omniverse_vrx record_scene_perception.launch
$ roslaunch omniverse_vrx record_semantic_navigation.launch
$ roslaunch omniverse_vrx record_gymkhana_challenge.launch
$ roslaunch omniverse_vrx record_scan_dock_deliver.launch
```

## Playing Back Recorded Bag Files

Launch Omniverse-VRX
 `playback` launch files.
```bash
$ roslaunch omniverse_vrx playback_<TASK_NAME>.launch

$ roslaunch omniverse_vrx playback_station_keeping.launch
$ roslaunch omniverse_vrx playback_wayfinding.launch
$ roslaunch omniverse_vrx playback_scene_perception.launch
$ roslaunch omniverse_vrx playback_semantic_navigation.launch
$ roslaunch omniverse_vrx playback_gymkhana_challenge.launch
$ roslaunch omniverse_vrx playback_scan_dock_deliver.launch
```
