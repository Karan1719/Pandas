#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd


# # Make a dataframe

# In[19]:


d1 = {'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'], 'ID': [1, 2, 3, 4], 'Salary': [100, 200, np.nan, pd.NaT],
      'Role': ['CEO', None, pd.NaT, pd.NaT]}


# # Check for the head

# In[20]:


df.head(2)


# # Check for the tail

# In[21]:


df.tail(2)


# # Check for the null Values

# In[22]:


df.isnull().sum()


# # Get the info about dataframe

# In[23]:


df.info()


# In[24]:


df = pd.DataFrame(d1)


# In[25]:


print(df)


# #  Pandas Drop All Rows with any Null/NaN/NaT Values

# In[5]:


df1 = df.dropna()


# In[6]:


print(df1)


# #  Drop All Columns with Any Missing Value

# In[7]:


df1 = df.dropna(axis=1)
print(df1)


# # Replace null Values with some other value

# In[27]:


df['Salary'].fillna('300',inplace=True)


# In[28]:


df


# In[32]:


df['Role'].fillna('CEO',inplace=True)


# In[30]:


df


# In[ ]:




