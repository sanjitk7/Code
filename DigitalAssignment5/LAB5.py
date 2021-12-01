import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, auc, roc_auc_score, roc_curve
from sklearn.metrics import recall_score, precision_score, accuracy_score, f1_score
from sklearn.naive_bayes import GaussianNB
df = pd.read_csv("./creditcard.csv")
print(df.shape)
print(df.describe())


def split_data(df, drop_list):
    df = df.drop(drop_list, axis=1)
    print(df.columns)
    # test train split time
    from sklearn.model_selection import train_test_split
    y = df['Class'].values  # target
    X = df.drop(['Class'], axis=1).values  # features
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42, stratify=y)
    print("train-set size: ", len(y_train),
          "\ntest-set size: ", len(y_test))
    print("fraud cases in test-set: ", sum(y_test))
    return X_train, X_test, y_train, y_test


def get_predictions(clf, X_train, y_train, X_test):
    # create classifier
    clf = clf
    # fit it to training data
    clf.fit(X_train, y_train)
    # predict using test data
    y_pred = clf.predict(X_test)
    # Compute predicted probabilities: y_pred_prob
    y_pred_prob = clf.predict_proba(X_test)
    # for fun: train-set predictions
    train_pred = clf.predict(X_train)
    print('train-set confusion matrix:\n',
          confusion_matrix(y_train, train_pred))
    return y_pred, y_pred_prob


def print_scores(y_test, y_pred, y_pred_prob):
    print('test-set confusion matrix:\n', confusion_matrix(y_test, y_pred))
    print("recall score: ", recall_score(y_test, y_pred))
    print("precision score: ", precision_score(y_test, y_pred))
    print("f1 score: ", f1_score(y_test, y_pred))
    print("accuracy score: ", accuracy_score(y_test, y_pred))
    print("ROC AUC: {}".format(roc_auc_score(y_test, y_pred_prob[:, 1])))

drop_list = []
X_train, X_test, y_train, y_test = split_data(df, drop_list)
y_pred, y_pred_prob = get_predictions(GaussianNB(), X_train, y_train, X_test)
print_scores(y_test,y_pred,y_pred_prob)
false_positive_rate, true_positive_rate, thresolds = roc_curve(y_test,y_pred)

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