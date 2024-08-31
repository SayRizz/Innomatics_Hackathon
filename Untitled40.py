#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


#Download the data from the above link. How many ".csv" files are available in the dataset?

links = pd.read_csv("/Users/sayedrizwan/Downloads/movie_data (1)/links.csv")
movies = pd.read_csv("/Users/sayedrizwan/Downloads/movie_data (1)/movies.csv")
ratings = pd.read_csv("/Users/sayedrizwan/Downloads/movie_data (1)/ratings.csv")
tags = pd.read_csv("/Users/sayedrizwan/Downloads/movie_data (1)/tags.csv")


# In[3]:


#What is the shape of "movies.csv"?

movies.shape


# In[4]:


What is the shape of "ratings.csv"?

ratings.shape


# In[5]:


ratings.columns


# In[9]:


#How many unique "userId" are available in "ratings.csv"?

len(ratings["userId"].unique())


# In[10]:


ratings.head()


# In[11]:


ratings.columns


# In[12]:


movies.columns


# In[13]:


tags.columns


# In[14]:


links.columns


# In[17]:


rat_mo = pd.merge(ratings, movies, on = "movieId", how = "inner")


# Which movie has recieved maximum number of user ratings?
# 

# In[24]:


rat_mo.groupby(['movieId']).count().sort_values(by = 'rating', ascending =False)


# In[30]:


movies[movies["movieId"] == 356]


# In[31]:


rat_mo.head()


# Select all the correct tags submitted by users to "Matrix, The (1999)" movie?

# In[32]:


tag_mo = pd.merge(movies, tags, on = "movieId", how = "inner")


# In[51]:


tag_mo[tag_mo["title"] == "Matrix, The (1999)"]


# What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?

# In[43]:


rat_mo_Terminator = rat_mo[rat_mo["title"] == "Terminator 2: Judgment Day (1991)"]
rat_mo_Terminator["rating"].mean()


# How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?

# In[48]:


import matplotlib.pyplot as plt
rat_mo_Fight_Club = rat_mo[rat_mo["title"] == "Fight Club (1999)"]
plt.hist(rat_mo_Fight_Club["rating"])


# Mandatory Operations:
# 1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings. 
# 2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1.
# 3. Filter only those movies which have more than 50 user ratings (i.e. > 50).

# In[60]:


# 1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings.

grouped_df = ratings.groupby('movieId')["rating"].describe()


# In[61]:


#2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1.

grouped_df_mo = pd.merge(movies, grouped_df, on = "movieId", how = "inner")


# In[62]:


grouped_df_mo.columns


# In[63]:


#3. Filter only those movies which have more than 50 user ratings (i.e. > 50).

filtered_df_mo = grouped_df_mo[grouped_df_mo['count']>50]


# In[65]:


filtered_df_mo.shape


# Which movie is the most popular based on  average user ratings?

# In[67]:


filtered_df_mo.sort_values(by = "mean", ascending = False)


# Select all the correct options which comes under top 5 popular movies based on number of user ratings.

# In[68]:


filtered_df_mo.sort_values(by = "count", ascending = False).head(5)


# Which Sci-Fi movie is "third most popular" based on the number of user ratings?

# In[74]:


filtered_df_mo[filtered_df_mo['genres'].str.contains('Sci-Fi', case=False, na=False)].sort_values(by='count', ascending=False).iloc[2]


# Using "links.csv", scrape the IMDB reviews of each movie with more than 50 user ratings. "README.md" file contains the required details.

# In[80]:


import requests
import numpy as np
from bs4 import BeautifulSoup

def scrapper(imdbId):
    id = str(int(imdbId))
    n_zeroes = 7 - len(id)
    new_id = "0"*n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    request_header = {'Content-Type': 'text/html; charset=UTF-8', 
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
                      'Accept-Encoding': 'gzip, deflate, br'}
    response = requests.BeautifulSoup(URL, headers=request_header)
    soup = BeautifulSoup(response.text)
    imdb_rating = soup.find('BeautifulSoup', attrs={'BeautifulSoup' : 'BeautifulSoup'})
    return imdb_rating.text if imdb_rating else np.nan


# Mention the movieId of the movie which has the highest IMDB rating.

# In[82]:


links.sort_values(by = 'imdbId', ascending = False)


# In[87]:


filtered_df_mo1 = pd.merge(filtered_df_mo, links, on='movieId', how='inner')


# In[88]:


filtered_df_mo1.head()


# In[89]:


filtered_df_mo1.sort_values(by = 'imdbId', ascending = False)


# In[90]:


filtered_df_mo1[filtered_df_mo1['genres'].str.contains('Sci-Fi', case=False, na=False)].sort_values(by='imdbId', ascending=False)


# In[92]:


links.columns


# In[ ]:




