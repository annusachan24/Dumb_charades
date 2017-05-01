from pandas import DataFrame, merge, Series
#from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn import preprocessing

#count the movies that have been rated
df_rating=DataFrame.from_csv('ratings.csv',index_col=False)
list_id=df_rating['movieId'].tolist()
list_id=set(list_id)

#count the movies that have been tagged
df_tags=DataFrame.from_csv('tags.csv',index_col=False)
list_id1=df_tags['movieId'].tolist()
list_id1=set(list_id1)


df_movies=DataFrame.from_csv('movies.csv',index_col=False)
movies_id=df_movies['movieId'].tolist()
movies_id=set(movies_id)
print len(movies_id)
remainder=movies_id-list_id
print len(remainder)

remainder1=movies_id-list_id1
print len(remainder1)

