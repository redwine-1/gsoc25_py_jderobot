from robot.robot import Robot
from robot.arena import Arena
from robot.animation import visualize

def run_simulation(arena_size: int = 100, steps: int = 1000, visualize_motion: bool = True):
    """
    Run the robot simulation in a square arena.
    
    :param arena_size: Size of the arena (assumed to be square).
    :param steps: Number of steps for the simulation.
    :param visualize_motion: Whether to visualize the robot's motion.
    :return: Array of robot positions during the simulation.
    """

    arena = Arena(arena_size)
    robot = Robot(arena)
    
    positions = robot.run(steps)
    
    if visualize_motion:
        visualize(positions, arena)
    
    return positions

if __name__ == "__main__":
    # Default simulation parameters
    arena_size = 100
    steps = 1000
    
    # Run the simulation with visualization
    run_simulation(arena_size, steps, visualize_motion=True)