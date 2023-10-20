#!/usr/bin/env python
# coding: utf-8

# # DATA CLEANING

# In[4]:


import pandas as pd


# In[5]:


df = pd.read_csv('Depression.csv')


# In[6]:


df.info


# In[7]:


df.head(20)


# In[8]:


#cleaning the dataset by removing rows with missing values.
#ensuring specific columns containing numeric data are 
#converted to the appropriate data type for further analysis

missing_data = df.isnull().sum()
columns_with_missing_values = ['Year', 'Entity', 'Schizophrenia (%)', 'Bipolar disorder (%)',
                                'Eating disorders (%)', 'Anxiety disorders (%)',
                                'Drug use disorders (%)', 'Depression (%)', 'Alcohol use disorders (%)']

df.dropna(subset=columns_with_missing_values, inplace=True)
numeric_columns = ['Year', 'Schizophrenia (%)', 'Bipolar disorder (%)',
                   'Eating disorders (%)', 'Anxiety disorders (%)',
                   'Drug use disorders (%)', 'Depression (%)', 'Alcohol use disorders (%)']

df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
df.reset_index(drop=True, inplace=True)


# In[9]:


df


# In[10]:


print(df)


# In[11]:


df.describe()


# In[12]:


df.isnull().sum()


# In[13]:


df


# In[14]:


df = df.drop(columns=['Code'])


# In[15]:


df


# In[16]:


df.to_csv("filtered_depression")


# In[17]:


df1 = pd.read_csv("filtered_depression 1.csv")


# # PREDICTIVE ANALYSIS

# In[18]:


df1


# In[19]:


#EXPLORATORY ANALYSIS


# In[20]:


df1.columns


# In[22]:


df1 = df1.drop(columns=['Unnamed: 0'])


# In[23]:


df1


# In[24]:


req_headers = ['Entity', 'Year', 'Schizophrenia (%)', 'Bipolar disorder (%)',
       'Eating disorders (%)', 'Anxiety disorders (%)',
       'Drug use disorders (%)', 'Depression (%)',
       'Alcohol use disorders (%)']
req_df = df1[req_headers]
req_df.head()


# In[25]:


nation_avg = req_df.groupby('Entity', as_index = False).agg({'Schizophrenia (%)':'mean', 'Bipolar disorder (%)':'mean','Eating disorders (%)':'mean', 'Anxiety disorders (%)':'mean', 'Drug use disorders (%)':'mean', 'Depression (%)':'mean', 'Alcohol use disorders (%)':'mean'})


# In[27]:


for i in nation_avg.columns[1:]:
    print(i)


# In[29]:


import matplotlib.pyplot as plt
import random


colors = ['red', 'orange', 'purple']


for i in nation_avg.columns[1:]:
    top_10_nation_group_issue_avg = nation_avg.sort_values(by=i, ascending=False).head(10)
    
    # generates the random colors for bars in the figure.
    bar_colors = []
    for j in range(20):
        bar_colors.append(random.choice(colors))
        
    fig, ax = plt.subplots(figsize=(8,8))
    ax.bar(top_10_nation_group_issue_avg['Entity'],top_10_nation_group_issue_avg[i] , width=0.35, label=i, color=bar_colors)
    
    ax.set_ylabel('avg_mental_issue')
    ax.set_title(f"Top 10 average mental issue visualization for '{i}' by nations ")
    plt.xticks(rotation=90)
    ax.legend()
    
    plt.show()


# In[ ]:




