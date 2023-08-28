#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    rospy.init_node('simple_publisher', anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(10)
    counter = 0
    while not rospy.is_shutdown():
        goodbyeMssg = 'Goodbye World for the ' + str(counter) + 'th time'
        pub.publish(goodbyeMssg)
        rate.sleep()
        counter += 1
