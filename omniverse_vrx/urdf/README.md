1. Change directory to `/omniverse_vrx/wamv` and edit the `component_config.yaml` and `thruster_config.yaml` files as required.

2. Launch the `omniverse_build_wamv.launch` file to build WAM-V as per the specifications of `component_config.yaml` and `thruster_config.yaml` files.
```bash
$ roslaunch <PACKAGE_NAME> <LAUNCH_FILE_NAME>.launch

$ roslaunch omniverse_vrx omniverse_build_wamv.launch
```

3. The built WAM-V will be saved to `/omniverse_vrx/urdf` directory as `omniverse.urdf` file by default (configurable through `omniverse_build_wamv.launch` file in `/omniverse_vrx/launch/tools` directory).
