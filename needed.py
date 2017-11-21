
from greedyRobot import Robot

# Take input from user
print("Please enter your coordinates point in robot X, robot Y, treasure X, trease Y:")
rx, ry, tx, ty = map(int, input().split())

print("rx, ry, tx, ty: ", rx, ry, tx, ty)

# Create robot instance with params
robot = Robot(rx, ry, tx, ty)
robot.solve()
robot.solution()
