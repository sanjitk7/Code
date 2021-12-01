import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

hindustan_times_text = """
On Saturday, October 2, 2021, the nation will pay homage to Mahatma Gandhi on what will be the 152nd birth anniversary of the Father of the Nation. Gandhi Jayanti, as the occasion is known, coincides this year with the Azadi Ka Amrit Mahotsav, which was inaugurated on March 12 by prime minister Narendra Modi, on the 91st anniversary of a significant event in Gandhi's life, the Dandi March.
"""
indian_express_text = """
Every year, Gandhi Jayanti is celebrated on October 2 to mark the birth anniversary of Mohandas Karamchand Gandhi, popularly known as Mahatma Gandhi. Observed across the nation, the day is also a national holiday.
Mahatma Gandhi was born on October 2, 1869, in Porbandar, Gujarat, and this year marks his 152nd birth anniversary.
"""
ndtv_text = """
India will mark the 152nd birth anniversary of Mahatma Gandhi on October 2, this year. Fondly remembered by people across the world as “Mahatma” or “Bapu”, Mohandas Karamchand Gandhi was born in Porbandar, Gujarat. Gandhi Jayanti is a national holiday. People celebrate the life and contributions of the great leader on October 2. The day is also celebrated as “International Day of Non-Violence” every year to honour Mahatma Gandhi's path of ahimsa (non-violence) during the Indian freedom struggle.
"""

docs = [hindustan_times_text, indian_express_text, ndtv_text]

# Creating TF-IDF Matrix for the 3 Documents
cv = CountVectorizer()

word_count = cv.fit(docs)
word_count_vector = cv.transform(docs)

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True) 
tfidf_transformer.fit(word_count_vector)

df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"]) 
df_idf.sort_values(by=['idf_weights'])
count_vector=cv.transform(docs) 
tf_idf_vector=tfidf_transformer.transform(count_vector)

feature_names = cv.get_feature_names()
first_document_vector=tf_idf_vector[0] 
df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"]) 
df.sort_values(by=["tfidf"],ascending=False)
print("\nTFIDF for Documents' Text:\n")
print(df)

# Calculating Similarity between the 3 Documents

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def create_dataframe(matrix, tokens):
    doc_names = ["hindustan_times_text","indian_express_text","ndtv_text"]
    df = pd.DataFrame(data=matrix, index=doc_names, columns=tokens)
    return(df)


print("\n Calculating COSINE Similarity:\n")

count_vectorizer = CountVectorizer()
vector_matrix = count_vectorizer.fit_transform(docs)
tokens = count_vectorizer.get_feature_names()

create_dataframe(vector_matrix.toarray(),tokens)

cosine_similarity_matrix = cosine_similarity(vector_matrix)
print(create_dataframe(cosine_similarity_matrix,['hindustan_times_text','indian_express_text',"ndtv_text"]))