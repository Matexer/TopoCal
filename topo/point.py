class Point:
    def __init__(self, cords):
        y, x = self.get_yx(cords)
        self.y = y   # E = Y
        self.x = x   # N = X

    def move(self, delta_y: int, delta_x: int):
        """
        :param delta_y:
        :param delta_x:
        :return:
        """
        self.y += delta_y
        self.x += delta_x

    def get_cords(self):
        y = str(self.y)
        x = str(self.x)

        while len(y) > len(x):
            x = "0" + x
        while len(x) > len(y):
            y = "0" + y

        cords = y + x
        return cords

    @staticmethod
    def get_yx(cords):
        div_point = len(cords) // 2
        x = int(cords[div_point:])
        y = int(cords[:div_point])
        return y, x

