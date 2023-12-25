import matplotlib.pyplot as plt
from ..models.stream_line import StreamLine

def plot_stream_lines(stream_lines):
    for stream_line in stream_lines:
        x_values = [point.x for point in stream_line.points]
        y_values = [point.y for point in stream_line.points]

        plt.plot(x_values, y_values, label='Stream Line')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Stream Lines')
        plt.legend()
        plt.show()

