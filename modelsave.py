from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from joblib import dump,load

def train_model(model,X_train,X_test,Y_train,Y_test):
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    score = accuracy_score(Y_test, prediction)
    return score


def predict():
    df=pd.read_csv('data.csv')
    X = df.drop(columns=['prognosis'])
    Y = df['prognosis']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    model = [DecisionTreeClassifier(), SVC(), LogisticRegression(), GaussianNB(), KNeighborsClassifier(n_neighbors=21), RandomForestClassifier(n_estimators=101)]
    for i in model:
        score=train_model(i,X_train,X_test,Y_train,Y_test)
        print(score)
    dump(model,'filename.joblib')
# X=np.zeros(132)
# X[0]=1
# X[1]=1
# X[105]=1

# model=load('filename.joblib')
# for i in model:
#     print(i.predict([X]))
predict()