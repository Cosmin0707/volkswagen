#! /usr/bin/env python

import rospy
from services_quiz.srv import servicesQuiz, servicesQuizRequest
import sys

rospy.init_node('spin_client')

rospy.wait_for_service('/quiz_server_spin')

spin_service = rospy.Service('/quiz_server_spin', servicesQuiz)
spin_object = servicesQuizRequest()

result = spin_service(spin_object)

print(result)
