import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make the random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points of the walk

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

plt.savefig("plots/rw1.png", dpi=100)

plt.show()