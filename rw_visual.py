import matplotlib.pyplot as plt

from random_walk import RandomWalk

# # Part 1: Plot the points of the walk
# rw = RandomWalk()
# rw.fill_walk()

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
#
# plt.savefig("plots/rw1.png", dpi=100)
#
# plt.show()

# Part 2: Generating Multiple Random Walks - as long as the program is active

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)

    plt.savefig("plots/rw2.png", dpi=100)

    plt.show()

    keep_running = input("Shall we make another walk? (y/n): ")
    if keep_running == 'n':
        break

