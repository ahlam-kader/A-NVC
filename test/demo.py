import matplotlib.pyplot as plt
from anvc import styled_line, styled_bar, styled_scatter, styled_hist, styled_box

x = [1,2,3,4,5]
y = [10,5,15,7,12]

fig, axs = plt.subplots(2, 3, figsize=(18,10))

axs[0,0].plot(x, y, color='#F4C2C2', marker='o')
axs[0,0].set_title("Line Chart")

colors = ['#8E4585' if i==2 else '#F4C2C2' for i in range(len(y))]
axs[0,1].bar(['A','B','C','D','E'], y, color=colors)
axs[0,1].set_title("Bar Chart")

axs[0,2].scatter(x, y, c='#C8A2C8', s=80, edgecolors='w')
axs[0,2].set_title("Scatter Plot")

axs[1,0].hist([1,2,2,3,3,3,4,4,5,5,5,5], bins=5, color='#A8E6CF', edgecolor='black')
axs[1,0].set_title("Histogram")

axs[1,1].boxplot([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]],
                 patch_artist=True,
                 boxprops=dict(facecolor='#AEC6CF', color='#AEC6CF'))
axs[1,1].set_title("Box Plot")
axs[1,1].set_xticklabels(['G1','G2','G3'])

fig.tight_layout()
plt.show()
