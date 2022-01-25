class Water:

    def __init__(self, num, color):
        self.num = num
        self.color = color

    def add(self, w):
        if w.color != self.color:
            return False
        else:
            self.num += w.num

    def out(self, num):
        if self.num < num:
            number = self.num
            self.num = 0
            return Water(number, self.color)
        else:
            self.num -= num
        return Water(num, self.color)
