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
    # sorted by precedence
    randomChoice = -1
    ## could also change a word's tense before looking for a valid reponse, i.e. cried -> cry
    if (re.search(r"I am feeling ([A-za-z\s]*)", userInput)):
        match = re.search(r"I am feeling ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Why are you feeling {}?".format(match.group(1)))

    elif (re.search(r"I feel ([A-za-z\s]*)", userInput)):
        match = re.search(r"I feel ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Why do you feel {}?".format(match.group(1)))

    elif (re.search(r"I want to ([A-za-z\s]*)", userInput)):
        match = re.search(r"I want to ([A-za-z\s]*)", userInput)
        print("[SYBIL]: {}, why do you want to {}?".format(userName, match.group(1)))

    elif (re.search(r"Because my ([A-za-z\s]*)", userInput)):
        match = re.search(r"Because my ([A-za-z\s]*)", userInput)
        print("[SYBIL]: {}, Why did your {}?".format(userName, match.group(1)))

    elif (re.search(r"I need ([A-za-z\s]*)", userInput)):
        #newUserInput = changeWords(userInput)
        match = re.search(r"I need ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Why do you need {}, {}?".format(match.group(1), userName))

    elif (re.search(r"I think ([A-za-z\s]*)", userInput)):
        match = re.search(r"I think ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Why do you think {}, {}?".format(match.group(1), userName))

    elif (re.search(r"(A|a)re you ([A-za-z\s]*)", userInput)):
        match = re.search(r"(A|a)re you ([A-za-z\s]*)", userInput)
        print("[SYBIL]: It's possible that I am {}, who knows?".format(match.group(2)))

    elif (re.search(r"(Y|y)ou ([A-za-z\s]*)", userInput)):
        match = re.search(r"You ([A-za-z\s]*)", userInput)
        print("[SYBIL]: {}, let's focus on you and not me.".format(userName))

    elif (re.search(r"(I am|I'm) ([A-za-z\s]*)", userInput)):
        match = re.search(r"(I am|I'm) ([A-za-z\s]*)", userInput)
        print("[SYBIL]: How does being {} make you feel?".format(match.group(2)))

    elif (re.search(r"(.+) mother ([A-za-z\s]*)", userInput)):
        match = re.search(r"(.+) mother ([A-za-z\s]*)", userInput)
        print("[SYBIL]: How does your mother make you feel?")

    elif (re.search(r"(.+) father ([A-za-z\s]*)", userInput)):
        match = re.search(r"(.+) father ([A-za-z\s]*)", userInput)
        print("[SYBIL]: How do you feel about your father, {}?".format(userName))

    elif (re.search(r"(.+) family ([A-za-z\s]*)", userInput)):
        match = re.search(r"(.+) family ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Tell me more about your family, {}.".format(userName))

    elif (re.search(r"makes me ([A-za-z\s]*)", userInput)):
        match = re.search(r"makes me ([A-za-z\s]*)", userInput)
        print("[SYBIL]: {}, why does it make you {}?".format(userName, match.group(1)))

    elif (re.search(r"I can't ([A-za-z\s]*)", userInput)):
        match = re.search(r"I can't ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Are you sure you can't {}, {}?".format(match.group(1), userName))

    elif (re.search(r"((H|h)ello|(H|h)i) ([A-za-z\s]*)", userInput)):
        print("[SYBIL]: Hello to you too {}.".format(userName))

    elif (re.search(r"(W|w)hy don't you ([A-za-z\s]*)", userInput)):
        match = re.search(r"(W|w)hy don't you ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Are you sure you want me to {}?".format(match.group(1)))

    elif (re.search(r"(W|w)hy can't I ([A-za-z\s]*)", userInput)):
        match = re.search(r"(W|w)hy can't I ([A-za-z\s]*)", userInput)
        print("[SYBIL]: Are you sure you can't {}?".format(match.group(1)))

    elif(re.search(r"How ([A-za-z\s]*)\?", userInput)):
        print("[SYBIL]: How do you suppose?")

    elif(re.search(r"What ([A-za-z\s]*)\?", userInput)):
        randomChoice = random.randint(1,2)
        if randomChoice == 1: print("[SYBIL]: How would an answer to that question make you feel?")
        if randomChoice == 2: print("[SYBIL]: {}, what do you think the answer to that is?".format(userName))

    elif (re.search(r"(.+) sorry ([A-za-z\s]*)", userInput)):
        print("[SYBIL]: {}, How does apologizing make you feel?".format(userName))

    else:
        randomChoice = random.randint(1,5)
        if randomChoice == 1: print("[SYBIL]: Please, tell me more.")
        if randomChoice == 2: print("[SYBIL]: Could you explain some more?")
        if randomChoice == 3: print("[SYBIL]: Please, could you elaborate some more?")
        if randomChoice == 4: print("[SYBIL]: Is there more to that?")
        if randomChoice == 5: print("[SYBIL]: Why do you say that?")
       
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

