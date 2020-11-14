#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def talker():
	pub = rospy.Publisher("/homework1/delta", Float32, queue_size=10)
	rospy.init_node('publish', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	total = 0
	while not rospy.is_shutdown():
		total = total + 1
		pub.publish(total)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
