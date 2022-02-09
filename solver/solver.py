from model.Cups import Cups


class Solver:
    # 存储答案
    res = []

    # 模式可选值 "REALESE"　"DEBUG"
    mode = "RELEASE"

    # 类构造函数
    def __init__(self):
        pass

    # 类方法 dfs求解算法
    @classmethod
    def sort(cls, cups: Cups):

        # 递归边界条件，判断当前状态是否已求解成功，求解成功则返回True,不往下进行
        if cups.is_success():
            print('solve success')
            return True

        # 判断当前是否还有可以进行的操作，如果没有则回溯
        if not cups.has_effective_action():
            return False


        for i in range(cups.cupNum):
            for j in range(cups.cupNum):

                # 对每一种可能的组合判断是否可以倒入
                if cups.cups[i].can_pour(cups.cups[j]):

                    # 深拷贝，便于回溯，虽然会降低效率，但是v1先这样写
                    newcups = cups.duplicate()
                    newcups.cups[i].pour_into(newcups.cups[j])

                    # 判断当前操作是否无意义（即对求解游戏毫无帮助）
                    # 判断方法：如果当前从i倒入j之后，从j还可以倒入i,我们称从i倒入j是无意义的，对求解游戏毫无帮助
                    # 如果当前操作无意义，则直接continue，不往下进行
                    if newcups.cups[j].can_pour(newcups.cups[i]):
                        newcups.cups[j].pour_into(newcups.cups[i])
                        continue

                    # 将当前操作添加到solver类的存储答案的空间中
                    cls.res.append((i, j))
                    # print("add " + str(i) + "," + str(j))

                    # 递归调用，如果返回True,说明找到了答案，可以停止所有递归，直接Return True
                    if Solver.sort(newcups):
                        return True

                    # 如果递归调用返回False ,说明这一步的操作是错误的，从答案列表中删除这一步
                    cls.res.pop()
        return False


    # 类方法，用于输出答案
    @classmethod
    def output(cls, data):

        print(cls.res)

        # DEBUG模式下会输出每一步结束后的数组
        if cls.mode == "DEBUG":
            cups = Cups(data)
            print('--------------------------------')
            print(data)
            print('--------------------------------')
            for act in cls.res:
                cups.cups[act[0]].pour_into(cups.cups[act[1]])
                cups.output_res()
                print('--------------------------------')
