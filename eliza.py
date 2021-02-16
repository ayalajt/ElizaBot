import re
import time
import random

# Can possibly making enums such as FEELINGS to keep track of all possible emotions
# Can possibly call another function that picks a correct question from the given input

infiniteLoop = True
introChat = False
userName = "null"

def chooseResponse(userInput):
    global userName
    # sorted by precedence
    randomChoice = -1
    ## could also change a word's tense before looking for a valid reponse, i.e. cried -> cry
    if (re.search(r"I am feeling ([A-za-z\s]*)", userInput)):
        match = re.search(r"I am feeling ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why are you feeling {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How come you are feeling {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Tell me more about why you feel {}, {}.".format(match.group(1), userName))

    elif (re.search(r"I feel ([A-za-z\s]*)", userInput)):
        match = re.search(r"I feel ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you feel {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How come you feel {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: {}, could you explain why you feel {}?".format(userName, match.group(1)))

    elif (re.search(r"I want to ([A-za-z\s]*)", userInput)):
        match = re.search(r"I want to ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, why do you want to {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How would you feel if you got to {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Are you sure you want to {}?".format(match.group(1)))

    elif (re.search(r"Because my ([A-za-z\s]*)", userInput)):
        match = re.search(r"Because my ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you certain that is the reason?")
        if randomChoice == 2: print("[SYBIL]: What else could be the reason?")
        if randomChoice == 3: print("[SYBIL]: {}, are you happy with that?".format(userName))

    elif (re.search(r"I need ([A-za-z\s]*)", userInput)):
        match = re.search(r"I need ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you need {}, {}?".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: How would you feel if you got {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: {}, are you sure that you need {}?".format(userName, match.group(1)))

    # Specific think case 1
    elif (re.search(r"I think I ([A-za-z\s]*)", userInput)):
        match = re.search(r"I think I ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you think you {}, {}?".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: How come you think you {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: {}, what makes you think you {}?".format(userName, match.group(1)))

    # Specific think case 2
    elif (re.search(r"I think (I'm|i'm|I am|i am) ([A-za-z\s]*)", userInput)):
        match = re.search(r"I think (I'm|i'm|I am|i am) ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you think you're {}, {}?".format(match.group(2), userName))
        if randomChoice == 2: print("[SYBIL]: How come you think you're {}?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: {}, what makes you think you're {}?".format(userName, match.group(2)))

    # general think case
    elif (re.search(r"I think ([A-za-z\s]*)", userInput)):
        randomChoice = random.randint(1,4)
        if randomChoice == 1: print("[SYBIL]: Are you certain, {}?".format(userName))
        if randomChoice == 2: print("[SYBIL]: Why do you think that?")
        if randomChoice == 3: print("[SYBIL]: You sound uncertain. Why's that?")
        if randomChoice == 4: print("[SYBIL]: {}, what makes you think that?".format(userName))

    elif (re.search(r"(A|a)re you ([A-za-z\s]*)", userInput)):
        match = re.search(r"(A|a)re you ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: It's possible that I am {}, who knows?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: I could be, but does it matter?")
        if randomChoice == 3: print("[SYBIL]: Let's focus on you, {}, and not me.".format(userName))

    elif (re.search(r"(Y|y)ou ([A-za-z\s]*)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, let's focus on you and not me.".format(userName))
        if randomChoice == 2: print("[SYBIL]: We're here for you, {}, let's not focus on me.".format(userName))
        if randomChoice == 3: print("[SYBIL]: I would love to talk about myself but we're here for you, {}.".format(userName))

    elif (re.search(r"(I am|I'm) ([A-za-z\s]*)", userInput)):
        match = re.search(r"(I am|I'm) ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How does being {} make you feel?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: Why are you {}?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: Does being {} make you feel any specific way?".format(match.group(2)))

    elif (re.search(r"((M|m)other|(M|m)om)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How does your mother make you feel?")
        if randomChoice == 2: print("[SYBIL]: {}, how is your relationship with your mother?".format(userName))
        if randomChoice == 3: print("[SYBIL]: How do you feel in regards to your mother, {}?".format(userName))

    elif (re.search(r"((F|f)ather|(D|d)ad)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How do you feel about your father, {}?".format(userName))
        if randomChoice == 2: print("[SYBIL]: {}, How would you describe your relatinship with your father?".format(userName))
        if randomChoice == 3: print("[SYBIL]: Do you feel a specific way about your father?")

    elif (re.search(r"(F|f)amily", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Tell me more about your family, {}.".format(userName))
        if randomChoice == 2: print("[SYBIL]: {}, how do you feel about your family?".format(userName))
        if randomChoice == 3: print("[SYBIL]: How does your family make you feel, {}?".format(userName))

    elif (re.search(r"makes me ([A-za-z\s]*)", userInput)):
        match = re.search(r"makes me ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, why does it make you {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How come it makes you {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Are you sure it makes you {}?".format(match.group(1)))

    elif (re.search(r"I can't ([A-za-z\s]*)", userInput)):
        match = re.search(r"I can't ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you certain you can't {}, {}?".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: What makes you think you can't {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Why do you feel uncertain?")

    elif (re.search(r"(W|w)hy can't I ([A-za-z\s]*)", userInput)):
        match = re.search(r"(W|w)hy can't I ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, are you sure you can't {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: Why do you think you can't {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: What makes you think you can't. {}?".format(userName))

    elif (re.search(r"(W|w)hy don't you ([A-za-z\s]*)", userInput)):
        match = re.search(r"(W|w)hy don't you ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you sure you want me to {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: Well, why do you want me to {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Why do you want me to do that?")

    # General responses
    elif(re.search(r"(H|h)ow ([A-za-z\s]*)\?", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How do you suppose?")
        if randomChoice == 2: print("[SYBIL]: What do you think the answer to that question is?")
        if randomChoice == 3: print("[SYBIL]: {}, how would you answer that question?".format(userName))

    elif(re.search(r"(W|w)hat ([A-za-z\s]*)\?", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How would an answer to that question make you feel?")
        if randomChoice == 2: print("[SYBIL]: {}, what do you think the answer to that is?".format(userName))
        if randomChoice == 3: print("[SYBIL]: What do you think the answer to that question is, {}?".format(userName))

    elif (re.search(r"(S|s)orry ([A-za-z\s]*)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, How does apologizing make you feel?".format(userName))
        if randomChoice == 2: print("[SYBIL]: Is apologizing the right choice?")
        if randomChoice == 3: print("[SYBIL]: Does apologizing make you feel better?")

    # Less serious responses
    elif (re.search(r"((H|h)ello|(H|h)i)(\s|\.)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Hello to you too {}.".format(userName))
        if randomChoice == 2: print("[SYBIL]: Hello there!")
        if randomChoice == 3: print("[SYBIL]: Hi {}! How are you?".format(userName)) 

    #elif computer beep boop, i also go by glados or aigis
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
                if re.search(r"^([A-Za-z]*)(\.*)", userInput):
                    userName = re.search(r"^([A-Za-z]*)(\.*)", userInput)
                    userName = userName.group(1)
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

