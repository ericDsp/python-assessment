# visual.py
import matplotlib.pyplot as plt


def plot_pie_chart(data, title):
    """Plot a pie chart with the given data."""
    labels = list(data.keys())
    sizes = list(data.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')


def plot_bar_chart(data, title, xlabel, ylabel):
    """Plot a bar chart with the given data."""
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()