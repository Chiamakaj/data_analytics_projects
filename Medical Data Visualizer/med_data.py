import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x:1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x:1 if x > 1 else 0)
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars= ['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat['total'] = 0
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).count().reset_index()
    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data = df_cat, x = 'variable', y = 'total' , col = 'cardio', hue= 'value', kind = 'bar')


    # Get the figure for the output
    fig = plot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df
    df_heat = df_heat[df_heat["ap_lo"] <= df_heat["ap_hi"]]
    df_heat = df_heat[df_heat["height"] >= df_heat["height"].quantile(0.025)]
    df_heat = df_heat[df_heat["height"] <= df_heat["height"].quantile(0.975)]
    df_heat = df_heat[df_heat["weight"] >= df_heat["weight"].quantile(0.025)]
    df_heat = df_heat[df_heat["weight"] <= df_heat["weight"].quantile(0.975)]
    df_heat.head()

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, vmax = 0.3, center = 0, annot = True, square = True, linewidths=0.5, cbar_kws={"shrink": 0.5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig