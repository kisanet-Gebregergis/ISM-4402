#!/usr/bin/env python
# coding: utf-8

# In[40]:


# --manipulating data 
#import pandas as pd 

#--a maths package
#import numpy as np


# --the basic plotting functionality that Pandas uses to produce charts and graphs.

import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')



Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)

df.head()


# In[36]:


df.hist()


# In[60]:


df.hist(column="Hours Worked")


# In[63]:


df.hist(column="Hours Worked", by="Cars Sold")


# In[55]:


df.boxplot(column='Hours Worked')


# In[59]:


axis1=df.boxplot(by='Gender', column='Hours Worked')
axis1.set_ylim(15,60)


# In[66]:


axis1=df.boxplot(by='Gender', column='Cars Sold')
axis1.set_ylim(0,8)


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[6]:


pd.pivot_table(df, values =['Cars Sold'], index=['Gender'])


# In[7]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[8]:


df['Years Experience'].mean()


# In[9]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[10]:


pd.pivot_table(df, values =['Cars Sold'], index=['SalesTraining'])


# In[ ]:




