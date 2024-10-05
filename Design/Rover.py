# Rover Control System with Obstacle Handling as Separate Classes

class Obstacle:
    def __init__(self, x, y):
        """
        Initialize an obstacle at position (x, y).
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Check equality based on coordinates.
        """
        return isinstance(other, Obstacle) and self.x == other.x and self.y == other.y

    def __hash__(self):
        """
        Hash based on coordinates to allow usage in sets.
        """
        return hash((self.x, self.y))

    def __repr__(self):
        """
        String representation of the obstacle.
        """
        return f"Obstacle({self.x}, {self.y})"


class ObstacleManager:
    def __init__(self):
        """
        Initialize the Obstacle Manager with an empty set of obstacles.
        """
        self.obstacles = set()

    def add_obstacle(self, x, y):
        """
        Add a new obstacle at (x, y).
        """
        obstacle = Obstacle(x, y)
        if obstacle in self.obstacles:
            print(f"Obstacle already exists at ({x}, {y}).")
            return False
        self.obstacles.add(obstacle)
        print(f"Obstacle added at ({x}, {y}).")
        return True

    def remove_obstacle(self, x, y):
        """
        Remove an obstacle from (x, y).
        """
        obstacle = Obstacle(x, y)
        if obstacle not in self.obstacles:
            print(f"No obstacle found at ({x}, {y}) to remove.")
            return False
        self.obstacles.remove(obstacle)
        print(f"Obstacle removed from ({x}, {y}).")
        return True

    def is_obstacle(self, x, y):
        """
        Check if there's an obstacle at (x, y).
        """
        return Obstacle(x, y) in self.obstacles

    def list_obstacles(self):
        """
        List all current obstacles.
        """
        if not self.obstacles:
            print("No obstacles present.")
            return []
        sorted_obstacles = sorted(self.obstacles, key=lambda o: (o.x, o.y))
        print("Current obstacles at positions:")
        for obs in sorted_obstacles:
            print(f"({obs.x}, {obs.y})")
        return sorted_obstacles


class Rover:
    def __init__(self, obstacle_manager=None):
        """
        Initialize the rover at position (0, 0) facing North with an optional Obstacle Manager.
        """
        self.x = 0  # X-coordinate
        self.y = 0  # Y-coordinate
        self.directions = ['North', 'East', 'South', 'West']  # Possible directions
        self.direction_index = 0  # Index to track current direction in the directions list
        self.obstacle_manager = obstacle_manager if obstacle_manager else ObstacleManager()

    def move(self):
        """
        Move the rover one unit forward in the current facing direction.
        Checks for obstacles before moving.
        """
        # Determine the next position based on the current direction
        current_direction = self.directions[self.direction_index]
        next_x, next_y = self.x, self.y

        if current_direction == 'North':
            next_y += 1
        elif current_direction == 'East':
            next_x += 1
        elif current_direction == 'South':
            next_y -= 1
        elif current_direction == 'West':
            next_x -= 1

        # Check for obstacle at the next position
        if self.obstacle_manager.is_obstacle(next_x, next_y):
            print(f"Cannot move to ({next_x}, {next_y}). Obstacle detected!")
            return

        # Update position if no obstacle
        self.x, self.y = next_x, next_y
        print(f"Moved to ({self.x}, {self.y}) facing {self.directions[self.direction_index]}.")

    def turn_left(self):
        """
        Rotate the rover 90 degrees to the left.
        """
        # Turning left decreases the direction index by 1 (modulo 4 to wrap around)
        self.direction_index = (self.direction_index - 1) % 4
        print(f"Turned left. Now facing {self.directions[self.direction_index]}.")

    def turn_right(self):
        """
        Rotate the rover 90 degrees to the right.
        """
        # Turning right increases the direction index by 1 (modulo 4 to wrap around)
        self.direction_index = (self.direction_index + 1) % 4
        print(f"Turned right. Now facing {self.directions[self.direction_index]}.")

    def report(self):
        """
        Return the current position and facing direction of the rover.
        """
        position = f"Rover is at ({self.x}, {self.y}) facing {self.directions[self.direction_index]}."
        print(position)
        return position

    def add_obstacle(self, x, y):
        """
        Add an obstacle at (x, y) via the Obstacle Manager.
        """
        if (x, y) == (self.x, self.y):
            print("Cannot place an obstacle at the rover's current position.")
            return False
        return self.obstacle_manager.add_obstacle(x, y)

    def remove_obstacle(self, x, y):
        """
        Remove an obstacle from (x, y) via the Obstacle Manager.
        """
        return self.obstacle_manager.remove_obstacle(x, y)

    def list_obstacles(self):
        """
        List all current obstacles via the Obstacle Manager.
        """
        return self.obstacle_manager.list_obstacles()


