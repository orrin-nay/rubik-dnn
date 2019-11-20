import csv
import numpy as np

faces = {
 'U': 0,
 'R': 1, 
 'F': 2, 
 'D': 3, 
 'L': 4, 
 'B': 5 
 }
moves = {
            'F': 0,
            "F'": 1,
            'U': 2,
            "U'": 3,
            'L': 4,
            "L'": 5,
            'R': 6,
            "R'": 7,
            'D': 8,
            "D'": 9,
            'B': 10,
            "B'": 11
 }

Xs = []
Ys = []
save = 0
with open('./rubik/train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        if line_count % 500000 == 0:
            Xs = np.array(Xs, dtype=np.bool)
            Ys = np.array(Ys, dtype=np.bool)

            np.save('train/Xs' + str(save) + '.npy', Xs)
            np.save('train/Ys' + str(save) + '.npy', Ys)

            Xs = []
            Ys = []
            print(line_count)
            save += 1
        current_faces = []
        for color in row[0]:
            current_face = np.zeros((6), dtype=np.bool)
            color_index = faces[color]
            current_face[color_index] = 1
            current_faces.append(current_face)
        current_move = np.zeros((12), dtype=np.bool)
        move_index = moves[row[1]]
        current_move[move_index] = 1

        Xs.append(current_faces)
        Ys.append(current_move)
Xs = np.array(Xs, dtype=np.bool)
Ys = np.array(Ys, dtype=np.bool)

np.save('train/Xs' + str(save) + '.npy', Xs)
np.save('train/Ys' + str(save) + '.npy', Ys)