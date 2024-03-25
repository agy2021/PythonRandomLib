import pandas as pd
import matplotlib.pyplot as plt

for i in range(1, 11):
    data = pd.read_excel("data.xlsx", sheet_name="data" + str(i), index_col=0)

    plt.bar(data.index, data["amount"])

    plt.xlabel("i")
    plt.ylabel("amount")

    plt.tight_layout()

    plt.ticklabel_format(style="plain", axis="y")

    max_amount = data["amount"].max()

    plt.ylim(0, max_amount * 0.1)
    plt.show()
