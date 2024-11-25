


def kernel(terrain, directory):
    # This is the initial coordinates of the lightbot on the matrix
    x = 8
    y = 0

    # Each direction will modify x and y differently
    dx = [0, -1, 0, 1]  # x stays the same for left/right, but changes for up/down
    dy = [1, 0, -1, 0]  # y stays the same for up/down, but changes for left/right

    direction = 0  # 0: right; 1: upwards; 2: leftwards; 3: downwards
    for i in directory:
        if i == "^":
            # Calculate new coordinates based on direction
            new_x = x + dx[direction]
            new_y = y + dy[direction]

            # Ensure the robot stays within the matrix bounds
            if 0 <= new_x < len(terrain) and 0 <= new_y < len(terrain[0]):
                x, y = new_x, new_y

        #elif i == "@":
        #    # Toggle the current position's value
        #    terrain[x][y] = 1 if terrain[x][y] == 0 else 0

        elif i == "<":
            # Turn left
            direction = (direction + 1) % 4

        elif i == ">":
            # Turn right
            direction = (direction - 1) % 4

        # I decided to express the existence of the light with +- 0.5 systems, because in the future +1 system
        # will describe the 3D level of the lightbot.
        # Also for now lightbot is able to turn on/off the light of every square, which I will fix in the following homework
        elif i == "@":
            if terrain[x][y] % 1 == 0:
                terrain[x][y] += 0.5
            elif terrain[x][y] % 1 != 0:
                terrain[x][y] += 0.5

    # the final matrix to see the result
    for row in terrain:
        print(row)  # The results is supposed resemble 7
    return matrix


answer1 = "^^^^^@<^@^@^@^@^@^@^@^@<^@^@^@^@<^@^^^^<^^^@^^@>^^^<^" # This is the answer to generate '7'
answer2 = "^^>^<^@^" # This answer is this week's task
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


kernel(matrix, answer2)


from vpython import *

terrain = []

for x in range(8):
    for y in range(8):
        square = box(pos = vector(x, y, 0), size = vector(1, 1, 1), color = color.blue)
        terrain.append(square)