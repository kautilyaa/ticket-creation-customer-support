import nltk
import csv
import re
import random

important_words = ['kudos', 'love', 'commending', 'great', 'nice' ,'congratulate', 'good', 'bad', 'super', 'cool', 'angry', 'sad', 'expectations', 'improve', 'know', 'suggest', 'improve', 'happy', 'commendable', 'recommend', 'awesome', 'applaudable', 'appreciate', 'glad']
categories = ['appreciation', 'suggestion', 'complaint', 'request', 'enquiry']
important_words += categories

def categorize_feature(email):
    subject, body = email['subject'], email['body']
    sub_words, body_words = nltk.word_tokenize(subject.lower()), nltk.word_tokenize(body.lower())
    result = {}

    for word in important_words:
        result['mail_has({})'.format(word)] = word.lower() in sub_words or word.lower() in body_words

    for category in sub_words:
        if (category in categories):
            result['guessed_categ'] = category

    return result

# GETTING TRAINING DATA
csv_filename = 'RPA_DATASET.csv'
csv_file = open(csv_filename, mode='r')
train_set = []
for row in list(csv.DictReader(csv_file)):
    train_set.append(({'body':row['Body (FROM MAIL)'], 'subject':row['Subject (FROM MAIL)']}, row['CATEGORY']))
csv_file.close()

# GENERATING TRAINING SET AND TRAINING

feature_set = [(categorize_feature(email), categ) for (email, categ) in train_set]
random.shuffle(feature_set)
category_classifier = nltk.classify.NaiveBayesClassifier.train(feature_set)

