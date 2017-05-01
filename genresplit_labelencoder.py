import pandas as pd
import numpy as np
import csv
from pandas import DataFrame, merge, Series
from sklearn import preprocessing



df_main=DataFrame.from_csv("final_dt.csv",index_col=False)


#################################################spliting the genre###########################################3
#print df_main.head(10)
genres=[]
for index, row in df_main.iterrows():
	#print type(row['genres'])
	#print row['title']
	genres.extend(row['genres'].split('|'))

genres=set(genres)
print genres

for genre in genres:
	df_main[genre]=0



for index, row in df_main.iterrows():
	temp_genres=row['genres'].split('|')
	for gen in temp_genres:
		df_main.set_value(index,gen,1)

#print df_main.head(10)

###############################extracting the release year##############################

df_main['release_year']=0
for index, row in df_main.iterrows():
	year=row['title'].strip(' ')[-5:-1]
	print row['userId'], row['movieId']
	try:
		df_main.set_value(index,'release_year',year)
	except Exception, e:
		df_main.set_value(index,'release_year',2000)

print df_main.head(10)
##########################endoing the tags#############################################
le=preprocessing.LabelEncoder()
df_main['tag']=le.fit_transform(df_main['tag'])

df_main.to_csv('final_genre_split.csv',index_col=False)
#name first col