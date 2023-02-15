import matplotlib.pyplot as plt


def line_plot(x: list, y: list, label: str):
    """
    Generate graph plot image
    :param x: horizontal axis data
    :param y: vertical axis data
    :param label: name of graph
    """
    plt.plot(x, y)
    plt.ylabel(label)
    plt.savefig('wiki-table.png')
