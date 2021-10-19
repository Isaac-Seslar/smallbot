#! /usr/bin/python3

import rospy
import tf 
import control_msgs

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

class sb:
	joint_pos_1 = float()
	joint_pos_2 = float()
	# joint_command_pub = float()
	# joint_position_pub = float()

def joint_pos_callback(msg):

	 sb.joint_pos_1 = msg.position[0]
	 sb.joint_pos_2 = msg.position[1]

	 # joint_pos_1 = msg.sensor_msgs.JointState.position
	 # joint_pos_2 = msg.sensor_msgs.JointState.position[1]

def main():
	
	inf_loop = 1
	start1 = 0
	start2 = 0

	while not rospy.is_shutdown():

		sb.joint_pos_cmd0 = start1
		sb.joint_pos_cmd1 = start2

		joint_command_pub0.publish(sb.joint_pos_cmd0)
		joint_command_pub1.publish(sb.joint_pos_cmd1)


		start1+=0.1
		start2+=0.1
		print(start1)
		rate.sleep()


if __name__ == '__main__':

	rospy.init_node('motor_sim', anonymous=False)
	rate=rospy.Rate(10)
	#--------------- Subscribers ---------------#
	joint_status_sub   = rospy.Subscriber(
							'/small_bot/joint_states', 
							JointState,
							joint_pos_callback, 
							queue_size=1)


	#---------------- Publishers ---------------#
	joint_command_pub0  = rospy.Publisher('/small_bot/joint_1_controller/command',Float64,queue_size=1) 

	joint_command_pub1  = rospy.Publisher(
							'/small_bot/joint_2_controller/command',
							Float64,
							queue_size=1) 

	joint_position_pub0 = rospy.Publisher(
							'/small_bot/joint_1_controller/position',
							Float64,
							queue_size=1
								)
	joint_position_pub1 = rospy.Publisher(
							'/small_bot/joint_2_controller/position',
							Float64,
							queue_size=1
								)


	rospy.loginfo("================================================")
	rospy.loginfo("========== Starting Motor Control ==============")
	rospy.loginfo("================================================")

	main()
