import numpy as np

class Arena:
    def __init__(self, size: int = 100):
        """
        Initialize the arena with a given size.
        :param size: Size of the arena (assumed to be square).
        """
        self.size = size

    def is_collision(self, position: np.ndarray) -> bool:
        """
        Check if the robot's position is outside the arena boundaries.
        :param position: Current position of the robot.
        :return: True if the position is outside the arena, False otherwise.
        """
        if position.size != 2:
            raise ValueError("Position must be a 2D vector.") 
        x, y = position
        return x <= 0 or x >= self.size or y <= 0 or y >= self.size