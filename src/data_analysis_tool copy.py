# Import the pandas library for Data manipulation
import pandas as pd

# Import the necessary libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Load the CSV file into DataFrame
df = pd.read_csv('../data/car_prices.csv')

"""
This line of code reads the CSV file and creates 
a DataFrame called df to store the data."""

# Fill missing values with forward-fill method
df.fillna(method='ffill', inplace=True)

# Display the first few rows of the DataFrame
print('First few rows of the dataset: ')
print(df.head())

# Display basic information about the dataset
print('\nInformation about the dataset: ')
print(df.info())

# Display summary statistics for numerical columns
print('\nSummary statistics for numeric columns: ')
print(df.describe())

"""
These lines of code will print out the first few rows of the dataset,
as well as information about each column (such as data type 
and number of non-null values). """

# Data Cleaning
# Handling missing values
# Check for missing values
missing_values = df.isnull().sum()
print('\nMissing Values: ')
print(missing_values)

# Handling Duplicates
# Check for and remove Duplicate rows

# Data Validation and Correction
# Check for and outliers in numerical columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['condition', 'odometer']])
plt.title('Box Plot of Condition and Odometer') 
plt.xlabel('Feature')
plt.ylabel('Value')
plt.show()

# Standardization
# Convert categorical variables to lowercase for consistency
df['make'] = df['make'].str.lower()
df['model'] = df['model'].str.lower()
df['trim'] = df['trim'].str.lower()
df['body'] = df['body'].str.lower()
df['transmission'] = df['transmission'].str.lower()
df['color'] = df['color'].str.lower()
df['interior'] = df['interior'].str.lower()
df['seller'] = df['seller'].str.lower()

# Feature Engineering
# Create a new feature for the age of the car
# Current year is 2024
current_year = datetime.datetime.now().year
df['car_age'] = current_year - df['year'] 

# Display the updated  DataFrame after data cleaning
print('\nFirst few rows of the cleaned dataset: ')
print(df.head())


# Plot a histogram of the selling price after cleaning
plt.figure(figsize=(8, 6))
sns.histplot(df['sellingprice'], bins=20, kde=True)
plt.title('Distribution of Car Selling Price')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show()

# Plot a scatter plot of year versus selling price after cleaning
plt.figure(figsize=(8, 6))
sns.scatterplot(x='year', y='sellingprice', data=df)
plt.title('Scatter Plot of Year Vs. Selling Price')
plt.xlabel('Year')
plt.ylabel('Selling Price')
plt.show()

# Plot a box plot of selling price by make after cleaning
plt.figure(figsize=(12, 8))
sns.boxplot(x='make', y='sellingprice', data=df)
plt.title('Box Plot of Selling Price by Make')
plt.xlabel('Make')
plt.ylabel('Selling Price')
plt.xticks(rotation=45)
plt.show()

# Plot a box plot of selling price by condition
plt.figure(figsize=(8, 6))
sns.boxplot(x='condition', y='sellingprice', data=df)
plt.title('Box Plot of Selling Price by Condition')
plt.xlabel('Condition')
plt.ylabel('Selling Price')
plt.show()

""" 
This code includes data cleaning tasks such as handling 
missing values, removing duplicates, validating and correcting data, 
standardizing categorical variables, and feature engineering. These tasks 
ensure that the dataset is clean, consistent, and ready for analysis 
and visualization."""

# Import the necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Load the CSV file into DataFrame
df = pd.read_csv('../data/car_prices.csv') 

# Fill missing values with forward-fill method
df.fillna(method='ffill', inplace=True)

# Display the first few rows of the DataFrame
print('First few rows of the dataset: ')
print(df.head())

# Display basic information about the dataset
print('\nInformation about the dataset: ')
print(df.info())

# Display summary statistics for numerical columns
print('\nSummary statistics for numeric columns: ')
print(df.describe())

# Data Cleaning
# Handling missing values
missing_values = df.isnull().sum()
print('\nMissing Values: ')
print(missing_values)

# Data Validation and Correction
# Check for outliers in numerical columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['condition', 'odometer']])
plt.title('Box Plot of Condition and Odometer') 
plt.xlabel('Feature')
plt.ylabel('Value')
plt.show()

# Standardization
# Convert categorical variables to lowercase for consistency
df['make'] = df['make'].str.lower()
df['model'] = df['model'].str.lower()
df['trim'] = df['trim'].str.lower()
df['body'] = df['body'].str.lower()
df['transmission'] = df['transmission'].str.lower()
df['color'] = df['color'].str.lower()
df['interior'] = df['interior'].str.lower()
df['seller'] = df['seller'].str.lower()

# Feature Engineering
# Create a new feature for the age of the car
current_year = datetime.datetime.now().year
df['car_age'] = current_year - df['year'] 

# Question 1: Distribution of vehicle prices based on their condition
plt.figure(figsize=(8, 6))
sns.boxplot(x='condition', y='sellingprice', data=df)
plt.title('Box Plot of Selling Price by Condition')
plt.xlabel('Condition')
plt.ylabel('Selling Price')
plt.show()

# Question 2: Mileage variation with the age of the car
plt.figure(figsize=(8, 6))
sns.scatterplot(x='car_age', y='odometer', data=df)
plt.title('Scatter Plot of Age Vs. Odometer Reading')
plt.xlabel('Car Age')
plt.ylabel('Odometer Reading')
plt.show()

# Additional Visualization: Histogram of Selling Price
plt.figure(figsize=(8, 6))
sns.histplot(df['sellingprice'], bins=20, kde=True)
plt.title('Distribution of Car Selling Price')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show()
