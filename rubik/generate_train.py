from solve_random_cubes import run_case
import solve
if __name__ == '__main__':
    from multiprocessing import Pool
    import itertools
    import csv
    solve.DEBUG = False
    p = Pool(12)
    results = p.map(run_case, range(40000))
    seen_positions = set()
    with open('train.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        result_set_count = 0
        for  r in results:
            result_set_count += 1
            if result_set_count % 1000 == 0:
                print(result_set_count)
            for data in r:
                if data[0] not in seen_positions:
                    wr.writerow(data)
                    seen_positions.add(data[0])

    print(len(results))