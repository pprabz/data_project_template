import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(df, column):
    plt.figure(figsize=(6, 4))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f"Distribution of {column}")
    plt.tight_layout()
    plt.show()

