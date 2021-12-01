
# Gaussian Naive Bayes
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
import nltk
import pandas as pd
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
# -----------------------------------------------------------------------------#

df = pd.read_table('C:/Users/Admin/Desktop/SMS',
                   sep='\t',
                   header=None,
                   names=['label', 'message'])

df['label'] = df.label.map({'ham': 0, 'spam': 1})
df['message'] = df.message.map(lambda x: x.lower())
df['message'] = df.message.str.replace('[^\w\s]', '')

nltk.download()

df['message'] = df['message'].apply(nltk.word_tokenize)
stemmer = PorterStemmer()
df['message'] = df['message'].apply(lambda x: [stemmer.stem(y) for y in x])

df['message'] = df['message'].apply(lambda x: ' '.join(x))
count_vect = CountVectorizer()
counts = count_vect.fit_transform(df['message'])
transformer = TfidfTransformer().fit(counts)
counts = transformer.transform(counts)
X_train, X_test, y_train, y_test = train_test_split(
    counts, df['label'], test_size=0.1, random_state=69)

model = MultinomialNB().fit(X_train, y_train)

predicted = model.predict(X_test)
print(np.mean(predicted == y_test))


print(confusion_matrix(y_test, predicted))

print(metrics.classification_report(y_test, predicted))
