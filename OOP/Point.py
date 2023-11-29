class Point:

    def __init__(self):
        self.a = 6
        self.b = 8

    def draw(self):
        print(f"drawing from point {self.a} to point {self.b}")


point1 = Point()
print(point1.draw())
