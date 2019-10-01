#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[5]:


bins = 0,80,100
Status_names = ['Fail','Pass']
df['Status'] = pd.cut(df['grade'], bins, labels = Status_names)
df


# In[6]:


pd.value_counts(df['Status'])


# In[ ]:




