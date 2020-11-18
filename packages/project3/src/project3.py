#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped
from std_msgs.msg import Float32

def talker():
	pub = rospy.Publisher("/duck69/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
	rospy.init_node('project3', anonymous=True)
	rate = rospy.Rate(10) #10 Hz
	velocity = 0.3
	o = 2.5
	while not rospy.is_shutdown():
		pub.publish(Twist2DStamped(header=None, v=velocity, omega=o))
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talker();
	except rospy.ROSInterruptException:
		pass
