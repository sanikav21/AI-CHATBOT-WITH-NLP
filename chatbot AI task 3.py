import nltk   #NLTK=nATURAL LANGUAGE Toolkit.(For processing human laguage.)
import random   # To choose random responses.
import string   # tO HANDLE PUNCTUATIONS LILKE ".",",","?",ETC.
from nltk.corpus import wordnet   # Used for word definition
from nltk.stem import WordNetLemmatizer  # To reduce words to their base form
from nltk.tokenize import word_tokenize # To split text into individual words

#Download the required NLTK data-
nltk.download('punkt') # Tokenizer models
nltk.download('wordnet') # WordNet corpus for lemmatization


# define all intents and response in one dictionary each 
intents ={
    "greetings":["hello","hi","hey","good morning","good evening","namaste"],
    "thanks":["Thank you","thanks","thx","much appreciated","thanks a lot"],
    "help":["help","need help","assist me"],
    "movie":["recommend a movie","best movie?","your favourite movie?"],
    "food": ["what is your favourite food?","do you eat?","what should i eat today?"],
    "hobby":["what are your hobbies?","what do you like?"],
}

# Define possible responses for each intent
responses ={
    "greetings":["Hello!","Hii there!","Hey!","Greetings!","Good Morning"],
    "thanks":["You're Welcome","Anytime","Glade to help!","No problem","My pleasure!"],
    "help":["Sure, how can I help you?","I am here to help you!","Let me know your issue."],
    "movie":["I love sci-fi like Interstellar!"],
    "food":["i don't eat, but I have heard pizza is awesome"],
    "hobby":["I love chatting,learning, and helping people like you"]
}
  
#Initialize lemmatizer
lemmatizer = WordNetLemmatizer() #converts words to their base form like "running"-> "run"

#Preprocess text : lowercase, remove punctuation, lemmatize words
def preprocess(text):
    tokens = word_tokenize(text.lower())   # Convert to lowercase and tokenize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]    # Remove punctuation and lemmatize
    return tokens

#Match user input to an intent
def match_intent(user_input):
    processed_input = preprocess(user_input) # Clean and tokenize user input
    
     # Iterate through each intent and its list of trigger phrases
    for intent, phrases in intents.items():
        for phrase in phrases:
            processed_phrase = preprocess(phrase)  # Clean and tokenize each phrase
           
            # If any word in the phrase matches user input, return that intent
            if any(word in processed_input for word in processed_phrase):
                return intent
    return None        # Return None if no intent matches

#Start the Chatbot
print("ChatBot: Hello! Type 'quit' to exit.")   # Welcome message

while True:
    user_input  = input("You: ")  # Take input from user

    if user_input.lower() == "quit":  # Exit condition
        print("ChatBot: Goodbye!")
        break

    intent = match_intent(user_input)   # Try to find matching intent
    if intent:
        print("ChatBot:", random.choice(responses[intent])) # If found, reply with random response

    else:
        print("ChatBot:Sorry,I didn't understand that.") # Default response for unknown inputs
        




