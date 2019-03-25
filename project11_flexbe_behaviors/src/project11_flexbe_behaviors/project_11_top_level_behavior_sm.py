#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from project11_flexbe_states.standby_state import StandbyState
from project11_flexbe_states.manual_state import ManualState
from project11_flexbe_states.autonomous_state import AutonomousState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Mar 18 2019
@author: Roland Arsenault
'''
class Project11TopLevelBehaviorSM(Behavior):
    '''
    Handles the top level states for the Project11 Backseat Driver
    '''


    def __init__(self):
        super(Project11TopLevelBehaviorSM, self).__init__()
        self.name = 'Project 11 Top Level Behavior'

        # parameters of this behavior

        # references to used behaviors

        # Additional initialization code can be added inside the following tags
        # [MANUAL_INIT]
		
		# [/MANUAL_INIT]

        # Behavior comments:



    def create(self):
        # x:30 y:365, x:130 y:365
        _state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

        # Additional creation code can be added inside the following tags
        # [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


        with _state_machine:
            # x:245 y:69
            OperatableStateMachine.add('standby',
                                        StandbyState(),
                                        transitions={'manual': 'manual', 'autonomous': 'autonomous'},
                                        autonomy={'manual': Autonomy.Off, 'autonomous': Autonomy.Off})

            # x:54 y:267
            OperatableStateMachine.add('manual',
                                        ManualState(),
                                        transitions={'autonomous': 'autonomous', 'standby': 'standby'},
                                        autonomy={'autonomous': Autonomy.Off, 'standby': Autonomy.Off})

            # x:423 y:269
            OperatableStateMachine.add('autonomous',
                                        AutonomousState(),
                                        transitions={'manual': 'manual', 'standby': 'standby'},
                                        autonomy={'manual': Autonomy.Off, 'standby': Autonomy.Off})


        return _state_machine


    # Private functions can be added inside the following tags
    # [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
