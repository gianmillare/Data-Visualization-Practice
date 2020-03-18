import matplotlib.pyplot as plt # Main import

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25] # You will need a variable assigned to a list of values

plt.style.use('seaborn')
fig, ax = plt.subplots() # "fig" represents the figure and collection of plots, "ax" represents a single plot in the figure
ax.plot(input_values, squares, linewidth=3)
# ax.plot(squares, linewidth = 3) # controls the width of the line

# Chart Title and Axis
ax.set_title("Square Numbers", fontsize=24) # Sets the title of the chart, also adds font size
ax.set_xlabel("Value", fontsize=14) # Title of the x-axis and adds font size
ax.set_ylabel("Square of the Value", fontsize=14) # Title of the y-axis and adds font size

# Set the size of the tick labels on the axis
ax.tick_params(axis='both', labelsize=14) # Styles the tick marks on both axis

plt.show()