def process_command(rover, command):
    """
    Process a single command and execute the corresponding rover method.
    Supports obstacle management commands.
    """
    command = command.strip().upper()  # Normalize command
    tokens = command.split()

    if not tokens:
        print("No command entered. Please enter a valid command.")
        return True  # Continue the loop

    if tokens[0] == 'MOVE':
        rover.move()
    elif tokens[0] == 'TURN':
        if len(tokens) < 2:
            print("Invalid TURN command. Specify LEFT or RIGHT.")
            return True
        if tokens[1] == 'LEFT':
            rover.turn_left()
        elif tokens[1] == 'RIGHT':
            rover.turn_right()
        else:
            print("Invalid TURN direction. Use LEFT or RIGHT.")
    elif tokens[0] == 'REPORT':
        rover.report()
    elif tokens[0] == 'ADD' and len(tokens) >= 4 and tokens[1] == 'OBSTACLE':
        try:
            x = int(tokens[2])
            y = int(tokens[3])
            rover.add_obstacle(x, y)
        except ValueError:
            print("Invalid coordinates for ADD OBSTACLE. Use integers for x and y.")
    elif tokens[0] == 'REMOVE' and len(tokens) >= 4 and tokens[1] == 'OBSTACLE':
        try:
            x = int(tokens[2])
            y = int(tokens[3])
            rover.remove_obstacle(x, y)
        except ValueError:
            print("Invalid coordinates for REMOVE OBSTACLE. Use integers for x and y.")
    elif tokens[0] == 'LIST' and len(tokens) >= 2 and tokens[1] == 'OBSTACLES':
        rover.list_obstacles()
    elif tokens[0] == 'EXIT':
        print("Exiting the Rover Control System. Goodbye!")
        return False  # Signal to terminate the loop
    else:
        print("Invalid command. Please enter a valid command:")
        print("MOVE, TURN LEFT, TURN RIGHT, REPORT, ADD OBSTACLE x y, REMOVE OBSTACLE x y, LIST OBSTACLES, EXIT.")
    return True  # Continue the loop


def main():
    """
    Main function to run the Rover Control System command-line application with obstacle handling.
    """
    rover = Rover()
    print("Welcome to the Enhanced Rover Control System with Obstacle Handling!")
    print("Available commands:")
    print("- MOVE")
    print("- TURN LEFT")
    print("- TURN RIGHT")
    print("- REPORT")
    print("- ADD OBSTACLE x y")
    print("- REMOVE OBSTACLE x y")
    print("- LIST OBSTACLES")
    print("- EXIT")

    while True:
        command = input("\nEnter command: ")
        should_continue = process_command(rover, command)
        if not should_continue:
            break


# Test Cases

def test_obstacle_class():
    """
    Test the Obstacle class for correct initialization and equality.
    """
    print("=== Testing Obstacle Class ===")
    obs1 = Obstacle(1, 2)
    obs2 = Obstacle(1, 2)
    obs3 = Obstacle(2, 3)

    assert obs1 == obs2, "Obstacles with same coordinates should be equal."
    assert obs1 != obs3, "Obstacles with different coordinates should not be equal."
    print("Obstacle Class tests passed.\n")


