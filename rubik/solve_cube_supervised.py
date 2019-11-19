import numpy as np
from solve_random_cubes import random_cube
from supervised_model import make_model
from tokenize_utils import tokenize_cube_state, detokenize_move
import random
from keras.models import load_model

model = make_model()
model.load_weights('../supervised_model.h5')
cube = random_cube()


MOVES = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]

number_of_moves = 0
last_move = ''
two_moves_ago = ''

print(cube)

while not cube.is_solved() and number_of_moves < 1000000:
    number_of_moves += 1
    if number_of_moves % 100 == 0:
        print(number_of_moves)
        print(cube)
    current_state = tokenize_cube_state(cube)
    next_move = model.predict(np.array([current_state]))
    move = detokenize_move(next_move[0])
    if move == two_moves_ago and move == last_move:
        move = random.choice(MOVES)
    two_moves_ago = last_move
    last_move = move

    cube.sequence(move)
print(number_of_moves)
