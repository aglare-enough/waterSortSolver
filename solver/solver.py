from model.Cups import Cups


class Solver:
    res = []

    def __init__(self):
        pass

    @classmethod
    def sort(cls, cups: Cups):
        if cups.is_success():
            print('solve success')
            return True
        if not cups.has_effective_action():
            return False
        for i in range(cups.cupNum):
            # j = i + 1
            for j in range(cups.cupNum):
                if cups.cups[i].can_pour(cups.cups[j]):
                    newcups = cups.duplicate()
                    newcups.cups[i].pour_into(newcups.cups[j])
                    # cls.res.append((i, j))
                    print("add " + str(i) + "," + str(j))
                    if Solver.sort(newcups):
                        return True
                    cls.res.pop()
                    # print("pop " + str(i) + "," + str(j))
                j += 1
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
