#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(data):
	rospy.loginfo("log info %s", data.data)

def listener():
	rospy.init_node('subscribe', anonymous=True)
	
	rospy.Subscriber("/homework1/total", Float32, callback)

	rospy.spin()
		
if __name__ == '__main__':
	listener()
