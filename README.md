# AI-CHATBOT-WITH-NLP

COMPANY: CODTECH IT SOLUTIONS 

NAME: SANIKA VYAS 

INTERN ID:CT04DN249 

DOMAIN: PYTHON 

DURATION: 4 WEEKS 

MENTOR: NEELA SANTOSH

DESCRIPTION OF CODE:
This Python script builds a basic rule-based chatbot that can respond to a limited set of user inputs using simple Natural Language Processing (NLP) techniques provided by the NLTK (Natural Language Toolkit) library. The chatbot recognizes user intentions—known as intents—such as greetings, asking for help, or talking about movies or food, and provides predefined responses based on those recognized intents. It simulates a conversational interface where users can type inputs and receive meaningful replies in return.

At the beginning of the script, key Python libraries are imported. nltk is the core library for processing natural language. It includes tools for tokenization, lemmatization, and corpus access, which are essential for interpreting human language. The random module is used to randomly select responses from a list of possible replies, ensuring variety in interaction. The string module helps in handling punctuation, which is typically unnecessary in intent recognition. From nltk.corpus, wordnet is imported, which supplies the vocabulary for the lemmatizer, and nltk.tokenize provides word_tokenize for breaking text into individual words. Additionally, WordNetLemmatizer is used to reduce words to their base form (e.g., “running” to “run”), which makes it easier to match user inputs to known phrases.

The script downloads two required datasets from NLTK using nltk.download('punkt') for tokenization and nltk.download('wordnet') for lemmatization support. Without these, the relevant NLP tools wouldn’t function.

Two core dictionaries are defined: intents and responses. The intents dictionary maps high-level user intentions (like greetings or help requests) to a list of possible phrases a user might input to express that intent. For example, the "greetings" intent includes various ways people say hello. The responses dictionary provides a corresponding list of potential chatbot replies for each intent. The chatbot selects one randomly when replying, which adds realism and variety to the interaction.

A lemmatizer instance is initialized using WordNetLemmatizer(), which is later used during the preprocessing stage. The preprocess() function is responsible for preparing the user’s input text before matching. It first converts the input to lowercase to ensure case-insensitive matching. Then it tokenizes the text into individual words using word_tokenize(). It also removes punctuation and lemmatizes each word. This normalization step ensures that variations in input (e.g., “running” vs. “ran”) don’t hinder intent recognition.

The match_intent() function is at the heart of the chatbot’s understanding capability. It processes the user input and compares it with all predefined phrases under each intent. For each phrase associated with an intent, it is also preprocessed. The function then checks if any of the words from the processed phrase appear in the user’s processed input. If a match is found, it returns the corresponding intent. If no match is found, it returns None, indicating the chatbot didn’t understand.

The actual conversation starts with a welcome message printed using print(). Then a while loop runs indefinitely, allowing the user to type messages until they type “quit”, at which point the chatbot politely says goodbye and the loop exits. For each input, the chatbot attempts to match the intent. If it successfully identifies the intent, it selects a random response from the corresponding list in the responses dictionary. If the chatbot is unable to identify the intent, it gives a default response: "Sorry, I didn't understand that."

This chatbot is a beginner-friendly example of how natural language understanding can be implemented in a structured, rule-based manner. It doesn’t use machine learning or deep learning models but still demonstrates fundamental concepts like tokenization, lemmatization, and intent mapping. This type of chatbot is ideal for small-scale applications like educational tools, interactive menus, or FAQ-style help desks. With more data and NLP enhancement, it can be scaled up by adding more intents, using fuzzy matching, or integrating with neural language models.


OUTPUT OF CODE:
