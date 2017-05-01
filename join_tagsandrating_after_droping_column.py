import pandas as pd
import numpy as np
import csv
from pandas import DataFrame, merge, Series

#df_movies=pd.read_csv("movies.csv")
#df_links=pd.read_csv("links.csv")
df_ratings=pd.read_csv("ratings.csv")
df_tags=pd.read_csv("tags.csv")

df_ratings.drop('timestamp', axis=1, inplace=True)
df_tags.drop('timestamp', axis=1, inplace=True)

df_tags_ratings=merge(df_tags,df_ratings,on=["userId","movieId"])
df_tags_ratings.to_csv("tags_ratings_dt_full.csv")



print "done part 1"
