from random import choice

class RandomWalk:
    """ Class to generate random walk (values)"""
    def __init__(self, num_points=5000):
        """ Attributes of the walk"""
        self.num_points = num_points

        # The walk will start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate all the points of the walk"""

        # Keep walking until the max points is reached
        while len(self.x_values) < self.num_points

            # We decide where to go and how far in that direction

            x_direction = choice([1, -1]) # random choice to move right (1) or left (-1)
            x_distance = choice([0, 1, 2, 3, 4]) # random choice to move a distance between 0-4, 0 meaning move vertically
            x_step = x_direction * x_distance

            y_direction = choice([1, -1]) # random choice to move up(1) or down (-1)
            y_distance = choice([0, 1, 2, 3, 4]) # random choice to move a distance between 0-4
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0: # if the choice returns (0, 0), we ignore it and move to the next step
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step # add the x_step into the empty list of self.x_values
            y = self.y_values[-1] + y_step # add the y_step into the empty list of self.y_values

            # Store the values by appending them into the empty list
            self.x_values.append(x)
            self.y_values.append(y)