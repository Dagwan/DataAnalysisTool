# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Set up the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to preprocess the data
def preprocess_data(df):
    """
    Preprocesses the input DataFrame.

    Parameters:
    - df: DataFrame to be preprocessed.

    Returns:
    - Preprocessed DataFrame.
    """

    # Handling missing values by forward filling
    df.fillna(method='ffill', inplace=True)
    logger.info('Missing values after preprocessing: \n%s', df.isnull().sum())

    # Convert 'DATE' column to datetime type
    df['DATE'] = pd.to_datetime(df['DATE'])

    return df

# Function for exploratory data analysis (EDA)
def perform_exploratory_data_analysis(df):
    """
    Performs exploratory data analysis on the input DataFrame.

    Parameters:
    - df: DataFrame for Exploratory Data Analysis (EDA).
    """

    # Summary statistics for numeric columns
    logger.info('Summary statistics for numeric columns: \n%s', df.describe())

    # Correlation heatmap for numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns

    # Check if there are any numeric columns
    if len(numeric_cols) > 0:
        plt.figure(figsize=(10, 8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap')
        plt.xlabel('Numeric Columns')
        plt.ylabel('Numeric Columns')
        plt.show()

        # Distribution of numeric features
        for col in numeric_cols:
            plt.figure(figsize=(8, 6))
            sns.histplot(df[col], bins=20, kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()

    else:
        logger.info('No numeric columns to plot correlations or distributions.')

# Function for Data Analysis
def analyze_data(demand_df, supply_df):
    """
    Performs data analysis on demand and supply DataFrame
    
    Paremeters:
    - demand_df DataFrame containing demand data
    - supply_df: DataFrame contining supply data
    """
    
    # Preprocess data
    demand_df = preprocess_data(demand_df)
    supply_df = preprocess_data(supply_df)
    
    # Perform Exploratory Data Analysis (EDA)
    perform_exploratory_data_analysis(demand_df)
    perform_exploratory_data_analysis(supply_df)
    
    # Calculate market share demand
    demand_df['CSUSHPISA'] = pd.to_numeric(demand_df['CSUSHPISA'], errors='coerce')
    supply_df['CSUSHPISA'] = pd.to_numeric(supply_df['CSUSHPISA'], errors='coerce')
    
    market_share_demand = demand_df['CSUSHPISA'].sum() / (demand_df['CSUSHPISA'].sum() + supply_df['CSUSHPISA'].sum())
    
    logger.info('Market share demand: %.2f', market_share_demand)
    
    # Additional functionalities
    # Filter data
    filtered_demand = demand_df[demand_df['UMCSENT'] > 90]
    logger.info('Filtered demand data:\n%s', filtered_demand.head())
    
    # Sort data
    sorted_supply = supply_df.sort_values(by='MSACSR', ascending=False)
    logger.info('Sorted supply data:\n%s', sorted_supply.head())
    
    # Aggregate data
    average_gdp = demand_df['GDP'].mean()
    logger.info('Average GDP: \n%s', average_gdp)
    
    # Correlation calculation
    total_permit_count = supply_df['PERMIT'].sum()
    
    # Catching error
    try:
        total_permit_count_int = int(total_permit_count)
        # Convert to integer for logging
        logger.info('Total Permit Count: %d', total_permit_count_int)
    
    except ValueError:
        logger.info('Total Permit Count could not be converted to integer: %s', total_permit_count)
        total_permit_count_int = None
    
    # Draw graph to visualize results
    plt.figure(figsize=(8, 6))
    sns.lineplot(x=demand_df['DATE'], y=demand_df['CSUSHPISA'], label='Demand')
    sns.lineplot(x=supply_df['DATE'], y=supply_df['CSUSHPISA'], label='Supply')
    plt.title('Housing  Demand vs. Supply Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price Index')
    plt.legend()
    plt.show()
    
    # Compare demand and supply summary
    compare_demand_supply_summary(demand_df, supply_df)

# Function to compare demand and supply summary
def compare_demand_supply_summary(demand_df, supply_df):
    """
    Compares summary statistics between demand and supply.
    
    Parameters:
    - demand_df: DataFrame containing demand data.
    - supply_df: DataFrame containing supply data.
    """
    # Exclude the 'DATE' column from the summary statistics
    demand_summary = demand_df.drop(columns=['DATE']).describe()
    supply_summary = supply_df.drop(columns=['DATE']).describe()
    
    # Plotting demand and supply summary statistics
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.heatmap(demand_summary, annot=True, cmap='Blues', fmt='.2f')
    plt.title('Demand Summary Statistics')
    plt.subplot(1, 2, 2)
    sns.heatmap(supply_summary, annot=True, cmap='Reds', fmt='.2f')
    plt.title('Supply Summary Statistics')
    plt.tight_layout()
    plt.show()

# Load the CSV file data
demand_df = pd.read_csv('../data/demand_dataset.csv')
supply_df = pd.read_csv('../data/supply_dataset.csv')

# Manin function
def main():
    """
    Main function to execut the data analysis
    """
    
    # Analysize data
    analyze_data(demand_df, supply_df)

# Start the program
if __name__ == '__main__':
    main()