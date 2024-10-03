#Should the snake move in 4 directions: up, down, left, and right?
#Is it guaranteed that food appears in sequence (i.e., the snake must eat food[i] before food[i+1] appears)?
#What should happen if the snake eats food and reaches the screen's boundaries at the same time? Is the game over, or does it extend without issue?
#Should the initial position of the snake's head always start at (0, 0)?

# The Snake:

# It starts at the top-left corner (0, 0) with a length of 1.
# It moves around the grid based on user input (like "U" for up, "D" for down, "L" for left, and "R" for right).
# The snake grows when it eats food.


# Algorithim
#Initialize the Game:

# Keep track of the snake’s body positions using a deque (double-ended queue) so that you can easily add new positions (snake's growth) and remove old positions (when the snake moves).
# Track the current index of the food to know which piece of food the snake should eat next.
# Store the snake’s head position and check for collisions after each move.
# Handle Movement:

# Depending on the input direction, update the snake’s head position.
# If the new position hits a wall or the snake’s body, return -1 (game over).
# If the snake reaches the food, grow the snake and increase the score.
# Otherwise, move the snake by updating its body positions.
# Game Over Check:

# After each move, check if the snake hits a wall or its body.

from collections import deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        # Store the grid dimensions
        self.width = width
        self.height = height
        
        # Store the food positions
        self.food = food
        self.food_index = 0  # To keep track of the next food to eat
        
        # Initialize the snake's position. We use deque for efficient front and back operations.
        self.snake = deque()
        self.snake.append((0, 0))  # Snake starts at the top-left corner
        
        # Set to store positions occupied by the snake for quick collision checks
        self.occupied = set()
        self.occupied.add((0, 0))  # Initially, only (0, 0) is occupied
        
        # Define direction vectors for movement
        # 'U' = Up, 'D' = Down, 'L' = Left, 'R' = Right
        self.directions = {
            'U': (-1, 0),  # Move up decreases the row index
            'D': (1, 0),   # Move down increases the row index
            'L': (0, -1),  # Move left decreases the column index
            'R': (0, 1)    # Move right increases the column index
        }
        
        # Initialize the game score
        self.score = 0
        
        # Flag to indicate if the game is over
        self.game_over = False
        

    def move(self, direction):
        """
        Move the snake in the given direction.

        :param direction: str - Direction to move ('U' for up, 'D' for down, 'L' for left, 'R' for right).
        :return: int - The game's score after the move. If the game is over, returns -1.
        """
        # If the game is already over, no further moves are allowed
        if self.game_over:
            print("Game is over. No more moves allowed.")
            return -1
        
        # Get the current head position of the snake
        current_head = self.snake[0]
        
        # Get the movement vector based on the direction
        if direction not in self.directions:
            print("Invalid direction! Use 'U', 'D', 'L', or 'R'.")
            return -1  # Invalid direction input
        
        move_row, move_col = self.directions[direction]
        
        # Calculate the new head position
        new_head = (current_head[0] + move_row, current_head[1] + move_col)
        print("Moving {} to {}.".format(direction, new_head))
        
        # Check if the new head position is outside the grid (wall collision)
        if not (0 <= new_head[0] < self.height) or not (0 <= new_head[1] < self.width):
            print("Hit the wall at {}. Game over!".format(new_head))
            self.game_over = True
            return -1
        
        # Check if the new head position is on the snake's body (self-collision)
        # Remove the tail position temporarily because the snake moves forward
        tail = self.snake.pop()  # Remove the tail
        self.occupied.remove(tail)  # Remove the tail from occupied positions
        
        if new_head in self.occupied:
            print("Ran into itself at {}. Game over!".format(new_head))
            self.game_over = True
            return -1
        
        # Add the tail back since the snake hasn't grown
        self.snake.append(tail)
        self.occupied.add(tail)
        
        # Check if there's food at the new head position
        if (self.food_index < len(self.food) and 
            new_head == tuple(self.food[self.food_index])):
            print("Ate food at {}!".format(new_head))
            self.score += 1  # Increase the score
            self.food_index += 1  # Move to the next food item
            # Do not remove the tail, as the snake grows
        else:
            # Move the snake forward by removing the tail
            removed_tail = self.snake.pop()
            self.occupied.remove(removed_tail)
            print("Moved forward. Removed tail at {}.".format(removed_tail))
        
        # Add the new head to the snake
        self.snake.appendleft(new_head)
        self.occupied.add(new_head)
        print("New head at {}. Current score: {}.".format(new_head, self.score))
        
        # Return the current score
        return self.score

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

# Create a game instance
snakeGame = SnakeGame(3, 3, [[1,2], [0,1]])

# Move right, expecting the score to remain 0
print(snakeGame.move("R"))  # Output: 0

# Move down, expecting the score to remain 0
print(snakeGame.move("D"))  # Output: 0

# Move right and eat food, expecting the score to become 1
print(snakeGame.move("R"))  # Output: 1

# Move up and hit the wall, expecting game over (-1)
print(snakeGame.move("U"))  # Output: -1
