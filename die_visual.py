from die import Die

# Part 1: Creating a six sided Die (D6)
die = Die()

results = [] # Create an empty list
for roll_num in range(100): # We roll the Die 100 times
    result = die.roll() # we call the die.py file and the roll function within
    results.append(result) # create another variable called 'results' and append the resulting roll

print(results)

