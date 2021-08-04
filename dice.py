import pygal
from die import Die

#Create Two D6 Dice
die_1 = Die()
die_2 = Die()


#Make some rolls and store results in a list
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

#Analyze the results
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(3,max_result + 1)]

#Visualize the result
hist = pygal.Bar()

hist.title = "Results Of Multiplying 2 D6 Dice"
hist.x_labels = [x for x in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6" , frequencies)
hist.render_to_file("dice_visual.svg")


print(frequencies)
