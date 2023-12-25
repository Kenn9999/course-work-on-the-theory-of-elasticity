from ..models.material_body import MaterialBody
from .runge_kutta import runge_kutta_method

def move_material_body(body, A, B, dt):
    for point in body.points:
        x, y = runge_kutta_method(lambda t, y: A(t) * point.x, 0, point.y, dt)
        point.x = x
        point.y = y