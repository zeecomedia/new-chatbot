from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import random
# from random import choice
import wikipedia
import re
# from PyDictionary import PyDictionary




def Educationmenu(req):  #wikipedia
    return wikipedia.summary(req)
    

def Googlemenu(req):
    url = f"https://www.google.com/search?q={req}"
    # make a request to the website
    HTML = requests.get(url)
    # parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # find the current price
    texti = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).text
    return texti




def QuotationCheck(req):
    match = re.findall(r'"(.+?)"', req)
    return match



def index(request):
    
    return render(request,"index.html")

  

Greeting_inputs = ["hello", "hi", "greetings", "sup", "What's up?", "hey","how are you?","how are you"]

Greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello","I am glad! You are talking to me"]

query_keywords = ["when", "what", "how", "where", "who", "why"]

                      

def rand_greeting():
    return random.choice(Greeting_responses)



def option_rockb_validate(req):
    result = ''
    querying_list = QuotationCheck(req)
    if req == "thanks":
        result =  "Good to hear that..."
    elif req in Greeting_inputs:
        result = rand_greeting()
    elif query_keywords:
        if querying_list:
            result = Googlemenu(req)   #####
        else:
            result = Educationmenu(req)
    else:
        result = 'I dont understand...'
        
    return result




def endpoint(request):
    req = request.GET.get('query')
    converted_word = req.lower()
    
    result = option_rockb_validate(converted_word)
     
    # print(result)
    return JsonResponse({"result":result})
  
    