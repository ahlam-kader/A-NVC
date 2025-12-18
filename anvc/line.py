from .style import apply_style, palette
import matplotlib.pyplot as plt

def styled_line(x, y, title="Line Chart"):
    apply_style()
    plt.plot(x, y, color=palette['line'], linewidth=2, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title(title)
    plt.show()
