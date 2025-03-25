#!/usr/bin/env python
# coding: utf-8

# # Description:
# This dataset contains district-wise data on the number of women teachers working in middle schools in Punjab over multiple
# years. It includes various districts as well as the overall total for Punjab. The data has been cleaned by replacing missing
# values with 0 and ensuring all numerical values are properly formatted. Several visualization techniques have been applied to 
# analyze trends, distributions, and variations in the dataset.
# 

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[57]:


df = pd.read_csv('Governmentdataset.csv')
df


# In[58]:


df.replace({"Year/District": {"Punjab": "Total"}}, inplace=True)
df


# In[59]:


df.fillna(0, inplace=True) 


# In[60]:


for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce').round(0).astype(int) 


# In[61]:


df


# In[62]:


plt.figure(figsize=(14, 8))
sns.boxplot(data=df.set_index("Year/District").T, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("Boxplot of Case Distribution Over the Years")
plt.show()


# This creates a boxplot to visualize the distribution of cases over the years 
# 

# In[63]:


plt.figure(figsize=(12, 6))
plt.plot(df.columns[1:], df[df['Year/District'] == 'Total'].values.flatten()[1:], marker='o', linestyle='-', color='b')
plt.title("Total Cases Over the Years")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.grid(True)
plt.show()


# This plots the total cases over the years using a line graph with markers, showing trends in case counts over time.
# 

# In[64]:


plt.figure(figsize=(12, 6))
for district in df["Year/District"]:
    plt.scatter(df.columns[1:], df[df["Year/District"] == district].values.flatten()[1:], label=district, alpha=0.5)
plt.title("Scatter Plot of Cases Over Years")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.show()


# It generates a scatter plot showing the distribution of cases over the years for each district, with different markers representing different districts.

# In[65]:


plt.figure(figsize=(14, 8))
sns.heatmap(df.set_index("Year/District").T, cmap='coolwarm', annot=False, linewidths=0.5)
plt.title("Heatmap of Cases Over the Years")
plt.show()


# It creates a heatmap to visualize the distribution and intensity of cases over the years across different districts using a color gradient.
# 

# In[66]:


highest_year = df.set_index("Year/District").sum().idxmax()
lowest_year = df.set_index("Year/District").sum().idxmin()

plt.figure(figsize=(8, 5))
plt.bar([highest_year, lowest_year], [df.set_index("Year/District")[highest_year].sum(), df.set_index("Year/District")[lowest_year].sum()], color=['red', 'green'])
plt.title("Year with Highest and Lowest Cases")
plt.xlabel("Year")
plt.ylabel("Total Cases")
plt.show()


# It identifies the years with the highest and lowest total cases and visualizes them using a bar chart with red and green bars.
# 

# In[67]:


plt.figure(figsize=(10, 6))
sns.kdeplot(df.set_index("Year/District").values.flatten(), fill=True, color='blue')
plt.title("KDE Plot of Case Distribution")
plt.xlabel("Cases")
plt.show()


# It generates a Kernel Density Estimate (KDE) plot to visualize the distribution of case values across all years and districts, highlighting density variations smoothly.
# 

# In[68]:


plt.figure(figsize=(10, 6))
plt.hist(df.set_index("Year/District").values.flatten(), bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Cases")
plt.xlabel("Cases")
plt.ylabel("Frequency")
plt.show()


# This creates a histogram to visualize the distribution of case counts, showing how frequently different case values occur.
# 

# In[69]:


plt.figure(figsize=(14, 8))
sns.violinplot(data=df.set_index("Year/District").T, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("Violin Plot of Cases Over the Years")
plt.show()


# In[70]:


plt.figure(figsize=(14, 6))
plt.fill_between(df.set_index("Year/District").columns, df.set_index("Year/District").sum(), alpha=0.5, color='blue')
plt.title("Area Plot of Total Cases Over Years")
plt.xlabel("Year")
plt.ylabel("Total Cases")
plt.show()


# It creates an area plot showing the total cases over the years, highlighting trends with a shaded region.

# In[71]:


plt.figure(figsize=(10, 10))
year = df.columns[-1]
pie_data = df.set_index("Year/District")[year]
pie_data = pie_data[pie_data > 0]
colors = plt.get_cmap("coolwarm")(np.linspace(0.2, 0.8, len(pie_data)))

plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title(f"Case Distribution in {year}")
plt.show()


# It generates a pie chart showing the distribution of cases across districts for the most recent year in the dataset, using a "coolwarm" color map.

# In[72]:


plt.figure(figsize=(12, 6))
df_sorted = df.sort_values(by=df.columns[-1], ascending=False)
sns.barplot(x=df_sorted["Year/District"].head(10), y=df_sorted[df.columns[-1]].head(10), palette="Reds")
plt.xticks(rotation=90)
plt.title("Top 10 Districts with Highest Cases")
plt.show()


# It creates a bar plot of the top 10 districts with the highest cases in the most recent year, sorting them in descending order.
# 

# In[73]:


plt.figure(figsize=(12, 6))
districts = df["Year/District"].sample(5, random_state=42)  # Random 5 districts
for district in districts:
    plt.plot(df.columns[1:], df[df["Year/District"] == district].values.flatten()[1:], marker='o', linestyle='-', label=district)
plt.title("Random Districts Case Trends")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.legend()
plt.show()


# It randomly selects 5 districts and plots their case trends over the years using a line plot.

# In[74]:


years = [df.columns[-1], df.columns[len(df.columns)//2]]
titles = ["Latest Year", "Midpoint Year"]

plt.figure(figsize=(16, 8))
for i, (year, title) in enumerate(zip(years, titles), start=1):
    plt.subplot(1, 2, i)
    pie_data = df.set_index("Year/District")[year]
    pie_data = pie_data[pie_data > 0]
    colors = plt.get_cmap("coolwarm")(np.linspace(0.2, 0.8, len(pie_data)))
    plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title(f"Case Distribution in {title}")
plt.show()


# It generates side-by-side pie charts showing the distribution of cases for the latest and midpoint years.
# 

# In[75]:


plt.figure(figsize=(12, 6))
sns.stripplot(data=df.set_index("Year/District").T, jitter=True, alpha=0.6)
plt.title("Strip Plot of Case Distribution")
plt.show()


# It creates a strip plot to visualize the distribution of case counts over the years, adding jitter for better visibility of overlapping points.
# 

# In[76]:


plt.figure(figsize=(14, 7))
selected_districts = df["Year/District"].sample(5, random_state=42)  # Random 5 districts
for district in selected_districts:
    plt.plot(df.columns[1:], df[df["Year/District"] == district].values.flatten()[1:], marker='o', linestyle='-', label=district)
plt.title("Trends of Selected Districts Over the Years")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.legend()
plt.grid(True)
plt.show()


# It randomly selects 5 districts and plots their case trends over the years using a line plot.
# 

# In[77]:


plt.figure(figsize=(14, 7))
selected_districts = df["Year/District"].sample(5, random_state=42)
for district in selected_districts:
    plt.scatter(df.columns[1:], df[df["Year/District"] == district].values.flatten()[1:], label=district, s=50)
plt.title("Scatter Plot of Cases Over Years")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.legend()
plt.grid(True)
plt.show()


# It generates a scatter plot of cases over the years for five randomly selected districts, highlighting trends in case distribution.
# 

# In[78]:


highest_year = df.set_index("Year/District").sum().idxmax()
lowest_year = df.set_index("Year/District").sum().idxmin()

plt.figure(figsize=(12, 6))
plt.plot(df["Year/District"], df[highest_year], marker='o', linestyle='-', label=f"Highest Year: {highest_year}", color="red")
plt.plot(df["Year/District"], df[lowest_year], marker='s', linestyle='--', label=f"Lowest Year: {lowest_year}", color="green")
plt.xticks(rotation=90)
plt.title("District-wise Case Trends for Highest & Lowest Year")
plt.xlabel("District")
plt.ylabel("Cases")
plt.legend()
plt.show()


# In[79]:


plt.figure(figsize=(12, 6))
average_cases = df.set_index("Year/District").drop(index="Total").mean()

plt.plot(average_cases.index, average_cases.values, marker='o', linestyle='-', color='orange', label="Avg Cases Per District")
plt.title("Average Cases Per District Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Cases")
plt.legend()
plt.grid(True)
plt.show()


# It plots the average number of cases per district over the years, excluding the "Total" row, using a line chart with markers for better visualization.
# 

# In[80]:


plt.figure(figsize=(12, 6))
districts = df["Year/District"].sample(2, random_state=10)
for district in districts:
    plt.plot(df.columns[1:], df[df["Year/District"] == district].values.flatten()[1:], marker='s', linestyle='--', label=district)
plt.title("Comparison Between Two Random Districts")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.legend()
plt.grid(True)
plt.show()


# This randomly selects two districts and plots their case trends over the years using a dashed line with square markers for comparison.

# # Observations:
# The dataset provides insights into the number of women teachers working in middle schools across different districts of Punjab
# over multiple years. Data cleaning was performed by replacing missing values with 0 and converting all numerical columns into 
# integers for uniformity. Analyzing the trends over time, it was observed that the total number of women teachers fluctuated,
# with certain years experiencing a peak while others showed a decline. Some districts consistently had a higher number of teachers, whereas others exhibited fluctuations rather than a steady increase or decrease.Visualizations provided deeper insights into these trends. The boxplot highlighted variations in teacher numbers across years,while the line plot showed an overall trend of growth or decline in total teachers. Scatter plots depicted yearly distributionsacross different districts, and heatmaps revealed density variations in teacher numbers over time. The bar chart identified years with the highest and lowest total teachers, while the histogram and KDE plot provided an overview of the distribution,indicating common and rare occurrences. The violin plot and strip plot illustrated the variability and spread of data, whereas pie charts displayed district-wise contributions for the latest and midpoint years.

# In[ ]:




