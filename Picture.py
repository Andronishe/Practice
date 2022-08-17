class Picture:
    def __init__(self, lst, width, height):
        self.bytes_ = lst
        self.width = width
        self.height = height

    def get_red(self):
        return [i[0] for i in self.bytes_]

    def get_green(self):
        return [i[1] for i in self.bytes_]

    def get_blue(self):
        return [i[2] for i in self.bytes_]


