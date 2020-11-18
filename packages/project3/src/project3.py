#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def talker():
	pub = rospy.Publisher("/duck69/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
	rospy.init_node('project3', anonymous=True)
	rate = rospy.Rate(10) #10 Hz
	velocity = 0.4099999964237213
	omega = 8.300000190734863
	while not rospy.is_shutdown():
		pub.publish(Twist2DStamped(header=None, v=velocity, o=omega))
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talker();
	except rospy.ROSInterruptException:
		pass
