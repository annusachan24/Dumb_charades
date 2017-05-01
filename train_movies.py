from pandas import DataFrame, merge, Series
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn import preprocessing, tree
from sklearn.externals import joblib
from sklearn.cross_validation import train_test_split 
from sklearn.metrics import classification_report, precision_score, recall_score, accuracy_score, f1_score

df_main=DataFrame.from_csv('moviesplit.csv',index_col=False)



#print df_main.head(10)
df_X=df_main.drop(['Id','movieId','title','genres'],axis=1)
df_Y=df_main['movieId']
#df_data_train1, df_data_test1, df_target_train1, df_target_test1=train_test_split(df_X,df_Y,test_size=0.70,random_state=0)
df_data_train, df_data_test, df_target_train, df_target_test=train_test_split(df_X,df_Y,test_size=0.20,random_state=0)
# df_data_train=df_data_train[1:]
# df_target_train=df_target_train[1:]
#choose a random forest classifier
#clf = RandomForestClassifier(n_estimators=10)
clf=tree.DecisionTreeClassifier()
print "start training"
print df_data_train[:10]
print df_target_train[:10]
clf.fit(df_data_train,df_target_train)
print "training done"
pred=clf.predict(df_data_test)

print "Recall is, ", recall_score(df_target_test,pred)
print "Precision is, ", precision_score(df_target_test,pred)
print "Accuracy is, ", accuracy_score(df_target_test,pred)
print "F1 score is, ", f1_score(df_target_test,pred)

# joblib.dump(clf,'model/random_clf.pkl')
# print "model dumped"