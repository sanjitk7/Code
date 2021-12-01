#Importing required libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

#Loading the iris data

data = load_iris()
print('Classes to predict: ', data.target_names)
print('Classes to predict: ', data.feature_names)


#Extracting data attributes

X = data.data

#Extracting target/ class labels

y = data.target

print('Number of examples in the data:', X.shape)

#First four rows in the variable 'X'

print(X[:4])

#Using the train_test_split to create train and test sets.

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = 0.8)

#Importing the Decision tree classifier from the sklearn library.
#from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

#Training the decision tree classifier. 

clf.fit(X_train, y_train)

#Predicting labels on the test set.

y_pred =  clf.predict(X_test)

#Importing the accuracy metric from sklearn.metrics library

from sklearn.metrics import accuracy_score
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train))*100)
print('Accuracy Score on test data: ', accuracy_score(y_true=y_test, y_pred=y_pred)*100)


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#Next, we will tune the parameters of the decision tree to increase its accuracy.
#One of those parameters is 'min_samples_split', which is the minimum number of samples required to split an internal node. 
#Its default value is equal to 2 because we cannot split on a node containing only one example/ sample.

clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf.fit(X_train, y_train)
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train))*100)
print('Accuracy Score on the test data: ', accuracy_score(y_true=y_test, y_pred=clf.predict(X_test))*100)


false_positive_rate, true_positive_rate, thresolds = metrics.roc_curve(y_test,y_pred)


plt.figure(figsize=(10, 8), dpi=100)
plt.axis('scaled')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.title("AUC & ROC Curve")
plt.plot(false_positive_rate, true_positive_rate, 'r')
plt.fill_between(false_positive_rate, true_positive_rate,facecolor='pink', alpha=0.7)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()