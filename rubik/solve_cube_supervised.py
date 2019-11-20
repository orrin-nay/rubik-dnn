import numpy as np
from solve_random_cubes import random_cube
from supervised_model import make_model
from tokenize_utils import tokenize_cube_state, detokenize_move
import random
from keras.models import load_model

model = make_model()
model.load_weights('../supervised_model.h5')

cube_shuffles = 7
cube = random_cube(cube_shuffles)


MOVES = [
 'U',
 'R', 
 'F', 
 'D', 
 'L', 
 'B', 
 "B'",
 "U'",
 "R'", 
 "F'", 
 "D'", 
 "L'" ]

number_of_moves = 0

print(cube)

def print_cube_in_grid(cube):
    new_state = np.array(cube.state)
    cube_string =("    %s%s%s" % tuple(new_state[0:3]))
    cube_string +=("\n    %s%s%s" % tuple(new_state[3:6]))
    cube_string +=("\n    %s%s%s" % tuple(new_state[6:9]))
    cube_string +=("\n%s%s%s %s%s%s %s%s%s %s%s%s" %
     tuple(np.concatenate((new_state[36:39], new_state[18:21], new_state[9:12], new_state[45:48]))))
    cube_string +=("\n%s%s%s %s%s%s %s%s%s %s%s%s" %
     tuple(np.concatenate((new_state[39:42], new_state[21:24], new_state[12:15], new_state[48:51]))))
    cube_string +=("\n%s%s%s %s%s%s %s%s%s %s%s%s" %
     tuple(np.concatenate((new_state[42:45], new_state[24:27], new_state[15:18], new_state[51:]))))
    cube_string +=("\n    %s%s%s" % tuple(new_state[27:30]))
    cube_string +=("\n    %s%s%s" % tuple(new_state[30:33]))
    cube_string +=("\n    %s%s%s" % tuple(new_state[33:36]))
    cube_string = cube_string.replace("U", colored("U", 'yellow')).replace("B", colored("B", 'blue')).replace("R", colored("R", 'red')).replace("U", colored("U", 'green')).replace("D", colored("D", 'magenta')).replace("L", colored("L", 'cyan'))
    print(cube_string)

previous_states = set()
while not cube.is_solved():
    number_of_moves += 1
    current_state = tokenize_cube_state(cube)
    next_move = model.predict(np.array([current_state]))
    move = detokenize_move(next_move[0])
    cube_state_hash = str(cube) + move
    if cube_state_hash in previous_states:
        for move_try in MOVES:
            cube_state_hash = str(cube) + move_try
            if cube_state_hash not in previous_states:
                move = move_try
                break
    if cube_state_hash in previous_states:
        number_of_moves = 0
        cube = random_cube(cube_shuffles)
        previous_states = set()
        print('stuck')
        print('----------------------------------')
        print(cube)

    previous_states.add(cube_state_hash)
    print_cube_in_grid(cube)
    print(move)
    cube.move(move)
print(number_of_moves)
print(cube)
print(move)
