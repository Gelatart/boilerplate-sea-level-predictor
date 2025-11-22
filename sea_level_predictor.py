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

    x_extend = np.linspace(min(x) - 10, 2050, 100)
    y_pred = slope*x_extend + intercept
    plt.plot(x_extend, y_pred)

    # Create second line of best fit


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()