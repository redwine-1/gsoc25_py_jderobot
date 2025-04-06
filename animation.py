import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from arena import Arena


def visualize(positions: np.ndarray, arena: Arena):
    """
    Visualize the robot's motion in the arena and save the animation as a GIF.
    :param positions: Array of positions of the robot.
    :param arena: Arena object containing the size of the arena.
    """
    positions = positions
    fig, ax = plt.subplots()
    padding = 5  


    ax.set_xlim(-padding, arena.size + padding)
    ax.set_ylim(-padding, arena.size + padding)
    ax.set_aspect('equal')
    ax.set_title("Robot Motion in Arena")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.grid(True)

    # Draw the arena boundaries
    ax.plot([0, 0, arena.size, arena.size, 0], [0, arena.size, arena.size, 0, 0], 'k-')  
    
    point, = ax.plot([], [], 'ro')  
    path, = ax.plot([], [], 'b-', alpha=0.5)  

    def init() -> tuple[plt.Line2D, plt.Line2D]:
        """
        Initialize the animation.
        """
        point.set_data([], [])
        path.set_data([], [])
        return point, path

    def update(frame) -> tuple[plt.Line2D, plt.Line2D]:
        """
        Update the animation for each frame.
        :param frame: Current frame number.
        """
        point.set_data(positions[frame][0], positions[frame][1])
        path.set_data(positions[:frame+1, 0], positions[:frame+1, 1])
        return point, path

    ani = FuncAnimation(fig, update, frames=len(positions), init_func=init, blit=True, interval=20)
    ani.save("robot_motion.gif", writer="pillow") 
    plt.show()