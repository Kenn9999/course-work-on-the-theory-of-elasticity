from math import sin, exp
from models.space import Space
from methods.create_body import create_material_body
from methods.move_through_space import move_through_space
from methods.plot_trajectory import plot_trajectory
from methods.plot_stream_lines import plot_stream_lines

def main():
    radius = 1  # радиус материального тела
    A = lambda t: sin(t)  # функция A(t)
    B = lambda t: exp(t)  # функция B(t)

    # задаем область
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    space = Space(x_min, x_max, y_min, y_max)

    body = create_material_body(radius)  # создание материального тела
    space = Space(x_min, x_max, y_min, y_max)

    body = create_material_body(radius)  # создание материального тела
    trajectory = move_through_space(body, A, B, space, dt=0.01)  # движение тела и получение траектории

    plot_trajectory(trajectory)  # построение графика траектории

    # построение линий тока
    stream_lines = []
    start_time, end_time, time_step = 0, 10, 1
    for t in range(start_time, end_time, time_step):
        stream_line = move_through_space(body, A, B, space, dt=0.01)
        stream_lines.append(stream_line)

    plot_stream_lines(stream_lines)  # построение графика линий тока

    if __name__ == "__main__":
        main()
