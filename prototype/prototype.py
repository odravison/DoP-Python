class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return Line(
            start=Point(self.start.x, self.start.y),
            end=Point(self.end.x, self.end.y)
        )