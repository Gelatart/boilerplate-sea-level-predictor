import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x,y)

    # Create first line of best fit
    slope, intercept, r, p, stderr = linregress(x, y)

    x_extend = pd.Series(range(1880, 2051))
    y_pred = slope*x_extend + intercept
    plt.plot(x_extend, y_pred)

    # Create second line of best fit
    df_2000 = df[df['Year'].between(2000, 2014)]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r, p, stderr = linregress(x_2000, y_2000)
    x_2000_extend = pd.Series(range(2000, 2051))
    y_2000_pred = slope_2000*x_2000_extend + intercept_2000
    plt.plot(x_2000_extend, y_2000_pred)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()