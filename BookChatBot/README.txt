Colin Lambe
This is the implementation of my final project idea: a literature chatbot

all_books.json contains the meta data for all scraped books
all_reviews.json contains the raw reviews for all scraped books
cleaned_reviews.json contains the summarized reveiws for all scrapped books
organized by book

to run the program run ChatBot_main.py

the brains of the operation are in Bot.py and tfidTest.py

Bot.py processes the user input and tries to figure out the best
type of response

tfidTest.py contains the functionality to find the most similar review to the
user input to output as a response
