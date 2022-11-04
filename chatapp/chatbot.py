import nltk
import numpy as np
import random
import string
import warnings
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer


f = open('chatapp/Poem.txt', 'r', errors = 'ignore')
raw_data = f.read()
raw_data = raw_data.lower()


warnings.filterwarnings("ignore")


nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_data)
word_tokens = nltk.word_tokenize(raw_data)


sent_tokens = nltk.sent_tokenize(raw_data)
word_tokens = nltk.word_tokenize(raw_data)

f.close()

lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Greeting_inputs = ("hello", "hi", "greetings", "sup", "What's up", "hey","how are you")

Greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello", 
                      "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in Greeting_inputs:
            return random.choice(Greeting_responses)
    
  



def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    google_keywords = ["how","what","when","which"]
    
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    
    elif(user_response in google_keywords):
        robo_response=robo_response+"I am searching it out!"
        return robo_response
        
    else:
        robo_response = robo_response+sent_tokens[idx]   #INSERT YOUR GOOGLE CODE HERE!!!
        return robo_response
    


# print("ABY ChatBot: \nMy name is ABY. \nI am a conversational Bot.")
      
