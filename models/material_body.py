from .material_point import MaterialPoint

class MaterialBody:
    def __init__(self, radius):
        self.radius = radius
        self.points = []   # список точек материального тела

    def add_point(self, point):
        self.points.append(point)