def test_obstacle_manager():
    """
    Test the ObstacleManager class for adding, removing, and checking obstacles.
    """
    print("=== Testing ObstacleManager Class ===")
    manager = ObstacleManager()

    # Add obstacles
    assert manager.add_obstacle(1, 1) == True, "Should successfully add obstacle at (1,1)."
    assert manager.add_obstacle(2, 2) == True, "Should successfully add obstacle at (2,2)."
    assert manager.add_obstacle(1, 1) == False, "Should not add duplicate obstacle at (1,1)."

    # Check obstacles
    assert manager.is_obstacle(1, 1) == True, "(1,1) should have an obstacle."
    assert manager.is_obstacle(3, 3) == False, "(3,3) should not have an obstacle."

    # Remove obstacles
    assert manager.remove_obstacle(1, 1) == True, "Should successfully remove obstacle at (1,1)."
    assert manager.remove_obstacle(1, 1) == False, "Should not remove non-existing obstacle at (1,1)."

    # List obstacles
    obstacles = manager.list_obstacles()
    assert len(obstacles) == 1 and obstacles[0].x == 2 and obstacles[0].y == 2, "Only obstacle at (2,2) should remain."

    print("ObstacleManager Class tests passed.\n")


def test_rover_with_obstacle_manager():
    """
    Test the Rover class with an ObstacleManager for correct movement and obstacle handling.
    """
    print("=== Testing Rover Class with ObstacleManager ===")
    manager = ObstacleManager()
    rover = Rover(obstacle_manager=manager)

    # Add obstacles
    rover.add_obstacle(0, 1)  # North of starting position
    rover.add_obstacle(1, 0)  # East of starting position

    # Attempt to move North into an obstacle
    rover.move()  # Should detect obstacle at (0,1)

    # Turn Right to face East and attempt to move into an obstacle
    rover.turn_right()
    rover.move()  # Should detect obstacle at (1,0)

    # Turn Right to face South and move South (no obstacle)
    rover.turn_right()
    rover.move()  # Should move to (0,-1)

    # Add obstacle at (0, -2) and attempt to move South
    rover.add_obstacle(0, -2)
    rover.move()  # Should detect obstacle at (0,-2)

    # Remove obstacle at (0, -2) and move South
    rover.remove_obstacle(0, -2)
    rover.move()  # Should move to (0,-2)

    # Final report
    rover.report()

    print("Rover Class with ObstacleManager tests passed.\n")


def test_command_processor_with_obstacle_manager():
    """
    Test the command processing with a sequence of commands involving obstacles.
    """
    print("=== Testing Command Processor with ObstacleManager ===")
    manager = ObstacleManager()
    rover = Rover(obstacle_manager=manager)

    commands = [
        "ADD OBSTACLE 2 2",
        "ADD OBSTACLE 3 3",
        "LIST OBSTACLES",
        "MOVE",          # North to (0,1)
        "MOVE",          # North to (0,2)
        "TURN RIGHT",    # East
        "MOVE",          # East to (1,2)
        "MOVE",          # East to (2,2) - obstacle
        "REPORT",
        "TURN LEFT",     # North
        "MOVE",          # North to (1,3)
        "ADD OBSTACLE 1 3",
        "MOVE",          # Attempt to move to (1,4) - no obstacle
        "TURN LEFT",     # West
        "MOVE",          # West to (0,3)
        "REPORT",
        "EXIT"
    ]

    expected_final_position = (0, 3)
    for command in commands:
        if command == 'EXIT':
            break
        process_command(rover, command)

    # Final state
    final_report = rover.report()
    expected_report = f"Rover is at (0, 3) facing West."
    assert final_report == expected_report, f"Expected '{expected_report}', got '{final_report}'"
    print("Command Processor with ObstacleManager tests passed.\n")


if __name__ == "__main__":
    # Run test cases
    test_obstacle_class()
    test_obstacle_manager()
    test_rover_with_obstacle_manager()
    test_command_processor_with_obstacle_manager()

    # Start the main application
    main()
