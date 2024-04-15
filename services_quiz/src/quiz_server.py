#! /usr/bin/env python

import rospy
import time, datetime
from geometry_msgs.msg import Twist
from services_quiz.srv import servicesQuiz, servicesQuizResponse

def my_callback(request):
	print("Checking if it works beep - - - boop")
	
	turn = Twist()
	i = 0
	duration = request.duration 
	start_time = rospy.get_time()
	
	while start_time + duration > rospy.get_time() :
		print('debug'+ str(i))
		if (request.direction == 'clockwise'):
			turn.angular.z = -0.5
			pub.publish(turn)
		elif (request.direction == 'counter clockwise'):
			turn.angular.z = 0.5
			pub.publish(turn)
		
		i = i+1
		rate.sleep()
	
	turn.angular.z = 0
	turn.linear.x = 0
	print('stop')
	pub.publish(turn)
	
	response = servicesQuizResponse()
	response.succes = True
	
	return response
	
rospy.init_node('quiz_server_spin')

srvQuiz = rospy.Service('/srvQuiz', servicesQuiz, my_callback)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

rate = rospy.Rate(2)

rospy.spin()
