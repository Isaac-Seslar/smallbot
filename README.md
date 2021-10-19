# Setting up a custom simulated environment in Gazebo 

- Note: Please keep in mind that this is my first time going through this whole process. My hope is just to get the basic idea across for my future reference as well as anyone new. If you find that what I say below is confusing, please open an issue or reach out to me at **iseslar@sandia.gov**.

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

- Looking at the package structure, you will realize that it is broken up in three different parts: small_bot_control, motor_sim, and small_bot. This breakdown is important. 

1. Within `small_bot_control`, each of the joint controllers are defined. See in `small_bot_control/config/small_bot_control.yaml`. This file is pointed to in the small_bot launch file, located in `small_bot/launch/smallbot.launch`. (ELABORATE MORE?)

2. The magic happens inside the motor_sim package. If you look through the file motor_sim_pos.py in scripts, you'll notice all the usual ROS stuff at the bottom under `if __name__ == '__main__'`. The Subscriber and Publisher topics are loaded in the launch file `small_bot.launch` (lines 27-35), which are previously set up in the `small_bot.xacro` file (lines 168-195). `motor_sim_pos.py` then proceeds to start the `main()` function. Within `main()` all I do is run a while loop for as long as ROS is running and publish a different position to each of the joints at a rate of 10Hz. The sleep function is very important; without it, the messages are published too fast for the robot to properly respond to happen. The callback function isn't being used in this code, but the setup is there. If you need to access joint position states, you need to define a callback. To exit the code use `Ctrl + C`.

3. Several files are located within `small_bot`. `config` has a file that defines the names of the joints, I don't think this is being used at the moment. Several tutorials had me a little mixed up. `launch` has all of the launch files used; for this tutorial, we just launch `small_bot.launch`. `meshes` is important; Gazebo is getting all of the model information here, make sure these are defined (you'll see these files should be pointed to in your .xacro file). Finally, we get to `urdf`. Within this directory, is where I keep my `.urdf` and my `.xacro`. Even though I'm not using the `.urdf`, it's still nice to have it if anything needs to be changed.