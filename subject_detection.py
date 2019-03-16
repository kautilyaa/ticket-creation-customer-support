import nltk
import csv
import random

subjects = ["Baggage Related" ,"Staff Related" ,"Special Assistance" ,"Announcements" ,"Food" ,"Booking Issues" ,"Fare" ,"Website" ,"Delays OR Cancellation" ,"Call Center" ,"Refund","Payment Failure" ,"New Train Request" ,"Request Documents" ,"Tatkaal" ,"Station" ,"Train Details" ,"Train Service"]
important_words = ['lost', 'bag', 'misbehaviour', 'misconduct', 'misplace', 'find', 'rude', 'absent', 'behaviour', 'good', 'joyful', 'wheelchair', 'handicapped', 'senior', 'porter', 'cooli', 'tasty', 'food', 'access', 'failure', 'payment', 'cheap', 'expensive', 'high', 'fares', 'helpful', 'irritated', 'tatkaal', 'urgent', 'tidy', 'dirty', 'clean', 'infrastructure', 'busy', 'wifi', 'wi-fi', 'customer', 'care', 'call', 'disconnects', 'disconnected']

# SUBJECT EXTRACTION
def subject_feature(email):
    subject, body = email['subject'], email['body']
    sub_words, body_words = nltk.word_tokenize(subject.lower()), nltk.word_tokenize(body.lower())
    result = {}

    for word in important_words:
        result['has({})'.format(word)] = word in sub_words or word in body_words

    return result    

# GETTING TRAINING DATA
csv_filename = 'RPA_DATASET.csv'
csv_file = open(csv_filename, mode='r')
train_set = []
for row in list(csv.DictReader(csv_file)):
    train_set.append(({'body':row['Body (FROM MAIL)'], 'subject':row['Subject (FROM MAIL)']}, row['REGARDING']))
csv_file.close()

feature_set = [(subject_feature(email), categ) for (email, categ) in train_set]
random.shuffle(feature_set)
subject_classifier = nltk.classify.NaiveBayesClassifier.train(feature_set)
