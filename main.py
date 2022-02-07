from model import Cups
from solver.solver import Solver

# test data
# 把试管抽象为一个特殊的栈(直接用数组来代替，因为数组就有append pop方法，将数组的尾部作为栈顶即试管顶部)
# 将颜色抽象为数字
test_waters = [
    [1, 2, 3, 4],
    [5, 4, 6, 1],
    [1, 7, 2, 8],
    [3, 8, 8, 5],
    [7, 9, 9, 3],
    [1, 8, 6, 2],
    [2, 9, 4, 5],
    [7, 6, 9, 6],
    [3, 5, 7, 4],
    [],
    []
]

if __name__ == '__main__':
    # 创建cups模型对象实例
    cups = Cups.Cups(test_waters)

    # 进行求解
    Solver.sort(cups)

    # 输出求解答案
    Solver.output(test_waters)
