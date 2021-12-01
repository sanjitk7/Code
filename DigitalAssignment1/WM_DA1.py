import re

import nltk
from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize
# nltk.download('punkt')

from spacy.lang.en import English

from tensorflow.keras.preprocessing.text import text_to_word_sequence

from gensim.utils import tokenize
from gensim.summarization.textcleaner import split_sentences

my_text = """
Stephanie Kwolek was an organic chemist, best known for inventing Kevlar in 1965. Kevlar is an immensely strong plastic, first used as a replacement for steel reinforcing strips in racing car tires, and now used in a large number of applications where high strength is required without high weight.

Advertisements

 
Stephanie Louise Kwolek was born in 1923 in Pittsburgh, Pennsylvania, USA. Her father died when she was only 10 years old, but he passed on his interest in science, particularly natural science to his daughter.

Age 23, Kwolek graduated with a degree in chemistry from Margaret Morrison Carnegie College of Carnegie Mellon University. She was quickly recruited to work as a chemist at Dupont Chemicals in Buffalo, NY. Four years later, she moved to Wilmington, Delaware where she spent the remainder of her career with DuPont.

After nine years of research work, Kwolek made her major breakthrough, discovering Kevlar. Her pathway to discovery began a year earlier, when she began looking for a new, lightweight plastic to be used in car tires. The idea was that lighter tires would allow vehicles to enjoy better fuel economy.
Not only did Kevlar find use in tires, its combination of lightness and strength has seen it used in a large variety of protective clothing applications, such as bulletproof vests, which have saved the lives of countless police officers and other people.

Speaking about her discovery, Stephanie Kwolek, “I don’t think there’s anything like saving someone’s life to bring you satisfaction and happiness.”

Stephanie Kwolek died on June 18, 2014, at the age of 90.
"""

# Tokenisation of Sentences and Words

# Word Tokenisation with Python Split()

print("Word Tokenisation thorugh Python split: \n")
python_spit_tokens = my_text.split()
print(python_spit_tokens)

# Sentence Tokenisation with Python Split()

print("\nSentence Tokenisation thorugh Python split: \n")
python_sent_spit_tokens = my_text.split(".")
print(python_sent_spit_tokens)

# Word Tokenisation with Python RegEx

print("\nWord Tokenisation thorugh Python RegEx: \n")
re_word_tokens = re.findall("[\w']+", my_text)
print(re_word_tokens)

# Word Tokenisation with Python RegEx

print("\nSentence Tokenisation thorugh Python RegEx: \n")
re_sent_tokens = re.compile('[.!?] ').split(my_text)
print(re_sent_tokens)


# Word Tokenisatin using NLTK

print("\nWord Tokenisation thorugh NLTKs Library: \n")
print(word_tokenize(my_text))

# Sentence Tokenisatin using NLTK

print("\nSentence Tokenisation thorugh NLTKs Library: \n")
print(sent_tokenize(my_text))


# Tokenisation using Spacy Library
print("\nSentence Tokenisation thorugh SpaCy Library: \n")
nlp = English()
my_text_doc = nlp(my_text)
token_list = []
for token in my_text_doc:
    token_list.append(token.text)
print(token_list)

# Tokenisation using Keras

print("\nWord Tokenisation thorugh Tensorflow Keras: \n")
word_tf_result = text_to_word_sequence(my_text)
print(word_tf_result)

# Word Tokenisation using Gensim
print("\nWord Tokenisation thorugh Gensim: \n")
gensim_words = list(tokenize(my_text))
print(gensim_words)

# Sentence Tokenisation using Gensim
print("\nSentence Tokenisation thorugh Gensim: \n")
gensim_sentences = split_sentences(my_text)
print(gensim_sentences)


#--------------------------------------------#

# Removing Stop Words

from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.tokenize import word_tokenize

print("\n Removing Stop Words:\n")
text_tokens = word_tokenize(my_text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

filtered_sentence = (" ").join(tokens_without_sw)
print(filtered_sentence)

#--------------------------------------------#