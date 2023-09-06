# Churn-Modeling-using-ANN


**PROJECT OBJECTIVE:** The objective, as a data scientist, is to build a model that will help to identify the potential customers who have a higher probability to churn. This will help the company to understand the pain points and patterns of customer churn and will increase the focus on strategizing customer retention.

**DATA EXPLORATION AND DATA CLEANING:**

Created a single file with all the relevant variables and perform the necessary data quality checks and cleaning. In data cleaning, checked for the missing values/unexpected values in the dataset and there is no missing valu in the dataset. Also, identified the outliers in  the dataset and replaced the outliers with median. Make sure that the data types of the variables are appropriate as required for our analysis (Here, converted all the categorical variable data types to category and continuous variable data types to int or float).

**DATA ANALYSIS:**

Checked the distribution of data for the continuous (histogram charts) and categorical (pie charts) variables along with the target variable (pie charts). Performed uni-variate, bivariate, and multivariate analysis of the dataset, for example, 5-point summary of the continuous variable, pair plot, correlation matrix plot, and boxplot to detect outliers. Also, test the hypothesis for continuous and categorical variables to see the relationship between the dependent and independent variable, here, used independent t-test and chi-square test to detect the relationship.

**DATA PREPROCESSING:**

Here, removed the unwanted/irrelevant independent variable/feature based on the above analysis from the dataset. Also, encoded the categorical variable using one-hot encoding and label encoding based on the categories, and scaled the independent variable using standard scaler.

**MODEL BUILDING:**

Build an ANN model with 2 hidden layer to predict the churn customer and evaluate the model using confusion metrix, accuracy score, recall score, precision score and f1 score.

**Achieved an accuracy of 85%.**

**MODEL DEPLOYMENT:**

Created a web app using pickle (used to save and load the standardscaler model) and streamlit (used o create the web app) to predict the churn customer. (refer to "Churn Prediction web app.py" file)
