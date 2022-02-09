import os.path
from model import Cups
from solver.solver import Solver
from util import env
from adbConnector import Connector
from openCVParser.parser import Parser
import time
# test data
# 把试管抽象为一个特殊的栈(直接用数组来代替，因为数组就有append pop方法，将数组的尾部作为栈顶即试管顶部)
# 将颜色抽象为数字



if __name__ == '__main__':

    # 创建环境变量管理器对象
    envmanager = env.EnvManager()

    # 初始化环境以及连接
    envmanager.init_env()

    # 截图
    Connector.Connector.screencap()

    # 等待adb截图保存 不可删除！！！
    time.sleep(2)

    # 传入img地址生成图片解析器对象parser
    parser = Parser(os.path.abspath(".").replace('\\','/') + Connector.img_path)

    # 解析数据
    data,pos = parser()

    print("[DEBUG] position: ",pos)

    print("[DEBUG] data :",data)

    cups = Cups.Cups(data)

    # 进行求解
    Solver.sort(cups)

    # 输出求解答案
    Solver.output(data)


    # click
    for action in Solver.res:
        print("[DEBUG] ",action," ",pos[action[0]] ," -> ",pos[action[1]])
        Connector.Connector.tap(pos[action[0]][0],pos[action[0]][1])
        time.sleep(0.9)
        Connector.Connector.tap(pos[action[1]][0],pos[action[1]][1])
        time.sleep(2.5)
