import re
import time
import random

# Can possibly making enums such as FEELINGS to keep track of all possible emotions
# Can possibly call another function that picks a correct question from the given input

infiniteLoop = True
introChat = False
toQuit = False
userName = "null"

def changeWords(userInput):
    if re.match("^I ", userInput):
        userInput = re.sub("^I ", "you ", userInput)
    if re.match("I", userInput):
        userInput = re.sub("I", "you", userInput)
    print(userInput)
    return userInput

def chooseResponse(userInput):
    randomChoiceNum = 1
    ## could also change a word's tense before looking for a valid reponse, i.e. cried -> cry
    if (re.search("I am feeling (.+)", userInput)):
        match = re.search("I am feeling (.+)", userInput)
        print("[SYBIL]: Why are you feeling {}?".format(match.group(1)))

    elif (re.search("I feel (.+)", userInput)):
        match = re.search("I feel (.+)", userInput)
        print("[SYBIL]: Why do you feel {}?".format(match.group(1)))

    elif (re.search("I want to (.+)", userInput)):
        match = re.search("I want to (.+)", userInput)
        print("[SYBIL]: {}, why do you want to {}?".format(userName, match.group(1)))

    elif (re.search("Because my (.+)", userInput)):
        match = re.search("Because my (.+)", userInput)
        print("[SYBIL]: {}, Why did your {}?".format(userName, match.group(1)))

    elif (re.search("I need (.+)", userInput)):
        #newUserInput = changeWords(userInput)
        match = re.search("I need (.+)", userInput)
        print("[SYBIL]: Why do you need {}, {}?".format(match.group(1), userName))

    elif (re.search("I think (.+)", userInput)):
        match = re.search("I think (.+)", userInput)
        print("[SYBIL]: Why do you think {}, {}?".format(match.group(1), userName))

    elif (re.search("You (.+)", userInput)):
        match = re.search("You (.+)", userInput)
        print("[SYBIL]: {}, let's focus on you and not me.".format(userName))

    elif (re.search("(.+) mother (.+)", userInput)):
        match = re.search("(.+) mother (.+)", userInput)
        print("[SYBIL]: How does your mother make you feel?")

    elif (re.search("(.+) father (.+)", userInput)):
        match = re.search("(.+) father (.+)", userInput)
        print("[SYBIL]: How do you feel about your father, {}?".format(userName))

    elif (re.search("makes me (.+)", userInput)):
        match = re.search("makes me (.+)", userInput)
        print("[SYBIL]: {}, why does it make you {}?".format(userName, match.group(1)))

    elif (re.search("I can't (.+)", userInput)):
        match = re.search("I can't (.+)", userInput)
        print("[SYBIL]: Are you sure you can't {}, {}?".format(match.group(1), userName))

    elif (re.search("((H|h)ello|(H|h)i) (.+)", userInput)):
        print("[SYBIL]: Hello to you too, {}.".format(userName))

    else:
        randomChoiceNum = random.randint(1,5)
        if randomChoiceNum == 1:
            print("[SYBIL]: Please, tell me more.")
        if randomChoiceNum == 2: 
            print("[SYBIL]: Could you explain some more?")
        if randomChoiceNum == 3:
            print("[SYBIL]: Please, could you elaborate some more?")
        if randomChoiceNum == 4:
            print("[SYBIL]: Is there more to that?")
        if randomChoiceNum == 5:
            print("[SYBIL]: Why do you say that?")
       
def checkQuit(userInput):
     if re.match("quit", userInput):
            print("[SYBIL]: Goodbye!")
            quit()

def introText(userInput):
    # need to figure out how to quit from here
    return True

def main():
    global infiniteLoop
    global userName
    introChat = False
    while infiniteLoop:
        while introChat == False:
            print("[SYBIL]: Hello! I am Sybil, a psychotherapist. What's your name?") 
            userInput = input("[USER]: ")
            checkQuit(userInput)
            if re.match(r"My (N|n)ame is ([A-Za-z]+)(\.*)", userInput):
                userName = re.search(r"My (N|n)ame is ([A-Za-z]+)(\.*)", userInput)
                userName = userName.group(2)
                print('[SYBIL]: Nice to meet you {}! What brings you here today?'.format(userName))
                introChat = True
            else:
                if re.match("^[A-Za-z]*$", userInput):
                    userName = userInput
                    print('[SYBIL]: Nice to meet you {}! What brings you here today?'.format(userName))
                    introChat = True
                else:
                    print("[SYBIL]: Please input a valid name.")

        # After intro has played
    
        userInput = input("[{}]: ".format(userName.upper()))
        checkQuit(userInput)
        chooseResponse(userInput)

if __name__ == '__main__':
    main()

