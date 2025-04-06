from robot import Robot
from arena import Arena
from animation import visualize

if __name__ == "__main__":
    arena_size = 100
    steps = 1000

    # Create an arena and a robot
    arena = Arena(arena_size)
    robot = Robot(arena)
    
    positions = robot.run(steps)
    visualize(positions, arena)