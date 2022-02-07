from model.Water import Water
import copy


class Cup:

    # 类构造函数 ，传入一个长度==self.MaxWaterNums的数组，判断该数组是否符合数据要求，将其实例化为cup对象
    def __init__(self, waters):
        self.waterTotalNum = len(waters)
        self.MaxWaterNums = 4
        self.waters = []
        count = 0
        last = 0

        # 为杯子中的水创建water对象实例
        for water in waters:
            if last == water or last == 0:
                count += 1
            else:
                # 如果数组长度大于4，退出
                if count > self.MaxWaterNums:
                    print("cup init error,param error")
                    exit()

                # 调用water的构造函数构造water对象实例
                w = Water(count, last)

                # 将w加入到self.waters中
                self.waters.append(w)

                count = 1
            last = water
        if count != 0:
            w = Water(count, last)
            self.waters.append(w)

    # 返回当前cup的栈顶water元素，若cup为空则返回False
    def top(self):
        if len(self.waters) > 0:
            return self.waters[-1]
        return False

    # 将当前杯子向to_cup中倒入液体
    def pour_into(self, to_cup):
        if not self.can_pour(to_cup):
            return False

        # 需考虑特殊情况
        # 当water所在的cup需要向外倒时，可能会出现:目标cup只能倒入数量为一（不一定是一）的液体，此时就需要从water对象中
        # 分离出数量为一的液体


        origin_water = self.waters.pop()
        #分离液体
        out_water = origin_water.out(self.MaxWaterNums - to_cup.waterTotalNum)
        self.waterTotalNum -= out_water.num


        if origin_water.num != 0:
            self.waters.append(origin_water)
        to_cup.waterTotalNum += out_water.num
        if to_cup.top():
            to_cup.top().num += out_water.num
        else:
            to_cup.waters.append(out_water)
        return True

    # 按照游戏规则，判断是否能倒入to_cup
    def can_pour(self, to_cup):

        # 若当前cup是空的，不能倒入，返回False
        if len(self.waters) == 0:
            return False

        # 若向自身倒入，则返回False
        if self == to_cup:
            return False

        # 如果需要导入的杯子本身是满的，返回False
        if to_cup.waterTotalNum == self.MaxWaterNums:
            return False

        # 避免无意义的操作
        if len(to_cup.waters) == 0 and len(self.waters) == 1:
            return False

        # 判断to_cup的杯子顶部液体颜色是否和当前杯子顶部液体颜色相同，相同则可以倒入，不同则不能倒入
        if to_cup.top():
            if to_cup.top().color != self.top().color:
                return False
            return True
        return True




class Cups:
    # 类构造器，传入一个二维数组，将其构造成cups对象实例
    def __init__(self, cups):
        # cup的数量
        self.cupNum = len(cups)

        # 存储所有的cup对象
        self.cups = []

        # 对每一个数组生成一个cup对象实例c，并将c添加到self.cups中
        for cup in cups:
            c = Cup(cup)
            self.cups.append(c)

    # 输出排序完成的结果,主要用于debug
    def output_res(self):
        for cup in self.cups:
            if len(cup.waters) == 0:
                print('[]')
            for water in cup.waters:
                for i in range(water.num):
                    print(f"{water.color}", end=', ')
            print('')

    # 判断当前阶段是否还有可以进行的有效操作
    def has_effective_action(self):
        for i in range(self.cupNum):
            for j in range(self.cupNum):
                if self.cups[i].can_pour(self.cups[j]):
                    return True
        return False

    # 判断当前是否已经到达求解完成的阶段
    def is_success(self) -> bool:

        # 对每个cup里的waters进行判断 ，若全部都是相同颜色或者是空的则solve success
        for cup in self.cups:
            if len(cup.waters) == 0:
                continue
            if len(cup.waters) != 1 or cup.waters[0].num != cup.MaxWaterNums:
                return False
        return True

    def get_all_eff_opr(self):
        pass

    # 深拷贝对象来进行下一步的递归调用，方便回溯
    def duplicate(self) :
        newCups = copy.deepcopy(self)
        return newCups
