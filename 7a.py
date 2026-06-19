import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
df=pd.read_csv('fruits.csv')
# X=df.drop(['Type'],axis=1)
# y=df['Type']
df.dropna(inplace=True)
#df=df.fillna(df.mean(numeric_only=True))
# df.dropna(inplace=True)
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2
,random_state=42)
metrics=['minkowski','euclidean']
for metric in metrics:
    print(f"Using {metric} distance:")
    model=KNeighborsClassifier(n_neighbors=5, metric=metric)
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    cm=confusion_matrix(y_test,y_pred)
    print("accuracy:",accuracy)
    print("confusion matrix:")
    print(cm)
