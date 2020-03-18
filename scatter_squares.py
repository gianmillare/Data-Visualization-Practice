import matplotlib.pyplot as plt

# # Part 1: plotting a single point
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2,4)
#
# plt.show()

# # Part 2: Styling a plot with a single point
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
#
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()


# Part 3: Plotting a series of points
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
