from sklearn import naive_bayes
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



dataset = datasets.load_wine()
X = dataset.data
y = dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = naive_bayes.GaussianNB()
model.fit(X_train, y_train)
print(model)
expected_y = y_test
predicted_y = model.predict(X_test)
print(metrics.classification_report(expected_y, predicted_y,target_names=dataset.target_names))
print(metrics.confusion_matrix(expected_y, predicted_y))

false_positive_rate, true_positive_rate, thresolds = metrics.roc_curve(expected_y,predicted_y)


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