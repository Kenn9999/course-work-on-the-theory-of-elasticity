from ..models.material_body import MaterialBody
from ..models.space import Space
from .runge_kutta import runge_kutta_method

def move_through_space(body, A, B, space, dt):
    trajectory = Trajectory()

    for point in body.points:
        x, y = point.x, point.y

        while space.x_min <= x <= space.x_max and space.y_min <= y <= space.y_max:
            trajectory,add_point(SpacePoint(x, y)):
            x, y = runge_kutta_method(lambda t, y: A(t) * x, 0, y, dt)

    return trajectory

