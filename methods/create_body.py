from ..models.material_point import MaterialPoint
from ..models.material_body import MaterialBody


def create_material_body(radius):
    body = MaterialBody(radius)
    # можно добавить начальные точки или другую логику по мере необходимости
    return body
