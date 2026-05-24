from json import load
from os import path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    theta0 = 0
    theta1 = 0
    normalization = 1
    if path.exists("thetas.json"):
        with open("thetas.json", "r") as f:
            thetas = load(f)
        theta0 = thetas["theta0"]
        theta1 = thetas["theta1"]
        normalization = thetas["normalization"]

    df = pd.read_csv("data.csv")

    y_pred = theta0 + theta1 * (df["km"] / normalization)
    y_true = df["price"]

    ss_res = ((y_true - y_pred) ** 2).sum()
    ss_tot = ((y_true - y_true.mean()) ** 2).sum()
    r2 = 1 - (ss_res / ss_tot)

    print(f"Précision du modèle (R²) : {r2:.4f}")

    x_line = np.linspace(df["km"].min(), df["km"].max(), 100)
    y_line = theta0 + theta1 * (x_line / normalization)

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(data=df, x="km", y="price", ax=ax, label="Données réelles", color="steelblue")
    ax.plot(x_line, y_line, color="tomato", linewidth=2, label="Régression linéaire")

    ax.set_title("Prix vs Kilométrage")
    ax.set_xlabel("Kilométrage (km)")
    ax.set_ylabel("Prix (€)")
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()