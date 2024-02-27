# simple_agent.py 
from agent_behaviours import go_towards_target
from agent_behaviours import enforce_field_boundaries
from agent import agent
import numpy as np

class SimpleAgent(agent):
    def __init__(self, id):
        super().__init__(id)
        self.target_position = None # Initialise with no target


    def set_target(self, target_position):        
        if not any(coord is None for coord in target_position):
            # target_position = super().check_boundary(target_position)
            self.target_position = np.array(target_position)


    def act(self, frame):




        #FIELD_WIDTH = 2760 #mm
        #FIELD_LENGTH = 5040 #mm


        my_x = frame['detection']['robots_blue'][self.id]['x']
        my_y = frame['detection']['robots_blue'][self.id]['y']
        my_position = (my_x, my_y)

        self.vx, self.vy = go_towards_target(self.target_position, my_position, slow_threshold=100, stop_threshold=0)


        #self.vx, self.vy = enforce_field_boundaries(my_x, my_y, self.vx, self.vy)
        self.vw = 0 

        return self.id, self.vx, self.vy, self.vw