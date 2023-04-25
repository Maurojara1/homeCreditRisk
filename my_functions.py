# Function to calculate missing values by column# Funct 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''######################################################### Cleaning ##########################################################################'''
def drop_features(df, x):
        null_percentages = df.isnull().sum()/df.shape[0]
        # get a list of columns where more than x% of the values are null
        null_columns = null_percentages[null_percentages > x].index.tolist()

        # drop the null columns from the DataFrame
        clean_df = df.drop(null_columns, axis=1)

        # Return the dataframe without features with more than x% of null values.
        return clean_df

def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns

'''################################################################ Ploting ####################################################################'''

def plot_histograms(df, bins=10, figsize=(10, 10)):
    """
    Plots histograms for each column in a dataframe.
    
    Parameters:
        df (pandas.DataFrame): The dataframe to plot histograms for.
        bins (int, optional): The number of bins for the histograms. Defaults to 10.
        figsize (tuple, optional): The size of the figure in inches. Defaults to (10, 10).
    """
    # Determine the number of rows and columns for the subplots
    n_rows = int(np.ceil(np.sqrt(len(df.columns))))
    n_cols = int(np.ceil(len(df.columns) / n_rows))
    
    # Create the subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.ravel()

    # Loop over each column and plot the histogram
    for i, column in enumerate(df.columns):
        ax = axes[i]
        ax.hist(df[column].dropna(), bins=bins)
        ax.set_title(column)
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        
    # Adjust the spacing between subplots
    fig.tight_layout()
    
    # Show the plot
    plt.show()

'''################################################################ EDA ####################################################################'''

def print_unique_values(df, col_name):
    if df[col_name].dtype == 'object':
        unique_vals = df[col_name].unique()
        print(f"Unique values for {col_name}: {unique_vals}")
        print()