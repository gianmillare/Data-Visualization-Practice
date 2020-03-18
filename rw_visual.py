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



# # Part 2: Generating Multiple Random Walks - as long as the program is active
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('seaborn')
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#
#     plt.savefig("plots/rw2.png", dpi=100)
#
#     plt.show()
#
#     keep_running = input("Shall we make another walk? (y/n): ")
#     if keep_running == 'n':
#         break




# # Part 3: Styling the Walk
#
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('seaborn')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#     # edgecolors-'none' removes the black outline to make the colors more noticable
#
#     plt.savefig("plots/rw3.png", dpi=100)
#
#     plt.show()
#
#     keep_running = input('Shall we go for another walk? (y/n): ')
#     if keep_running == 'n':
#         break




# # Part 4: Plotting the Starting and Ending points
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('seaborn')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#
#     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#
#     # Here we begin emphasizing the beginning and ending points
#     ax.scatter(0, 0, c='green', edgecolors='none', s=175)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=175)
#
#     plt.savefig("plots/rw4.png", dpi=100)
#
#     plt.show()
#
#     keep_running = input("Shall we go for another walk? (y/n): ")
#     if keep_running == 'n':
#         break




# # Part 5: Cleaning up the axes
# while True:
#     rw =RandomWalk()
#     rw.fill_walk()
#
#     plt.style.use('seaborn')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#
#     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#
#     ax.scatter(0, 0, c='green', edgecolors='none', s=175)
#     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=175)
#
#     # Remove the axes
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
#     plt.savefig("plots/rw5.png", dpi=100)
#
#     plt.show()
#
#     keep_running = input("Shall we go for another walk? (y/n): ")
#     if keep_running == 'n':
#         break




# Part 6: Adding Plot Points with bigger data; configuring the plot size
while True:
    rw = RandomWalk(50_000) # here we increase the data to be ten times bigger
    rw.fill_walk()

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15,9)) # putting 'figsize' into this function allows us to control the plot's size
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1) # we set size to 1

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.savefig("plots/rw6.png", dpi=100)

    plt.show()

    keep_running = input("Shall we go for another walk? (y/n): ")
    if keep_running == 'n':
        break

