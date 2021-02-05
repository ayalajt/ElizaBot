import re
import time

# Can possibly making enums such as FEELINGS to keep track of all possible emotions
# Can possibly call another function that picks a correct question from the given input

infiniteLoop = True

def chooseResponse(userInput):
    if (re.search("feeling", userInput)):
        print("[SYBIL]: Why are you feeling sad")

def checkQuit(userInput):
     if re.match("quit", userInput):
            print("[SYBIL]: Goodbye!")
            return True

def main():
    global infiniteLoop
    introChat = False
    while infiniteLoop:
        if introChat == False:
            print("[SYBIL]: Hello! My name is Sybil. What's your name?") 
            userInput = input("[USER]: ")
            if checkQuit(userInput): break
            if re.match("^[A-Za-z]*$", userInput):
                userName = userInput
                print('[SYBIL]: Nice to meet you {}!'.format(userName))
                time.sleep(1)
                print('[SYBIL]: What brings you here today {}?'.format(userName))
                introChat = True
            else:
                print("[SYBIL]: Please input a valid name.")
        # After intro has played
        userInput = input("[{}]: ".format(userName.upper()))
        if checkQuit(userInput): break
        chooseResponse(userInput)

if __name__ == '__main__':
    main()

