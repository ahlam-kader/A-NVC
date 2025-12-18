palette = {
    'line': '#F4C2C2',
    'scatter': '#C8A2C8',
    'highlight': '#8E4585',
    'alert': '#FF6F61',
    'hist': '#A8E6CF',
    'pie': '#AEC6CF',
    'background': '#E6E6FA'
}

def apply_style():
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    plt.rcParams['figure.figsize'] = (8,5)
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['grid.color'] = palette['background']
    plt.rcParams['grid.linestyle'] = '--'
