from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy
import csv

#set random seed for repeatable results
numpy.random.seed(7)

#load dataset
training_dataset = numpy.loadtxt("training_dataset.csv", delimiter = ",")

#split into inputs and labels (X and Y respectively)
X_train = training_dataset[:,0:1]
Y_train = training_dataset[:,1]

#generate the neural network
model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1))

# Compile model
model.compile(loss='mse', optimizer='adam', metrics=['mse'])

# train model
history = model.fit(X_train, Y_train, epochs=1000, batch_size=100, verbose=2)

#load test data
test_dataset = numpy.loadtxt("test_dataset.csv", delimiter = ",")
X_test = test_dataset[:,0:1]

#use test inputs to generate predictions (outputs)
Y_test = model.predict(X_test)

#add to graph
plt.scatter(X_train, Y_train, c = "black")
plt.scatter(X_test, Y_test, c = "red")

#add gridlines to the graph and 
plt.grid(True, which='both')


plt.xlabel("Pi Radians")
plt.ylabel("Sin(x)")
plt.show()
        
