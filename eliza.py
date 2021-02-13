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
    if re.match(r"\sI\s", userInput):
        userInput = re.sub(r"\sI\s", " you ", userInput)
    return userInput

def chooseResponse(userInput):
    ## could also change a word's tense before looking for a valid reponse, i.e. cried -> cry
    if (re.search("feeling (.+)", userInput)):
        match = re.search("feeling (.+)", userInput)
        print("[SYBIL]: Why are you feeling {}?".format(match.group(1)))
    elif (re.search("feel (.+)", userInput)):
        match = re.search("feel (.+)", userInput)
        print("[SYBIL]: Why do you feel {}?".format(match.group(1)))
    elif (re.search("want to (.+)", userInput)):
        match = re.search("want to (.+)", userInput)
        print("[SYBIL]: {}, Why do you want to {}?".format(userName, match.group(1)))
    elif (re.search("(B|b)ecause my (.+)", userInput)):
        match = re.search("(B|b)ecause my (.+)", userInput)
        print("[SYBIL]: {}, Why did your {}?".format(userName, match.group(2)))
    elif (re.search("I need (.+)", userInput)):
        #userInput = changeWords(userInput)
        match = re.search("I need (.+)", userInput)
        print("[SYBIL]: Why do you need {}, {}?".format(match.group(1), userName))
    elif (re.search("I think (.+)", userInput)):
        match = re.search("I think (.+)", userInput)
        print("[SYBIL]: Why do you think {}, {}?".format(match.group(1), userName))
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

