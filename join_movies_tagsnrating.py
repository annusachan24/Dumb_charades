import pandas as pd
import numpy as np
import csv
from pandas import DataFrame, merge, Series
df_1=pd.read_csv("tags_ratings_dt_full.csv",index_col=False)
df_2=pd.read_csv("movies.csv",index_col=False)

#drop column 1 
df_1.drop(df_1.columns[[0]], axis=1)
df_final=merge(df_1,df_2,on=["movieId"])
df_final.to_csv("final_dt.csv")
#delete unamed column in final_dt.csv and name column 1 as Id
print "done part 2"