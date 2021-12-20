import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("tableau-colorblind10")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize =14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", labelsize=12)

plt.show()