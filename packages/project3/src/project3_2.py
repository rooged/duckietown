#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped
from std_msgs.msg import Float32

def talker():
	pub = rospy.Publisher("/duck69/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
	rospy.init_node('project3_2', anonymous=True)
	rate = rospy.Rate(10) #10 Hz
	time = 0
	turnTime = 0
	while not rospy.is_shutdown():
		pub.publish(Twist2DStamped(header=None, v=0.3, omega=0))
		if time == 35:
			pub.publish(Twist2DStamped(header=None, v=0, omega=0))
			while turnTime < 1650:
				pub.publish(Twist2DStamped(header=None, v=0, omega=9))
				turnTime = turnTime + 1
			time = 0
			turnTime = 0
		time = time + 1
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talker();
	except rospy.ROSInterruptException:
		pass
