#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install seaborn')


# ### Relational/Statistical Plots ###
# Relational Plots are used to perform multivariate analysis(more than one dt and you have to analysis that together)
# 
# 1. Scatter Plots
# 2. Line Plots - used for time series data
# 3. FaceGrids - Plotting multiple graphs side by side

# ## Scatter Plots ##
# - mainstay of statistical visualization
# - A dot chart showing how two things relate to each other.
# - Use a scatter plot when you want to see if two things are connected, like if studying hours affects test scores.
#   
# - It is used to plot for both numerical as well as categorical data, it's mostly used to depit relationship between numerical data
# 
# - There are 2 ways to draw a scatterplot in a seaborn
#   1. **relplot [Figure Level Function]
#   2. scatterplot [Axes Level Function]
#  
# 

# In[3]:


get_ipython().system('pip install matplotlib')


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[9]:


plt.style.use('fivethirtyeight') #styling element


# In[10]:


data=sns.load_dataset('tips')  


# In[12]:


data.head()


# ## Plot a Scatter Plot between total_bill and tip ##

# ## Using relplot ##

# In[14]:


#Plot here
sns.relplot(x='total_bill' , y='tip' , kind = 'scatter',data=data)


# ## The hue Parameter ##

# In[15]:


##distribution based on sex , smoker
## pass categorical dt
sns.relplot(x='total_bill' , y='tip' ,hue = 'smoker', kind = 'scatter',data=data)


# In[17]:


sns.relplot(x='total_bill' , y='tip' ,hue = 'sex', kind = 'scatter',data=data)


# ## Tbe Style Parameter ##

# In[18]:


## pass categorical dt
sns.relplot(x='total_bill' , y='tip' ,hue = 'smoker', style = 'sex',kind = 'scatter',data=data)


# ## The Size Parameter ##

# In[24]:


## numerical dt

sns.relplot(x='total_bill' , y='tip' ,hue = 'smoker', style = 'sex',size = 'size',kind = 'scatter',data=data)


# In[21]:


## hue = smoker , style = gender sex , size = size of sex(changable)


# In[25]:


sns.relplot(x='total_bill' , y='tip' ,hue = 'smoker', style = 'sex',size = 'size',sizes=(15,200),kind = 'scatter',data=data)


# In[26]:


## discrete/ continuous data


# ## Using the scatterplot function ##

# In[28]:


sns.scatterplot(x='total_bill' , y='tip' ,hue ='smoker',data=data)


# In[ ]:




