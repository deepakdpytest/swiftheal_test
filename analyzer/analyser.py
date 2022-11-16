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
from joblib import load
from functools import lru_cache

def countOneRatio(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.sum(a*b)/np.sum(a)

def strtoarr(txt):
    lst=txt.split(',')
    lst=list(map(eval,lst))
    a=np.array(lst)
    return a

def arrtostr(arr):
    a=""
    for i in range(len(arr)-1):
        a+=str(arr[i])+','
    a+=str(arr[len(arr)-1])
    return a

def changeform(a,symbol):
    lst2=[]
    if(symbol==' '):
        for item in a:
            item2=item.replace(' ','_')
            lst2.append(item2)
    else:
        for item in a:
            item2=item.replace('_',' ')
            lst2.append(item2)
    return lst2

@lru_cache(maxsize=2)
def csvreader():
    df=pd.read_csv('data.csv')
    return df

@lru_cache(maxsize=2)
def twowaymapperutill():
    df = csvreader()
    symplist = list(df.columns)
    symplist.pop()
    twowaymapper = list(zip(range(132), symplist))
    return twowaymapper

def twoWayMapper(a):
    twowaymapper = twowaymapperutill()

    if(type(a) == type(1)):
        return twowaymapper[a][1]
    else:
        for item in twowaymapper:
            if(item[1] == a):
                return item[0]
        return -1


def maxCorr(question, flag):
    corrMax = 0
    lst = [None, None]
    # df = pd.read_csv('data.csv')
    df=csvreader()
    symplist = list(df.columns)
    symplist.pop()
    symptoms = symplist.copy()
    ser = pd.Series(np.ones(len(df)))
    for ques in question:
        ser = ser*df[ques]
    for symp in symptoms:
        if(symp not in question and flag[twoWayMapper(symp)] == 0):
            corr = countOneRatio(ser, df[symp])
            if(corrMax <= corr):
                corrMax = corr
                lst[0] = corrMax
                lst[1] = symp
    return lst


def symptomanalyser(ques,rep,flag):
    for q in ques:
        if(q=="None of these"):
            continue
        rep[twoWayMapper(q)] = 1
        flag[twoWayMapper(q)] = 1
        corr = 1
    lst = []
    ask=[]
    for i in range(len(rep)):
        if(rep[i] == 1):
            lst.append(twoWayMapper(i))
    status=[]
    for i in range(3):
        corr = maxCorr(lst, flag)
        if(corr[0]==None):
            break
        if(corr[0]>0.4):
            ask.append(corr[1])
            flag[twoWayMapper(corr[1])] = 1
            status.append(1)
        else:
            flag[twoWayMapper(corr[1])] = 1
            status.append(0)
    if(sum(status)<2):
        status='diagnosed'
    else:
        status='active'
    res={'question':ask,'rep':rep,'flag':flag,'status':status}
    return res

def removeExtra(lst):
    dict1={}
    for item in lst:
        count=0
        for i in lst:
            if(i==item):
                count+=1
        dict1[item]=count
    lst=[]
    for key,value in dict1.items():
        if(value>1):
            lst.append(key)
    return lst

def train_model(model,X_train,X_test,Y_train,Y_test):
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    score = accuracy_score(Y_test, prediction)
    return score


def predict(a):
    model = load('filename.joblib')
    lst=[]
    for i in model:
        lst.append(i.predict([a])[0])
    lst=removeExtra(lst)
    return lst
