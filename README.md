# Setting up a custom simulated environment in Gazebo 

## Defining the 3D model for Gazebo
1. To begin, make sure you have updated SolidWorks. At minimum do not use 2018; according to [this webpage](http://wiki.ros.org/sw_urdf_exporter), the 2018 version of SolidWorks has a bug that doesn't allow the URDF exporter to work properly. 

2. After ensuring you have a compatible version of SW, download the [Solidworks to URDF exporter](http://wiki.ros.org/sw_urdf_exporter). Go through the setup on that webpage.

3. When designing your robot, ensure each part is contained in its own part file (i.e. Each joint of the robot is separate or more specifically: a. The body is separate from a wheel b. The arm is separate from the end effector, etc.). When finished, assemble each of the parts in an Assembly file (.SLDASM).

4. Once an assembly has been established, use this very useful tutorial on how to export an Assembly to URDF: [Export a SolidWorks Assembly to URDF](http://wiki.ros.org/sw_urdf_exporter/Tutorials/Export%20an%20Assembly).

5. Make sure to define limits to the joints. This can be done later in the .xacro or .URDF file. Gazebo may experience some silent errors if not defined. These limits can be seen towards the bottom of the link def in the uploaded `small_bot.xacro` file (ex. line 162-165).

	- A .xacro file and a .URDF file are very similar. *As far as I understand*, the .xacro is basically a macro that generates a .URDF file from scratch. This is helpful when adding colors, textures, and (most importantly) control.

	- It should be easiest to show rather than try and explain the differences. Take a look at the files `small_bot.urdf` and `small_bot.xacro` to see the major differences. The .urdf file was created by the SW to urdf exporter and the xacro was the file edited and saved by me.

6. Once finished, make sure to edit the launch file to launch the .xacro instead of the .urdf (See `small_bot.launch`).

## Controlling the robot in Gazebo

1. Looking at the package structure, you will realize that it is broken up in three different parts: small_bot_control, motor_sim, and small_bot. 
	- Within small_bot_control, each of the joint controllers are defined. See in small_bot_control/config/small_bot_control.yaml. This file is pointed to in the small_bot launch file, located in small_bot/launch/smallbot.launch. (ELABORATE MORE?)

	- 