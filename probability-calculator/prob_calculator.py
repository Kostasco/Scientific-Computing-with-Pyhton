import copy  # Import the copy module for deep copying objects
import random  # Import the random module for generating random numbers

class Hat:
    def __init__(self, **kwargs):
        # Initialize the Hat object with contents based on the provided colors and quantities
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)

    def draw(self, number):
        # Draw a specified number of balls randomly from the hat
        if number > len(self.contents):
            return self.contents
        balls = []
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Perform a specified number of experiments to determine the probability
    successful_experiments = 0

    for _ in range(num_experiments):
        # Create a deep copy of the original hat for each experiment
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)

        # Check if the drawn balls match the expected_balls
        drawn_balls_count = {color: drawn_balls.count(color) for color in expected_balls}
        match = all(drawn_balls_count[color] >= count for color, count in expected_balls.items())

        if match:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
