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



# Part 2: Analyzing results: Counting Frequency
die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Recording the frequency of each roll
frequencies = [] # make an empty list
for value in range (1, die.num_sides+1): # we add 1 (+1) so it will include the very last side
    frequency = results.count(value) # count how many time a certain value appears
    frequencies.append(frequency)

print(frequencies)