from .style import apply_style, palette
import matplotlib.pyplot as plt

def styled_hist(data, bins=10, title="Histogram"):
    apply_style()
    plt.hist(data, bins=bins, color=palette['hist'], edgecolor='black', alpha=0.7)
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()
