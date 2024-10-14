# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):

    # Calculate the maximum inches that can be covered by big bricks without exceeding the goal
    max_big_bricks = min(big, goal // 5)

    # Calculate the remaining inches to be covered after using big bricks
    remaining_goal = goal - (max_big_bricks * 5)

    # If we have enough small bricks to cover the remaining inches, return True
    return small >= remaining_goal
