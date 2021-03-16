Colin Lambe
This is the implementation of a closed domain literature chatbot

required: all_books.json contains the meta data for all scraped books
required: all_reviews.json contains the raw reviews for all scraped books

I used the scrapper from https://github.com/maria-antoniak/goodreads-scraper to generate these but any data following the same format should work just as well

cleaned_reviews.json contains the summarized reveiws for all scrapped books
organized by book

to run the program run ChatBot_main.py

the brains of the operation are in Bot.py and tfidTest.py

Bot.py processes the user input and tries to figure out the best
type of response

tfidTest.py contains the functionality to find the most similar review to the
user input to output as a response
