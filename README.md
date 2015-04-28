# HackerNewsRanking
Implemented various ML models on hacker news for ranking

## Train, Test and Validation set
Scraped al the articles of Hacker News at 1:00am 28th April,2015 and used top 100 as training set
In testing phase, performed k fold cross validation, where k was selected by iterating over k from 1 to 10 and taking the best score among them
Scraped al the articles of Hacker News at 9:30am 28th April,2015 and used top 100 as training set

## Evaluation metrics
With each implemented model the evaluation metrics are present in the corresponding output file

## Feature Selection
* Time(in hours) is an important feature
* Points(i.e. number of upvotes) is intutively very important
* Number of comments: Although didn't find any significant correlation, but included it
* Karma score of user who posted the news: Didn't find any correlation, so finally removed it
* As hacker news is only link aggreator, and doesn't have the articles, uesd no NLP feature.

Used the scikit python library for various models, namely
* Linear Regression
* Logistic Regression
* Lasso
* Perceptron
* SGD Regressor
* SVR
* Bayesian Redge

Output file for each model is also present in the directory. The evaluation metrics used are:
* Mean Absolute Error of rankings
* Mean Squared Error of rankings
* R^2 Score for expected and predicted output
* Residual Sum of Squares
* Variance
* Explained Variance Score
