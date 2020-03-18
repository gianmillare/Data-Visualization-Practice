from random import choice

class RandomWalk:
    """ Class to generate random walk (values)"""
    def __init__(self, num_points=5000):
        """ Attributes of the walk"""
        self.num_points = num_points

        # The walk will start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]