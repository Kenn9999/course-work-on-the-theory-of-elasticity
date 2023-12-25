import matplotlib.pyplot as plt
from ..models.trajectory import Trajectory

def plot_trajectory(trajectory):
    x_values = [point.x for point in trajectory.points]
    y_values = [point.y for point in trajectory.points]

    plt.plot (x_values, y_values, label='Trajectory')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt,title('Material Body Trajectory')
    plt.legend()
    plt.show()