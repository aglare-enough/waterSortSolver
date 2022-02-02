from model import Cups
from solver.solver import Solver

test_waters = [
    [1,2,3,4],
    [5,4,6,1],
    [1, 7, 2, 8],
    [3, 8, 8, 5],
    [7, 9, 9, 3],
    [1, 8, 6, 2],
    [2, 9, 4, 5],
    [7, 6, 9, 6],
    [3, 5, 7, 4],
    [],
    []
    # [1, 2, 3, 3],
    # [3, 3, 2, 1],
    # [2, 2, 1, 1],
]

if __name__ == '__main__':
    cups = Cups.Cups(test_waters)
    Solver.sort(cups,0)
    Solver.output(test_waters)
