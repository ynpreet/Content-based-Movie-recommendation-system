#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return dd[dd.index == index]["title"].values[0]

def get_index_from_title(title):
	return dd[dd.title == title]["index"].values[0]
##################################################

##Step 1: Read CSV File

##Step 2: Select Features

##Step 3: Create a column in DF which combines all selected features

##Step 4: Create count matrix from this new combined column

##Step 5: Compute the Cosine Similarity based on the count_matrix

movie_user_likes = "Avatar"


# In[3]:


dd=pd.read_csv("movie_dataset.csv")
dd.columns


# In[4]:


features=['keywords','cast','genres','director']


# In[16]:


def combined_features(row):
    try:
        return row['keywords']+" "+ row['cast']+" "+row['genres']+" "+row['director']
    except:
        return "Error:", row


# In[17]:


for feature in features:
    dd[feature]=dd[feature].fillna('')


# In[18]:


dd['combined_features']=dd.apply(combined_features, axis=1)


# In[19]:


print ("combined_features:"), dd["combined_features"].head()


# In[20]:


cv=CountVectorizer()
count_matrix=cv.fit_transform(dd["combined_features"])


cosine_sim=cosine_similarity(count_matrix)


# In[21]:


movie_user_likes="The Mummy Returns"


# In[22]:


movie_index=get_index_from_title(movie_user_likes)


# In[23]:


similar_movies=list(enumerate(cosine_sim[movie_index]))


# In[24]:


sorted_similar_movies=sorted(similar_movies,key=lambda x: x[1],reverse=True)


# In[25]:


i=0


# In[15]:


for movie in sorted_similar_movies:
    print (get_title_from_index(movie[0]))
    i=i+1
    if i>10:
        break


# In[ ]:




