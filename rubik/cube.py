
class Cube(object):
    def __init__(self):
        self.state = ['U','U','U','U','U','U','U','U','U','R','R','R','R','R','R','R','R','R','F','F','F','F','F','F','F','F','F','D','D','D','D','D','D','D','D','D','L','L','L','L','L','L','L','L','L','B','B','B','B','B','B','B','B','B']
        self.solved = ''.join(self.state)
        self.name_to_index = {
            'U1': 0, 
            'U2': 1, 
            'U3': 2, 
            'U4': 3, 
            'U5': 4, 
            'U6': 5, 
            'U7': 6, 
            'U8': 7, 
            'U9': 8, 
            'R1': 9, 
            'R2': 10, 
            'R3': 11, 
            'R4': 12, 
            'R5': 13, 
            'R6': 14, 
            'R7': 15, 
            'R8': 16, 
            'R9': 17, 
            'F1': 18, 
            'F2': 19, 
            'F3': 20, 
            'F4': 21, 
            'F5': 22, 
            'F6': 23, 
            'F7': 24, 
            'F8': 25, 
            'F9': 26, 
            'D1': 27, 
            'D2': 28, 
            'D3': 29, 
            'D4': 30, 
            'D5': 31, 
            'D6': 32, 
            'D7': 33, 
            'D8': 34, 
            'D9': 35, 
            'L1': 36, 
            'L2': 37, 
            'L3': 38, 
            'L4': 39, 
            'L5': 40, 
            'L6': 41, 
            'L7': 42, 
            'L8': 43, 
            'L9': 44, 
            'B1': 45, 
            'B2': 46, 
            'B3': 47, 
            'B4': 48, 
            'B5': 49, 
            'B6': 50, 
            'B7': 51, 
            'B8': 52, 
            'B9': 53
        }
    def face_rotation(self, start):
        state_copy = self.state.copy()
        self.state[start] = state_copy[start + 6]
        self.state[start + 1] = state_copy[start + 3]
        self.state[start + 2] = state_copy[start]
        self.state[start + 3] = state_copy[start + 7]
        self.state[start + 5] = state_copy[start + 1]
        self.state[start + 6] = state_copy[start + 8]
        self.state[start + 7] = state_copy[start + 5]
        self.state[start + 8] = state_copy[start + 2]
    def rotate_three(self, f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11):
        state_copy = self.state.copy()
        self.state[f_0] = state_copy[f_9]
        self.state[f_1] = state_copy[f_10]
        self.state[f_2] = state_copy[f_11]
        self.state[f_3] = state_copy[f_0]
        self.state[f_4] = state_copy[f_1]
        self.state[f_5] = state_copy[f_2]
        self.state[f_6] = state_copy[f_3]
        self.state[f_7] = state_copy[f_4]
        self.state[f_8] = state_copy[f_5]
        self.state[f_9] = state_copy[f_6]
        self.state[f_10] = state_copy[f_7]
        self.state[f_11] = state_copy[f_8]

    def rotate_front(self):
        self.face_rotation(self.name_to_index['F1'])
        self.rotate_three(self.name_to_index['U7'],
                        self.name_to_index['U8'],
                        self.name_to_index['U9'],
                        self.name_to_index['R1'],
                        self.name_to_index['R4'],
                        self.name_to_index['R7'],
                        self.name_to_index['D3'],
                        self.name_to_index['D2'],
                        self.name_to_index['D1'],
                        self.name_to_index['L9'],
                        self.name_to_index['L6'],
                        self.name_to_index['L3']
                        )
    def rotate_reverse_front(self):
        self.rotate_front()
        self.rotate_front()
        self.rotate_front()

    def rotate_up(self):
        self.face_rotation(self.name_to_index['U1'])
        self.rotate_three(self.name_to_index['F3'],
                        self.name_to_index['F2'],
                        self.name_to_index['F1'],
                        self.name_to_index['L3'],
                        self.name_to_index['L2'],
                        self.name_to_index['L1'],
                        self.name_to_index['B3'],
                        self.name_to_index['B2'],
                        self.name_to_index['B1'],
                        self.name_to_index['R3'],
                        self.name_to_index['R2'],
                        self.name_to_index['R1']
                        )
    def rotate_reverse_up(self):
        self.rotate_up()
        self.rotate_up()
        self.rotate_up()

    def rotate_left(self):
        self.face_rotation(self.name_to_index['L1'])
        self.rotate_three(self.name_to_index['U1'],
                        self.name_to_index['U4'],
                        self.name_to_index['U7'],
                        self.name_to_index['F1'],
                        self.name_to_index['F4'],
                        self.name_to_index['F7'],
                        self.name_to_index['D1'],
                        self.name_to_index['D4'],
                        self.name_to_index['D7'],
                        self.name_to_index['B9'],
                        self.name_to_index['B6'],
                        self.name_to_index['B3']
                        )
    def rotate_reverse_left(self):
        self.rotate_left()
        self.rotate_left()
        self.rotate_left()

    def rotate_right(self):
        self.face_rotation(self.name_to_index['R1'])
        self.rotate_three(self.name_to_index['F9'],
                        self.name_to_index['F6'],
                        self.name_to_index['F3'],
                        self.name_to_index['U9'],
                        self.name_to_index['U6'],
                        self.name_to_index['U3'],
                        self.name_to_index['B1'],
                        self.name_to_index['B4'],
                        self.name_to_index['B7'],
                        self.name_to_index['D9'],
                        self.name_to_index['D6'],
                        self.name_to_index['D3']
                        )
    def rotate_reverse_right(self):
        self.rotate_right()
        self.rotate_right()
        self.rotate_right()

    def rotate_down(self):
        self.face_rotation(self.name_to_index['D1'])
        self.rotate_three(self.name_to_index['F7'],
                        self.name_to_index['F8'],
                        self.name_to_index['F9'],
                        self.name_to_index['R7'],
                        self.name_to_index['R8'],
                        self.name_to_index['R9'],
                        self.name_to_index['B7'],
                        self.name_to_index['B8'],
                        self.name_to_index['B9'],
                        self.name_to_index['L7'],
                        self.name_to_index['L8'],
                        self.name_to_index['L9']
                        )
    def rotate_reverse_down(self):
        self.rotate_down()
        self.rotate_down()
        self.rotate_down()

    def rotate_back(self):
        self.face_rotation(self.name_to_index['B1'])
        self.rotate_three(self.name_to_index['R9'],
                        self.name_to_index['R6'],
                        self.name_to_index['R3'],
                        self.name_to_index['U3'],
                        self.name_to_index['U2'],
                        self.name_to_index['U1'],
                        self.name_to_index['L1'],
                        self.name_to_index['L4'],
                        self.name_to_index['L7'],
                        self.name_to_index['D7'],
                        self.name_to_index['D8'],
                        self.name_to_index['D9']
                        )
    def rotate_reverse_back(self):
        self.rotate_back()
        self.rotate_back()
        self.rotate_back()

    def move(self, move):
        moves = {
            'F': self.rotate_front,
            "F'": self.rotate_reverse_front,
            'U': self.rotate_up,
            "U'": self.rotate_reverse_up,
            'L': self.rotate_left,
            "L'": self.rotate_reverse_left,
            'R': self.rotate_right,
            "R'": self.rotate_reverse_right,
            'D': self.rotate_down,
            "D'": self.rotate_reverse_down,
            'B': self.rotate_back,
            "B'": self.rotate_reverse_back
        }
        moves[move]()
            # case 'U':  monthString = "January";
            #          break;
            # case "U'":  monthString = "February";
            #          break;
            # case 'R':  monthString = "March";
            #          break;
            # case "R'":  monthString = "April";
            #          break;
            # case 'F':  self.rotate_front();
            #          break;
            # case "F'":  monthString = "April";
            #          break;
            # case 'D':  monthString = "March";
            #          break;
            # case "D'":  monthString = "April";
            #          break;
            # case 'L':  monthString = "March";
            #          break;
            # case "L'":  monthString = "April";
            #          break;
            # case 'B':  monthString = "March";
            #          break;
            # case "B'":  monthString = "April";
            #          break;
    def __str__(self):
        return "".join(self.state)
    def is_solved(self):
        if "".join(self.state) == self.solved:
            return True
        return False