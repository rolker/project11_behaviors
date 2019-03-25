#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger
from project11_state_base import Project11StateBase

from marine_msgs.msg import Helm

from flexbe_core.proxy import ProxyPublisher

class ManualState(EventState):
    '''
    Project11 state where vehicle is operated from joystick commands.
    '''

    def __init__(self):
        # Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
        super(ManualState, self).__init__(outcomes = ['autonomous', 'standby'])
        
        self.publishers = ProxyPublisher({'/helm':Helm})
        self.p11sb = Project11StateBase()

    def execute(self, userdata):
        # This method is called periodically while the state is active.
        # Main purpose is to check state conditions and trigger a corresponding outcome.
        # If no outcome is returned, the state will stay active.
        js = self.p11sb.checkJoystick()
        if js is not None:
            requested_state = js[1]
            if requested_state is not None and requested_state != 'manual':
                return requested_state
            msg = js[0]
            helm = Helm()
            helm.header.stamp = rospy.Time.now()
            helm.throttle = msg.axes[1]
            helm.rudder = -msg.axes[3]
            self.publishers.publish('/helm',helm)
            

    def on_enter(self, userdata):
        # This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
        # It is primarily used to start actions which are associated with this state.
        pass

    def on_exit(self, userdata):
        # This method is called when an outcome is returned and another state gets active.
        # It can be used to stop possibly running processes started by on_enter.

        pass # Nothing to do in this example.


    def on_start(self):
        # This method is called when the behavior is started.
        # If possible, it is generally better to initialize used resources in the constructor
        # because if anything failed, the behavior would not even be started.
        pass

    def on_stop(self):
        # This method is called whenever the behavior stops execution, also if it is cancelled.
        # Use this event to clean up things like claimed resources.

        pass # Nothing to do in this example.
            
