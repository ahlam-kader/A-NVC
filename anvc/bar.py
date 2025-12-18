from .style import apply_style, palette
import matplotlib.pyplot as plt

def styled_bar(x, y, title="Bar Chart", highlight_index=None, horizontal=False):
    apply_style()
    colors = [palette['highlight'] if i==highlight_index else palette_feminine['line'] for i in range(len(x))]
    if horizontal:
        plt.barh(x, y, color=colors)
        plt.xlabel('Values')
        plt.ylabel('Categories')
    else:
        plt.bar(x, y, color=colors)
        plt.xlabel('Categories')
        plt.ylabel('Values')
    plt.title(title)
    plt.show()
