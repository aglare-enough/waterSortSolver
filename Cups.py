from Water import Water
from copy import deepcopy


class Cup:
    def __init__(self, waters):
        self.waterTotalNum = len(waters)
        self.MaxWaterNums = 4
        self.waters = []
        count = 0
        last = 0
        for water in waters:
            if last == water or last == 0:
                count += 1
            else:
                if count > 4:
                    print("cup init error,param error")
                    exit()
                w = Water(count, last)
                self.waters.append(w)
                count = 1
            last = water
        if count != 0:
            w = Water(count, last)
            self.waters.append(w)

    def top(self):
        if len(self.waters) > 0:
            return self.waters[-1]
        return False

    def pour_into(self, to_cup):
        if not self.can_pour(to_cup):
            return False
        origin_water = self.waters.pop()
        out_water = origin_water.out(self.MaxWaterNums - to_cup.waterTotalNum)
        if origin_water.num != 0:
            self.waters.append(origin_water)
        to_cup.waterTotalNum += out_water.num
        if to_cup.top():
            to_cup.top().num += out_water.num
        return True

    # whether or cannot pour into to_cup
    def can_pour(self, to_cup):
        if to_cup.waterTotalNum == self.MaxWaterNums:
            return False
        if to_cup.top():
            if to_cup.top().color != self.top().color:
                return False
            return True
        return True


# TODO   水排序算法
class Cups:
    def __init__(self, cups):
        self.cupNum = len(cups)
        self.ans_ope = []
        self.cups = []
        for cup in cups:
            c = Cup(cup)
            self.cups.append(c)

    def sort(self):
        pass

    def output_res(self):
        for cup in self.cups:
            if len(cup.waters) == 0:
                print('[]')
            for water in cup.waters:
                for i in range(water.num):
                    print(f"{water.color}", end=', ')
            print('')

    def output_ans(self):
        pass

    def get_all_eff_opr(self):
        pass
