
# LSVC and OLS

In this notebook we perform the Linear Support Vector Classifier feature selection with L1 penalty in order to find the features that (according to this method) are the best classifiers for each of the target variables. Before that we also run some OLS preliminary models for each target variable using all of our features to find the maximum achievable R squared for each of them. There is also some PCA exploration.

# Correlation Analysis.

After having used all the models and feature selection methods to identify the most relevant features we perform a correlation analysis for each of them and all of the target variables. Here we find significance and sign of the correlation. Finally we try to use the predicted values of an OLS in sample model to plot a map and compare with the actual values of the target variable.
