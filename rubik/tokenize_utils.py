import numpy as np

faces = {
 'U': 0,
 'R': 1, 
 'F': 2, 
 'D': 3, 
 'L': 4, 
 'B': 5 
 }
moves_to_tokens = {
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
tokens_to_moves = {
            0: 'F',
            1: "F'",
            2: 'U',
            3: "U'",
            4: 'L',
            5: "L'",
            6: 'R',
            7: "R'",
            8: 'D',
            9: "D'",
            10: 'B',
            11: "B'"
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