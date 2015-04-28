import numpy as np
from sklearn.neural_network import BernoulliRBM
from sklearn import cross_validation

#Read from data file
with open("dataset") as textFile:
	lines = [line.split() for line in textFile]
a = np.array(lines, dtype=float)

dataPoints = np.array(a[:, [1, 2, 3]])
target = np.array(a[:, 0])

model = BernoulliRBM()
last_score = 0
last_partition = 0
for i in range(2, 10):
	x_train, x_test, y_train, y_test = cross_validation.train_test_split(dataPoints, target, test_size = float(i)/10.0, random_state = 0)
	model.fit(x_train, y_train)
	if (model.score_samples(x_test, y_test)) > last_score:
		last_score = model.score_samples(x_test, y_test)
		last_partition = (i+1)/10
x_train, x_test, y_train, y_test = cross_validation.train_test_split(dataPoints, target, test_size = last_partition, random_state = 0)
model.fit(x_train, y_train)
print model.score_samples(x_test, y_test)
print last_score