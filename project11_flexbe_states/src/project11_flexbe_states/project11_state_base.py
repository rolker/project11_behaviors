#!/usr/bin/env python
import rospy

from flexbe_core.proxy import ProxySubscriberCached
from sensor_msgs.msg import Joy

class Project11StateBase():
    '''
    Base class for Project11 states. 
    Handles operations, such as interpreting jostick buttons, that are common to many states.
    '''
    
    def __init__(self):
        self.base_subscribers = ProxySubscriberCached({'/joy':Joy})

    def checkJoystick(self):
        if self.base_subscribers.has_msg('/joy'):
            msg = self.base_subscribers.get_last_msg('/joy')
            state_request = None
            if msg.buttons[0]:
                state_request = 'manual'
            if msg.buttons[1]:
                state_request = 'autonomous'
            if msg.buttons[2]:
                state_request = 'standby'
            return msg,state_request
