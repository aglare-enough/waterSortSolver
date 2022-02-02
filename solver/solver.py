from model.Cups import Cups


class Solver:
    res = []

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
            for j in range(cups.cupNum):
                if cups.cups[i].can_pour(cups.cups[j]):
                    newcups = cups.duplicate()
                    newcups.cups[i].pour_into(newcups.cups[j])

                    if newcups.cups[j].can_pour(newcups.cups[i]):
                        newcups.cups[j].pour_into(newcups.cups[i])
                        continue

                    cls.res.append((i, j))
                    print("add " + str(i) + "," + str(j))
                    if Solver.sort(newcups,depth+1):
                        return True
                    cls.res.pop()
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
