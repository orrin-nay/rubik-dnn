import numpy as np

faces = {
 'B': 0,
 'O': 1, 
 'G': 2, 
 'R': 3, 
 'Y': 4, 
 'W': 5 
 }
moves_to_tokens = {
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
tokens_to_moves = {
 0:'X',
 1:'Bi',
 2:'Di',
 3:'Fi',
 4:'R',
 5:'Si',
 6:'Z',
 7:'Ui',
 8:'Ri',
 9:'Xi',
 10:'D',
 11:'Li',
 12:'B',
 13:'Zi',
 14:'U',
 15:'E',
 16:'L',
 17:'F',
 18:'Ei',
 19:'S'
 }

def tokenize_cube_state(cube):
    cube_state = str(cube).replace("\n","").replace(" ", "")
    state_faces = []
    for color in cube_state:
        current_face = np.zeros((6), dtype=np.bool)
        color_index = faces[color]
        current_face[color_index] = 1
        state_faces.append(current_face)
    return np.array(state_faces)
def detokenize_move(move_prediction):
    move_token = np.argmax(move_prediction)
    move = tokens_to_moves[move_token]
    return move