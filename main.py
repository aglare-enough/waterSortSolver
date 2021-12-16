import Cups
test_waters = [
    [],
    [],
    [1, 2, 3, 4],
    [5, 6, 5, 5],
    [3, 7, 3, 4],
    [6, 5, 1, 7],
    [3, 2, 1, 1],
    [2, 4, 4, 6],
    [6, 7, 7, 2]
]

if __name__ == '__main__':
    cups = Cups.Cups(test_waters)
    cups.sort()
    cups.output_res()
    cups.output_ans()
