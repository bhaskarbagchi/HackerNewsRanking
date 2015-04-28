import numpy as np
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import metrics

#Read from data file
with open("dataset") as textFile:
	lines = [line.split() for line in textFile]
a = np.array(lines, dtype=float)
# print a

# split the array to data points and target values
dataPoints = np.array(a[:, [1, 2, 3]])
target = np.array(a[:, 0])

regr = linear_model.LogisticRegression()

last_score = 0
last_partition = 0
for i in range(2, 10):
	x_train, x_test, y_train, y_test = cross_validation.train_test_split(dataPoints, target, test_size = float(i)/10.0, random_state = 0)
	regr.fit(x_train, y_train)
	if regr.score(x_test, y_test) > last_score:
		last_score = regr.score(x_test, y_test)
		last_partition = (i+1)/10
x_train, x_test, y_train, y_test = cross_validation.train_test_split(dataPoints, target, test_size = last_partition, random_state = 0)
regr.fit(x_train, y_train)
print regr.score(x_test, y_test)
#Coefficients
print('Coefficients: \n', regr.coef_)
# #Mean Squared Error
# # print("Residual sum of squares: %.2f"
# 	# % np.mean((regr.predict(dataPoints) - target) ** 2))
# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % regr.score(dataPoints, target))


#Read from data file
with open("testset") as textFile:
	lines = [line.split() for line in textFile]
a = np.array(lines, dtype=float)
# print a

# split the array to data points and target values
testPoints = np.array(a[:, [1, 2, 3]])
expectedOutput = np.array(a[:, 0])
# print dataPoints
print regr.score(testPoints, expectedOutput)
# Mean Squared Error
print("Residual sum of squares: %.2f"
	% np.mean((regr.predict(testPoints) - expectedOutput) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(testPoints, expectedOutput))


result = []
for x in dataPoints:
	result.append(regr.predict(x))
# print result
min_ = result[0]
max_ = result[0]
for x in result:
	if x > max_:
		max_ = x
	if x < min_:
		min_ = x
for x in result:
	x = 100* (x - min_)/(max_ - min_) + 1

print ('mean absolute error: %.2f' % metrics.mean_absolute_error(result, expectedOutput) )
print ('explained variance score: %.2f' % metrics.explained_variance_score(result, expectedOutput) )
print ('mean squared error: %.2f' % metrics.mean_squared_error(result, expectedOutput) )
print ('r^2 score: %.2f' % metrics.r2_score(result, expectedOutput) )