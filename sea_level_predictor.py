import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    

    # Create first line of best fit
    firstline_model=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_pred=pd.Series([i for i in range(1880,2051)])

    first_line=firstline_model.slope*x_pred+firstline_model.intercept
    plt.plot(x_pred, first_line)

    # Create second line of best fit
    datafrom2000year=df[df['Year']>=2000]
    second_line_model=linregress(datafrom2000year['Year'],datafrom2000year['CSIRO Adjusted Sea Level'])
    Second_line=second_line_model.slope*pd.Series([i for i in range(2000,2051)])+second_line_model.intercept
    plt.plot(pd.Series([i for i in range(2000,2051)]), Second_line)

    # Add labels and title

    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()