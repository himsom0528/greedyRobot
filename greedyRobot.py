class Robot:
  
    # Constructor
    def __init__(self, rX = 0, rY = 0, tX = 0, tY = 0):
        # Set attributes to params values
        self._rx = rX
        self._ry = rY
        self._tx = tX
        self._ty = tY
        
        # Set helper attributes 
        self.minSteps = -1     # -1 because it's not set yet
        self.paths = []         # Empty list that will contain the shortest paths

    def solve(self):
        # Call path method with the current positions as the starting positions, 
        # number of steps so far = 0
        # Path so far is empty
        self.path(self._rx, self._ry, 0, [])

    def path(self, coordinateX, coordinateY, steps, path):
        # Exceeded the minimum solution so it won't be considered in the solutions
        if self.minSteps > 0 and self.minSteps < steps:
            return

        # Reached target
        if coordinateX == self._tx and coordinateY == self._ty:
            # If starting position and target position are the same return (Do nothing)
            if len(path) == 0:
              return
            
            # Concatenate path: ['N', 'E', 'N', 'N'] --> 'NENN' to be added to paths list
            pathString = ''.join(path)
            

            # First path found
            if self.minSteps < 0:
                self.minSteps = steps
                self.paths.append(pathString)
            # Found path is as short as the first path found
            elif self.minSteps == steps:
                # Make sure path is not duplicated 
                if pathString not in self.paths:
                    # Add path to paths list if it has not been added yet
                    self.paths.append(pathString)
            # Found path is shorter than shortest path found, so far
            elif self.minSteps > steps:
                # Update minSteps value
                self.minSteps = steps
                # Set paths list to new path only since all other paths are longer
                self.paths = [pathString]
        # Goal has not been reached yet
        else:
            # Need to go EAST to reach target
            if coordinateX < self._tx:
                self.path(coordinateX + 1, coordinateY, steps + 1, list(path) + ['E'])
            
            # Need to go WEST to reach target
            if coordinateX > self._tx:
                self.path(coordinateX - 1, coordinateY, steps + 1, list(path) + ['W'])

            # Need to go NORTH to reach target
            if coordinateY < self._ty:
                self.path(coordinateX, coordinateY + 1, steps + 1, list(path) + ['N'])
            
            # Need to go SOUTH to reach target
            if coordinateY > self._ty:
                self.path(coordinateX, coordinateY - 1, steps + 1, list(path) + ['S'])

    # Prints solution
    def solution(self):
        for path in self.paths:
            print(path)
        print("Number of paths: ", len(self.paths))
