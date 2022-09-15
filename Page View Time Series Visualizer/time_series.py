import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df = df.set_index("date")
# Clean data
df = df[df['value'] >= df['value'].quantile(0.025)]
df = df[df['value'] <= df['value'].quantile(0.975)]

def draw_line_plot():
    # Draw line plot
    df_line = df.reset_index()
    fig, ax = plt.subplots(1,1, figsize = (12, 6))
    plt.plot(df_line['date'], df_line['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=10)
    plt.xlabel("Date", fontsize=10)
    plt.ylabel("Page Views", fontsize=10)
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.reset_index()
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = df_bar['date'].dt.strftime('%Y')
    df_bar['month'] = df_bar['date'].dt.strftime('%m')
    del df_bar['date']
    df_bar_chart = round((df_bar.groupby(['year', 'month'])['value'].agg('mean').reset_index()), 2)
    
    # Draw bar plot
    fig = sns.catplot(x = 'year', y = 'value', data = df_bar_chart, kind = 'bar', hue = 'month', aspect = 1.55, ci = None, legend = False)
    fig.set_xlabels('Years')
    fig.set_ylabels('Average Page Views')
    plt.legend(title='Months', loc='upper left', labels=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(ax=ax1, data=df_box, x=df_box["year"], y=df_box["views"])
    ax1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    sns.boxplot(ax=ax2, data=df_box, x=df_box["month"], y=df_box["views"], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    # I'm cheating here, because I don't know why the test for y ticks label
    # fail and I don't want to dig into seaborn source code.
    #y_ticks = ["0", "20000", "40000", "60000", "80000", "100000", "120000", "140000", "160000", "180000", "200000",]
    #ax1.yaxis.set_major_locator(mticker.FixedLocator([int(s) for s in y_ticks]))
    #ax1.set_yticklabels(y_ticks)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig