#Importing required libraries

from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

#Loading the breast cancer data

data = load_breast_cancer()
print('Classes to predict: ', data.target_names)
print('Classes to predict: ', data.feature_names)


X = data.data

y = data.target

print('Number of examples in the data:', X.shape)

print(X[:4])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 77, train_size = 0.8)

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

y_pred =  clf.predict(X_test)

from sklearn.metrics import accuracy_score
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train))*100)
print('Accuracy Score on test data: ', accuracy_score(y_true=y_test, y_pred=y_pred)*100)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf.fit(X_train, y_train)
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train))*100)
print('Accuracy Score on the test data: ', accuracy_score(y_true=y_test, y_pred=clf.predict(X_test))*100)
