from .style import apply_style, palette
import matplotlib.pyplot as plt

def styled_scatter(x, y, title="Scatter Plot"):
    apply_style()
    plt.scatter(x, y, c=palette['scatter'], alpha=0.7, edgecolors='w', s=80)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.show()
