from .style import apply_style, palette
import matplotlib.pyplot as plt

def styled_box(data, labels=None, title="Box Plot"):
    apply_style()
    plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor=palette['pie'], color=palette_feminine['pie']))
    if labels:
        plt.xticks(range(1,len(labels)+1), labels)
    plt.title(title)
    plt.show()
