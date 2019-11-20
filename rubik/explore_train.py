# import csv

# moves = {
#             'F': 0,
#             "F'": 0,
#             'U': 0,
#             "U'": 0,
#             'L': 0,
#             "L'": 0,
#             'R': 0,
#             "R'": 0,
#             'D': 0,
#             "D'": 0,
#             'B': 0,
#             "B'": 0
#  }
# seen_states = set()
# with open('./train.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if row[0] not in seen_states:
#             seen_states.add(row[0])
#             moves[row[1]] += 1
# print(moves)

# from solve_random_cubes import random_cube
# import kociemba
# import random


# def convert_kociemba_to_cube(kociemba_string):
#     new_kociemba_string = ""
#     for i in range(0, len(kociemba_string)):
#         if kociemba_string[i] == ' ':
#             new_kociemba_string += ' '
#             continue
#         if kociemba_string[i] == '2':
#             new_kociemba_string += ' ' + new_kociemba_string[len(new_kociemba_string) - 1]
#             continue
#         new_kociemba_string += kociemba_string[i]
#     return new_kociemba_string
# for i in range(10000):
#     if i % 1000 == 0:
#         print(i)
#     cube = Cube()
#     for _ in range(100):
#         move = random.choice(MOVES) 
#         cube.move(move)
#     kociemba_sequence = kociemba.solve(str(cube))
#     kociemba_sequence = convert_kociemba_to_cube(kociemba_sequence)
#     for move in kociemba_sequence.split(' '):
#         cube.move(move)
#     if not cube.is_solved():
#         print('fail')


# def convert_cube_to_kociemba(flat_cube_str):
#     kociemba_letters = flat_cube_str.replace("O", "U").replace("Y", "L").replace("W", "F").replace("R", "D").replace("G", "R")
#     return kociemba_letters
# def convert_kociemba_to_cube(kociemba_string):
#     kociemba_string = kociemba_string.replace("'", "i")
#     new_kociemba_string = ""
#     for i in range(0, len(kociemba_string)):
#         if kociemba_string[i] == ' ':
#             new_kociemba_string += ' '
#             continue
#         if kociemba_string[i] == '2':
#             new_kociemba_string += ' ' + new_kociemba_string[len(new_kociemba_string) - 1]
#             continue
#         new_kociemba_string += kociemba_string[i]
#     return new_kociemba_string
# cube_str = convert_cube_to_kociemba(cube.flat_str())
# print(cube_str)
# kociemba_string = kociemba.solve(cube_str)

# cube_str = convert_kociemba_to_cube(kociemba_string)

# # print(cube)
# # cube.sequence(cube_str)

# # print(cube_str)
# # print(cube)

from cube import Cube
from termcolor import colored
import numpy as np

new_cube = Cube()


print_cube_in_grid(new_cube)