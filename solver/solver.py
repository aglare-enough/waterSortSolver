from model.Cups import Cups


class Solver:
    res = []

    #value为1则lock 否则 unlock
    hashlock = {}

    def __init__(self):
        pass

    @classmethod
    def sort(cls, cups: Cups,depth):
        if cups.is_success():
            print('solve success')
            return True
        if not cups.has_effective_action():
            return False
        for i in range(cups.cupNum):
            # j = i + 1
            for j in range(cups.cupNum):
                if cls.hashlock.get((i, j)) == 1:
                    continue
                if cups.cups[i].can_pour(cups.cups[j]):
                    newcups = cups.duplicate()
                    newcups.cups[i].pour_into(newcups.cups[j])
                    cls.res.append((i, j))

                    # 解锁操作
                    for m in range(cups.cupNum):
                        cls.hashlock[(m, i)] = 0
                        cls.hashlock[(i, m)] = 0
                        cls.hashlock[(m, j)] = 0
                        cls.hashlock[(j, m)] = 0

                    # 上锁操作
                    cls.hashlock[(j, i)] = 1

                    print("add " + str(i) + "," + str(j))
                    if Solver.sort(newcups,depth+1):
                        return True
                    cls.res.pop()
                    # print("pop " + str(i) + "," + str(j))
        return False

    @classmethod
    def output(cls, data):
        cups = Cups(data)
        print(cls.res)
        print('--------------------------------')
        print(data)
        print('--------------------------------')
        for act in cls.res:
            cups.cups[act[0]].pour_into(cups.cups[act[1]])
            cups.output_res()
            print('--------------------------------')
