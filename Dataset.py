import csv
import math
import random
import matplotlib.pyplot as plt

#open and write to a new CSV file
with open("Dataset.csv", "a", newline = '') as output:

    writer = csv.writer(output)

    for i in range(0, 20000):

        #maximum number of radians to be 2Pi
        rad = 2 * math.pi
        
        #generate a random number of radians between 0 and 2π
        x = random.uniform(0, rad)

        #assign y the sin(x) value
        y = math.sin(x)

        #write the x and y value to a row in the csv file
        writer.writerow([x, y])
        
        #add to graph
        plt.scatter(x, y, c = "black")

#add gridlines to the graph and 
plt.grid(True, which='both')


plt.xlabel(" Pi Radians")
plt.ylabel("Sin(x)")
plt.show()
