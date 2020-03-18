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





# # Part 3: Plotting a series of points
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)
#
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()





# # Part 4: Calculating data automatically using scatter plot
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values] # we are squaring every value(x) in the x_values list
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)
#
# ax.set_title("Square Numbers", fontsize=20)
# ax.set_xlabel("Values", fontsize=12)
# ax.set_ylabel("Square of Values", fontsize=12)
#
# ax.axis([0, 1100, 0, 1100000]) # we use this method to specify the range of each axis because the values are much larger.
# # This method requires the min and max values for the x and y axis
# #ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()




# # Part 5: Color Maps - Defining custom colors
# # like so --> ax.scatter(x_values, y_values, c='red', s=10)
# # or by using the RGB method like so --> ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# # or by using the COLOR MAPS as show below
#
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
#
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#
# ax.set_title("Square Numbers", fontsize=20)
# ax.set_xlabel("Values", fontsize=12)
# ax.set_ylabel("Square of Values", fontsize=12)
#
# ax.axis([0, 1100, 0, 1100000])
#
# plt.show()


# OPTIONAL: Saving plots automatically --> plt.savefig('~filename~.png', bbox_inches='tight')

# Part 6: Practice using Cube (x**3)

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cube Numbers", fontsize=20)
ax.set_xlabel("Values", fontsize=12)
ax.set_ylabel("Cube of Values", fontsize=12)

ax.axis([0, 1100, 0, 1300000000])

plt.savefig('plots/scatter3.png', dpi=100)

plt.show()



