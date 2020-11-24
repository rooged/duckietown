#!/usr/bin/env python3

import rospy
import math
from duckietown_msgs.msg import Twist2DStamped
from duckietown_msgs.msg import Pose2DStamped
from std_msgs.msg import Float32
from std_msgs.msg import String

global phi
phi = 0

class robot:	
	def __init__(self):
		self.previous_error = 0
		self.set_point = 1
		self.kp = 1.5
		self.ki = 0
		self.kd = 4
		self.integral = 0
		self.dt = .1
		
	def pid(self, measured_value):
		self.error = self.set_point - measured_value
		self.derivative = (self.error - self.previous_error) / self.dt
		self.previous_error = self.error

		return self.kp * self.error + self.kd * self.derivative

def callback(data):
	phi = data.data

def talk():
	rospy.init_node('project4', anonymous=True)
	rate = rospy.Rate(10) #10 Hz
	pub = rospy.Publisher("/duck69/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)
	r = robot()
	while not rospy.is_shutdown():
		rospy.Subscriber("/duck69/lane_controller_node/lane_post", Pose2DStamped, callback)
		rospy.loginfo("Timothy Gedney lane following node")
		o = r.pid(phi)
		pub.publish(Twist2DStamped(header=None, v=.15, omega=o))
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talk()
	except rospy.ROSInterruptException:
		pass
