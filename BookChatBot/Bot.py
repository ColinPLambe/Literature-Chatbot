"""
This is the brains of the chatbot itself
"""
import re
import random
import json
import tfidTest


with open('cleaned_reviews.json') as revs:
    reviews = json.load(revs)

with open('all_books.json') as meta:
    meta_data = json.load(meta)


greetings = ['hi', 'hello', 'greetings', 'hey']
goodbyes = ['bye', 'goodbye', 'farewell', 'cya']


def get_response(input):
    if(greeting(input)):
        response = greeting_response()
    elif(goodbye(input)):
        response = goodbye_response()
    else:
        response = get_intent(input)
    return response


def greeting(input):
    input = input.lower()
    for word in greetings:
        if word == input.strip():
            return True
    return False

def greeting_response():
    return random.choice(greetings) + " what do you want to talk about?"

def goodbye(input):
    input = input.lower()
    for word in goodbyes:
        if word in input:
            return True
    return False

def goodbye_response():
    return random.choice(goodbyes)

def get_intent(input):
    input = input.lower()
    quoted = re.findall(r'".*"', input)
    quoted = [item[1:-1] for item in quoted]

    #some intents should be like simple queries

    # do you like
    if(re.match(r'do you like*', input)):
        if len(quoted) >  0:
            item = quoted[0]
            for data in meta_data:
                if item == data["book_title"].lower():
                    return "I give it a " + str(round((float)(data["average_rating"])) % 5) + " out of 5"
                elif item == data["author"].lower():
                    return "I do! I particularly like " + data["book_title"]
            return f"I'm sorry, I haven't read {item}"
        else:
            return "Sorry, I didn't quite catch that. Try mentioning a book in your input with the format \"book\""

    #favorite
    elif(re.match(r'what\'s your favorite book?', input)):
        return f"I've been liking {random.choice(meta_data)['book_title']} lately"


    #have you read {book, author}
    elif re.match(r'have you read.*', input):
        #item might be an author
        if len(quoted) > 0:
            item = quoted[0]
            for data in meta_data:
                if item == data["book_title"].lower():
                    return "I have, I give it a " + str(round((float)(data["average_rating"])) % 5) + " out of 5"
                elif item == data["author"].lower():
                    return "I have! I particularly like " + data["book_title"]
            return "I don't think I've read that one"
        return "Sorry, I didn't quite catch that. Try mentioning a book in your input with the format \"book\""

    #how many pages is {book}
    elif re.match(r'how many pages is*', input):
        if len(quoted) > 0:
            item = quoted[0]
            for data in meta_data:
                if item == data["book_title"].lower():
                    return item + " is " + str(data["num_pages"]) + " pages long."
            return "I don't think I know that one"
        return "Sorry, I didn't quite catch that. Try mentioning a book in your input with the format \"book\""


    #what genre is {book}
    elif re.match(r'what genre is*', input):
        if len(quoted) > 0:
            item = quoted[0]
            for data in meta_data:
                if item == data["book_title"].lower():
                    return item + " is considered to be in the following genres: "  + str(data["genres"]) + "\n but if you asked me I'd leave call it a " + data["genres"][0]
            return "I don't think I've read that one"
        return "Sorry, I didn't quite catch that. Try mentioning a book in your input with the format \"book\""

    #doesn't match any predefined queries time to get weird
    else:
        #book mentioned
        if len(quoted) > 0:
            for key in reviews.keys():
                if quoted[0] == key.lower():
                    return tfidTest.choose_review(input, reviews[key])
        #book not mentioned
        return "Sorry, I didn't quite catch that. Try mentioning a book in your input with the format \"book\""


