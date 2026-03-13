import nltk
import pandas as pd
import numpy as np
import time,random
import pickle
import re
emotions=['fear','anger','sadness','disgust','shame','guilt']
# get the word lists of sentences
def get_words_in_sentences(sentences):
            all_words = []
            for (words, sentiment) in sentences:
                    all_words.extend(words)
            return all_words

def close(wndw):
        wndw.destroy()

def result(result):
        rs=result
        print(rs[0])
        print("-------------------------")

# get the unique word from the word list	
def get_word_features(wordlist):
            wordlist = nltk.FreqDist(wordlist)
            word_features = wordlist.keys()
            return word_features
def testit(sente_tests):
    train = pd.read_csv("out.csv", header=0, delimiter=",", quoting=1)
    num_reviews = train["statements"].size
    print(num_reviews)
    data = []
    sentiments = []
    global sentences
    sentences = []
   
    for i in range(0, num_reviews):
        # Convert www.* or https?://* to URL
        sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', train["statements"][i])
        # Convert @username to AT_USER
        sente = re.sub('@[^\s]+', '', sente)
        # Remove additional white spaces
        sente = re.sub('[\s]+', ' ', sente)
        # Replace #word with word
        sente = re.sub(r'#([^\s]+)', r'\1', sente)
        # trim
        sente = sente.strip('\'"')
        words_filtereds = [e.lower() for e in sente.split() if len(e) >= 3]
        sentences.append((words_filtereds, train["sentiments"][i]))
    word_features = get_word_features(get_words_in_sentences(sentences))
    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
          features['contains(%s)' % word] = (word in document_words)
        return features
    sents=sente_tests.split("\n")
    print(sents)
    print(len(sents))
    dic=""
    outf=open("data.txt",'w+')
    if len(sente_tests)>2:
    #Convert to lower case
      sente = sente_tests.lower()
      sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',sente)
      sente = re.sub('@[^\s]+','',sente)
    #Remove additional white spaces
      sente = re.sub('[\s]+', ' ', sente)
    #Replace #word with word
      sente = re.sub(r'#([^\s]+)', r'\1', sente)
      sente = sente.strip('\'"')
      f=open("myclass123.pickle",'rb')
      classi=pickle.load(f)
      emot=classi.classify(extract_features(sente.split()))
      print(emot)
      return emot
def mainn():
    train = pd.read_csv("out.csv", header=0,delimiter=",", quoting=1)
    num_reviews = train["statements"].size
    print(num_reviews)
    data=[]
    sentiments=[]
    global sentences
    sentences = []
    for i in range( 0,num_reviews ):
        sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',train["statements"][i])
        sente = re.sub('@[^\s]+','',sente)    
        #Remove additional white spaces
        sente = re.sub('[\s]+', ' ', sente)
        #Replace #word with word
        sente = re.sub(r'#([^\s]+)', r'\1', sente)
        #trim
        sente = sente.strip('\'"')
        words_filtereds = [e.lower() for e in sente.split() if len(e) >= 3]
        sentences.append((words_filtereds,train["sentiments"][i]))

    word_features = get_word_features(get_words_in_sentences(sentences))
    
    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
          features['contains(%s)' % word] = (word in document_words)
        return features
    print(sentences)
##    tkMessageBox.showinfo("Training Completed","Training Completed")
    training_set = nltk.classify.util.apply_features(extract_features, sentences)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    f=open("myclass123.pickle","wb")
    pickle.dump(classifier,f)
    f.close
a=input("Enter text data:\n>")
testit(a)
