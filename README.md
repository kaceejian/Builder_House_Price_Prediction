# BOB THE BUILDER

## Teammates:

- Ricky
- Ehizogie
- Kacee Kira

## Purpose/Overview:

What’s your home worth? Estimating the value of a property is necessary for many different reasons, including financing, sales, property insurance. And the simple answer to your home worth is the purchase price. Each real estate has unique features such as location, size, and other features which make up the home price. Therefore, the home price is an essential factor in selling a house.
With realistic variables such as Roof material, Proximity to various conditions, Garage quality, Type of Sale, Exterior covering on the house (if more than one material), Exterior covering on house, Sale condition, Type of roof, Home functionality rating, and Physical locations within Ames city limits, we can predict the price of a home in Ames, Iowa. Our goal is to assist you in making renovation plans to compete in today’s market using a linear regression model.

## Research Questions:

1. How does the feature (such as location, size, rooftop material, etc.) of the house affect the overall house price?
2. What are the features that have the highest coefficients related to the house sale price?
3. We'd like to create a machine learning model that can predict a house price with a list of customized features.

## Data Source:

House Price Prediction Data from Kaggle
https://www.kaggle.com/c/neolen-house-price-prediction/data

## Tools:

- Python/Jupyter Notebook
- Pandas
- Sklearn
- Matplotlib
- HTML
- CSS
- Flask
- Heroku

---

## PROCESS:

> DATA CLEANING / TRANSFORMATION / FEATURE SELECTION / MODEL TRAINING & RESULTS /
> by doing the following steps:

### -> Check overall correlation:

1. Run correlation between all features and SalePrice column,drop low correlation features.
2. Identify and drop columns that have too many null values (columns that have more than 1000 null values), which are not useful data for what we're trying to predict.
3. Collect the column names that contain over 1000 useful values and turn it into a dataframe.
4. Identify the correlation again between the columns with low null values and SalePrice.
5. Drop columns with correlations that are lower than 0.05 and save the remaining columns into a new dataframe that represents columns have have high correlation with SalePrice.

### -> Clean Numeric Columns:

6. Select numeric columns from the above new high correlation dataframe and plot histograms
7. From the plots, we can see that the LotArea plot shows that there are not too many houses that have a lot size value that is more than 50,000.
8. Based on this finding, we cut off the outliers of Lot Areas that are above 50,000 and save the data to a new dataframe.

### -> Clean Categorical columns:

9.  From the above new dataframe, select columns that are categorical only.
10. Group by each column to see the average SalePrice.
11. Find out how many levels are in each column. Check if there're columns with a single level. There was none.
12. Estimate the correlation for each column with SalePrice.
13. Drop the low correlation column with a threshold of 0.15.

### -> Dummification:

14. Dummify the dataframe.
15. Check if there are any null values and fill na with average value.

### -> Machine Learning Models:

Model 1:

16. From the latest dataframe, identify X and y.
17. Split the data into X_train, X_test, y_train, y_test.
18. Run Linear Regression. The report showed:

- Root mean squared error: 34854.74
- Coefficient of determination: 0.72

Model 2:

19. For the purpose of making the website input page, we decided to retrain the model again with the most important features. Use coefficient to find out the most important features.
20. Find out the normalized coefficient values.
21. Select the top 10 columns that have the highest coefficients.
22. Retrain the model with the top 10 columns, which have 97 features (sub-categories) in total.
23. Run Linear Regression. The report this time showed:

- Root mean squared error: 46194.08
- Retrain Coefficient of determination: 0.52

---

## Conclusions / Final Analysis:

We were able to create/train a model that has an RMSE of 34854.74, and the Coefficient of determination of 0.72.
And, by implementing this model, we were able to create a input form for builders to customize house features for a predicted sale price, so that they can use this form to best estimate and put together the best combination of features needed for each unique case.

## Challenges:

There were some challenges throughout the process. For example there were challenges in data preprocessing and during the cleaning process from figuring out the correlation, numerical data clearning and categorical data clearning, but finally have them figured out. There were also challenges in how to connect the model to the user input form, there were at once not matching data feature quantities and the process stuck for a bit, but then finally figured out.

## Next steps (with time, what would we do?)

If there were more time, for next steps:

1. For data cleaning, we could also try to bin the sub-categories with less values into an "others" column.
2. Currently we are using the top most important 94 features for the user input form for the overall efficiency and project timeframe. But if we had more time, we could implement the entire 222 features that are relevant to the model, which might help improve the overall prediction accuracy.
3. We currenly deply the database to Heroku, we could also try to deploy it to AWS.

---

## Thank you!
