class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        #Robot's starting position: The robot starts at position (0, 0). Think of this as the "home base" at the center of a huge map.
        x,y = 0, 0
        #Directions: The robot can face in 4 directions: North (+Y, which means going up). East (+X, which means going right). South (-Y, which means going down). West (-X, which means going left).

        directions = [[0,1], [1,0], [0,-1], [-1,0]] #N,E,S,W. [0, 1] means go north (increase Y). [1, 0] means go east (increase X). [0, -1] means go south (decrease Y). [-1, 0] means go west (decrease X)
        d = 0 #Direction tracking: We use d = 0 to start with the robot facing north. So: d = 0 means north, d = 1 means east, d = 2 means south, d = 3 means west.
        result = 0

        #metnniond this later in a interveiw to deal wiht obstaces
        #Obstacles: The robot can run into obstacles, but it shouldn’t walk through them. We turn the list of obstacles into a set of tuples because checking if something is in a set is super fast. This line converts each obstacle into a tuple (because lists can’t be added to sets) and stores them in a set.
        obstacles = {tuple(o) for o in obstacles} #set comprehsion

        for command in commands:
            #The % 4 part ensures that when we reach 4 (or below 0), we wrap around. Like, if you’re facing west and turn right, you should go back to facing north.
            if command == -1:
                d = (d +1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                #This grabs the direction vector (how much to change x and y).
                dx, dy = directions[d]
                #For every step (up to k steps), we check if the next position (x + dx, y + dy) is an obstacle:
                for _ in range(command):
                    #If it is an obstacle, the robot stops moving in that direction.
                    if (x+dx, y + dy) in obstacles:
                        # Stop if there's an obstacle
                        break
                    # Update position if no obstacle
                    x, y = x + dx, y + 
            #keep track of the maximum distance the robot reaches.
            result = max(result, x**2 + y**2)
        return result

commands = [4, -1, 3]
obstacles = []
print(robotSim(commands, obstacles))  # Output: 25

commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(robotSim(commands, obstacles))  # Output: 65
        
