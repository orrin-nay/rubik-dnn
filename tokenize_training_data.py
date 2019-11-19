import csv
import numpy as np

moves = {
 'X':0,
 'Bi':1,
 'Di':2,
 'Fi':3,
 'R':4,
 'Si':5,
 'Z':6,
 'Ui':7,
 'Ri':8,
 'Xi':9,
 'D':10,
 'Li':11,
 'B':12,
 'Zi':13,
 'U':14,
 'E':15,
 'L':16,
 'F':17,
 'Ei':18,
 'S':19
 }
faces = {
 'B': 0,
 'O': 1, 
 'G': 2, 
 'R': 3, 
 'Y': 4, 
 'W': 5 
 }

Xs = []
Ys = []
save = 0
with open('./rubik/train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        if line_count % 1000000 == 0:
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
        current_move = np.zeros((20), dtype=np.bool)
        move_index = moves[row[1]]
        current_move[move_index] = 1

        Xs.append(current_faces)
        Ys.append(current_move)
Xs = np.array(Xs, dtype=np.bool)
Ys = np.array(Ys, dtype=np.bool)

np.save('train/Xs' + str(save) + '.npy', Xs)
np.save('train/Ys' + str(save) + '.npy', Ys)