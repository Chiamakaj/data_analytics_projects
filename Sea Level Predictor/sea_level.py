import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # Replace 'sea_level_data' with import file
    df = read_csv("sea_level_data")

    # Create scatter plot
    fig, ax = plt.subplots(1,1, figsize = (12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, c='Green')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.show()

    # Create first line of best fit
    last_year = df["Year"].max()
    df = df.append([{"Year": y} for y in range(last_year + 1, 2050)])
    
    fig, ax = plt.subplots(1,1, figsize = (12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, c='Green')
    plt.plot(df['Year'], intercept + slope * df['Year'], c='Red', label='fit all')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Rise in Sea Level')
    plt.show()

    # Create second line of best fit
    df_recent = df.loc[(df['Year'] >= 2000) & (df['Year'] <= last_year)]
    df_recent = df_recent.append([{'Year': y} for y in range(last_year + 1, 2050)])
    df_recent.head()
    
    new_result = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    new_slope = new_result.slope
    new_intercept = new_result.intercept
    new_y_hat = new_slope * df_recent['Year'] + new_intercept
    
    fig, ax = plt.subplots(1,1, figsize = (12, 6))
    plt.scatter(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'], s=10, c='Green')
    plt.plot(df_recent['Year'], new_y_hat, c='Red', label='fit all')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()