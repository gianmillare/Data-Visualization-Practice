from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# # Part 1: Creating a six sided Die (D6)
# die = Die()
#
# results = [] # Create an empty list
# for roll_num in range(100): # We roll the Die 100 times
#     result = die.roll() # we call the die.py file and the roll function within
#     results.append(result) # call the variable 'results' and append the resulting roll
#
# print(results)



# # Part 2: Analyzing results: Counting Frequency
# die = Die()
#
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# # Recording the frequency of each roll
# frequencies = [] # make an empty list
# for value in range (1, die.num_sides+1): # we add 1 (+1) so it will include the very last side
#     frequency = results.count(value) # count how many time a certain value appears
#     frequencies.append(frequency)
#
# print(frequencies)



#  Part 3: Make a Histogram
die =Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides + 1)) # x-axis will be the number of sides + 1
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='plotly_htmls/d6.html')
