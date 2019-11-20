from cube import Cube
import kociemba
import random
MOVES = ["F", "U", "L", "R", "D", "B"]


def convert_kociemba_to_cube(kociemba_string):
    new_kociemba_string = ""
    for i in range(0, len(kociemba_string)):
        if kociemba_string[i] == ' ':
            new_kociemba_string += ' '
            continue
        if kociemba_string[i] == '2':
            new_kociemba_string += ' ' + new_kociemba_string[len(new_kociemba_string) - 1]
            continue
        new_kociemba_string += kociemba_string[i]
    return new_kociemba_string

def random_cube(shuffle_count=30):
    """
    :return: A new scrambled Cube
    """
    scramble_moves = " ".join(random.choice(MOVES) )
    a = Cube()
    for _ in range(shuffle_count):
        move = random.choice(MOVES)
        a.move(move)
    return a

def run_case(args):
    cube = random_cube()

    if args % 10000 == 0:
        print(args)

    training_data = []

    kociemba_sequence = kociemba.solve(str(cube))
    kociemba_sequence = convert_kociemba_to_cube(kociemba_sequence)
    for move in kociemba_sequence.split(' '):
        training_data.append([str(cube), move])
        cube.move(move)
    return training_data

if __name__ == '__main__':
    from multiprocessing import Pool
    import itertools
    import csv
    p = Pool(12)
    results = p.map(run_case, range(100000))
    seen_positions = set()
    with open('train.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        result_set_count = 0
        for  r in results:
            result_set_count += 1
            if result_set_count % 10000 == 0:
                print(result_set_count)
            for data in r:
                if data[0] not in seen_positions:
                    wr.writerow(data)
                    seen_positions.add(data[0])

    print(len(results))