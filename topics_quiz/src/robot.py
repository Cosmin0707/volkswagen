#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):  
    print (msg.ranges[0])
    if msg.ranges[0] < 1:
      #stop turn left
      turn.linear.x = 0
      turn.angular.z = 0
      pub.publish(turn)
      time.sleep(2)
      
      for i in range(4):
      	turn.angular.z = 0.2
      	pub.publish(turn) 
      	time.sleep(2)
      	i+=1
      
      turn.linear.x = 0.2
      turn.angular.z = 0
      pub.publish(turn)
      time.sleep(2)
      
      turn.linear.x = 0
      turn.angular.z = 0
      pub.publish(turn)
      time.sleep(2)
      
      turn.linear.x = 0.2
      turn.angular.z = 0
      pub.publish(turn)
      time.sleep(2)
      
      #for i in range(4):
      	#turn.angular.z = -0.2
      	#turn.linear.x = 0
      	#pub.publish(turn) 
      	#time.sleep(2)
      	#i+=1
      
    #mers inainte
    turn.linear.x = 0.2
    pub.publish(turn)
    
rospy.init_node('scan_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1) 
sub = rospy.Subscriber('/scan', LaserScan, callback) 

rate = rospy.Rate(2)
turn = Twist()

rospy.spin()
