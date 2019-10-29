#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


plt.scatter(df['hours'], df['grade'])


# In[ ]:




