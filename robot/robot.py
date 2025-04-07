import numpy as np
from robot.arena import Arena

class Robot:
    """
    A simple robot class that moves in a 2D arena.
    The robot can move in a random direction and rotate randomly upon collision with the arena boundaries.
    """

    def __init__(self,arena : Arena, speed: float = 1.0):
        """
        Initialize the robot with a direction and center position.
        :param arena_size: Size of the arena (assumed to be square).
        """
        self.arena = arena
        self.position = np.array([arena.size / 2, arena.size / 2])
        self.direction = 0
        self.speed = speed 

    def move(self):
        """
        Move the robot in the current direction.
        """
        self.position += self.speed * np.array([np.cos(self.direction), np.sin(self.direction)])

    def rotate_randomly(self):
        """
        Rotate the robot to a random direction.
        """
        self.direction = np.random.uniform(0, 2 * np.pi)
    
    def run(self, steps: int = 1000) -> np.ndarray:
        """
        Run the robot for a specified number of steps.
        :param steps: Number of steps to run.
        """
        positions = np.zeros((steps, 2))
     
        positions[0] = self.position.copy()

        for i in range(1, steps):
            self.move()
            # Check for collision with the arena boundaries

            if self.arena.is_collision(self.position):
                self.rotate_randomly()
                # Ensure the robot stays within the arena boundaries
                self.position[0] = np.clip(self.position[0], 0, self.arena.size)
                self.position[1] = np.clip(self.position[1], 0, self.arena.size)

            # Store the current position in the array
            positions[i] = self.position.copy()

        return positions