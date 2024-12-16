class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define the possible directions for movement (up, down, left, right)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Determine the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Initialize a counter to keep track of the number of islands
        islands = 0

        # Depth-first search (DFS) function to traverse and mark the island
        def dfs(r, c):
            # Check if the current cell is out of bounds or water ('0')
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            # Mark the current cell as visited by setting it to '0'
            grid[r][c] = "0"

            # Explore all neighboring cells in the specified directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Iterate through each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If the cell is land ('1'), it means we've found an island
                if grid[r][c] == "1":
                    # Perform a DFS to mark the entire island as visited
                    dfs(r, c)
                    # Increment the island count
                    islands += 1

        # Return the total number of islands found
        return islands
