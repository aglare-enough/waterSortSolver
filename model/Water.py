# 游戏中的同种颜色的液体如果在一起，在倒向其他cup的时候会一起倒入
# 所以在这里将同种颜色的位置相邻的液体看作一个water对象，方便后续操作

class Water:

    def __init__(self, num, color):
        # 当前water对象中包含的真正液体的数量
        self.num = num

        # 当前water对象的颜色
        self.color = color

    # water对象的融合，传入的w是water对象，两个water对象的融合
    def add(self, w):
        if w.color != self.color:
            return False
        else:
            self.num += w.num

    # 当water所在的cup需要向外倒时，可能会出现:目标cup只能倒入数量为一（不一定是一）的液体，此时就需要从water对象中
    # 分离出数量为一的液体
    # out 方法 传入需要分离出的液体数量，返回分离出的液体的water对象实例
    def out(self, num):
        if self.num < num:
            number = self.num
            self.num = 0
            return Water(number, self.color)
        else:
            self.num -= num
        return Water(num, self.color)
