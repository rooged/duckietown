#!/usr/bin/envpython

import rospy
from std_msgs.msgimport String

class listener:
	def __init__(self):
		rospy.Subscriber("chatter", String, self.callback)

	def callback(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		
if __name__ == '__main__':
	rospy.init_node('listener', anonymous=True)
	listener()

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
