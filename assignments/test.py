# import os
# stream = os.popen('py ./main.py')
# output = stream.read()

# print(output)

import CPSC217S23A3Board as game

b = [[0, 0, 1],
 [0, 1, 0],
 [1, 0, 0]]

w = game.win_in_diagonal_forward_slash(b, 1)

print(w)