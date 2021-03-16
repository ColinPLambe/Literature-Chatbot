"""
The driver for the literature chatbot program
"""
import Bot



def main():
    print("Hi, I'm LitBot")
    #start conversation
    response = ""
    while (True):
        response = Bot.get_response(input(">you: "))
        print("LitBot: ", response)

if __name__ == "__main__":
    main()
