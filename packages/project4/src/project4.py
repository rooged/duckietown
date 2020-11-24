#!/usr/bin/env python3

import rospy
import math
from duckietown_msgs.msg import Twist2DStamped
from duckietown_msgs.msg import Pose2DStamped
from std_msgs.msg import Float32

global phi
phi = None

class robot:	
	def __init__(self):
		self.phi_previous_error = 0
		self.d_previous_error = 0
		self.set_point = 1
		self.kp = 1
		self.ki = 0
		self.kd = 0
		self.integral = 0
		self.dt = .1
		
	def pid(self, measured_value):
		self.error = self.set_point - measured_value
		self.derivative = (self.error - self.previous_error) / self.dt
		self.previous_error = self.error

		return self.kp * self.error + self.kd * self.derivative
		
class talker:
	def callback(data):
		value = data

	def __init__(self):
		self.sub = rospy.Subscriber("/duck69/lane_controller_node/lane_post", Pose2DStamped, self.callback)
		self.pub = rospy.Publisher("/duck69/car_cmd_switch_node/cmd", Twist2DStamped, queue_size=10)

	def talk():
		r = robot()
		velocity = .3
		o = r.pid(phi)
		pub.publish(Twist2DStamped(header=None, v=velocity, omega=o))
		
if __name__ == '__main__':
	try:
		t = start()
		rospy.init_node('project4', anonymous=True)
		rate = rospy.Rate(10) #10 Hz
		while not rospy.is_shutdown():
			rospy.loginfo("Timothy Gedney lane following node")
			t.talk()
			rate.sleep()
			rospy.spin()
	except rospy.ROSInterruptException:
		pass
