#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install numpy')


# In[5]:


get_ipython().system('pip install pandas')



# In[7]:


get_ipython().system('pip install matplotlib')
 


# In[9]:


get_ipython().system('pip install seaborn')


# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[26]:


df = pd.read_csv("C:/Users/Admin/Desktop/student.csv")


# In[27]:


print(df.head())


# In[28]:


df.describe()


# In[29]:


df.info()


# In[30]:


df.isnull().sum()


# In[31]:


df = df.drop("Unnamed: 0", axis = 1)
print(df.head)


# In[32]:


df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()


# In[40]:


plt.figure(figsize= (4,5))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.show()


# In[42]:


gb =df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[50]:


plt.figure(figsize= (4,4))
sns.heatmap(gb, annot = True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# In[48]:


gb1 =df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb1)


# In[51]:


plt.figure(figsize= (4,4))
sns.heatmap(gb1, annot = True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# In[52]:


sns.boxplot(data = df, x = "MathScore")
plt.show()


# In[53]:


sns.boxplot(data = df, x = "ReadingScore")
plt.show()


# In[54]:


sns.boxplot(data = df, x = "WritingScore")
plt.show()


# In[55]:


print(df["EthnicGroup"].unique())


# In[70]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["group A", "group B","group C","group D","group E"]

mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
print(mlist)
plt.pie(mlist, labels = l, autopct ="%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[ ]:




