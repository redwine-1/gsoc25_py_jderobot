from robot.simulator import run_simulation

if __name__ == "__main__":
    # Default simulation parameters
    arena_size = 100
    steps = 1000
    
    # Run the simulation with visualization
    run_simulation(arena_size, steps, visualize_motion=True)