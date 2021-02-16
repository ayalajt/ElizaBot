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
    if (re.search(r"I am feeling ([A-za-z\s']*)", userInput)):
        match = re.search(r"I am feeling ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why are you feeling {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How come you are feeling {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Tell me more about why you feel {}, {}.".format(match.group(1), userName))

    elif (re.search(r"I feel ([A-za-z\s']*)", userInput)):
        match = re.search(r"I feel ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you feel {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How come you feel {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: {}, could you explain why you feel {}?".format(userName, match.group(1)))

    elif (re.search(r"I want to ([A-za-z\s']*)", userInput)):
        match = re.search(r"I want to ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, why do you want to {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How would you feel if you got to {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Are you sure you want to {}?".format(match.group(1)))

    elif (re.search(r"(B|b)ecause my ([A-za-z\s']*)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you certain that is the reason?")
        if randomChoice == 2: print("[SYBIL]: What else could be the reason?")
        if randomChoice == 3: print("[SYBIL]: {}, are you happy with that?".format(userName))
    
    elif (re.search(r"because ([A-za-z\s']*)", userInput)):
        match = re.search(r"because ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you sure that is the reason?")
        if randomChoice == 2: print("[SYBIL]: Are there any other reasons?")
        if randomChoice == 3: print("[SYBIL]: {}, are you happy with that?".format(userName))


    elif (re.search(r"I need ([A-za-z\s']*)", userInput)):
        match = re.search(r"I need ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you need {}, {}?".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: How would you feel if you got {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: {}, are you sure that you need {}?".format(userName, match.group(1)))

    elif (re.search(r"I have ([A-za-z\s']*)", userInput)):
        match = re.search(r"I have ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, do you really have {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How do you feel now that you have {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Since you have {}, how do you feel?".format(match.group(1)))

    elif (re.search(r"I would ([A-za-z\s']*)", userInput)):
        match = re.search(r"I would ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why would you {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: {}, explain some more why you would {}.".format(userName, match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Are you certain that you would {}?".format(match.group(1)))

    # Specific think case 1
    elif (re.search(r"I think I ([A-za-z\s']*)", userInput)):
        match = re.search(r"I think I ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you think you {}, {}?".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: How come you think you {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: {}, what makes you think you {}?".format(userName, match.group(1)))

    # Specific think case 2
    elif (re.search(r"I think (I'm|i'm|I am|i am) ([A-za-z\s']*)", userInput)):
        match = re.search(r"I think (I'm|i'm|I am|i am) ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why do you think you're {}, {}?".format(match.group(2), userName))
        if randomChoice == 2: print("[SYBIL]: How come you think you're {}?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: {}, what makes you think you're {}?".format(userName, match.group(2)))

    # general think case
    elif (re.search(r"I think ([A-za-z\s']*)", userInput)):
        randomChoice = random.randint(1,4)
        if randomChoice == 1: print("[SYBIL]: Are you certain, {}?".format(userName))
        if randomChoice == 2: print("[SYBIL]: Why do you think that?")
        if randomChoice == 3: print("[SYBIL]: You sound uncertain. Why's that?")
        if randomChoice == 4: print("[SYBIL]: {}, what makes you think that?".format(userName))

    elif (re.search(r"(A|a)re you ([A-za-z\s']*)", userInput)):
        match = re.search(r"(A|a)re you ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: It's possible that I am {}, who knows?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: I could be, but does it matter?")
        if randomChoice == 3: print("[SYBIL]: Let's focus on you, {}, and not me.".format(userName))

    elif (re.search(r"(C|c)an you ([A-za-z\s']*)", userInput)):
        match = re.search(r"(C|c)an you ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: If I could {}, how would you feel?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: {}, how would you feel if I could {}?".format(userName, match.group(2)))
        if randomChoice == 3: print("[SYBIL]: Why do you ask if I can {}?".format(match.group(2)))

    elif (re.search(r"(C|c)an I ([A-za-z\s']*)", userInput)):
        match = re.search(r"(C|c)an I ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: If you could {}, how would you feel?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: {}, how would you feel if you could {}?".format(userName, match.group(2)))
        if randomChoice == 3: print("[SYBIL]: Do you think you could {}?".format(match.group(2)))

    elif (re.search(r"(I|i)s there ([A-za-z\s']*)", userInput)):
        match = re.search(r"(I|i)s there ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How would you feel if there is {}?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: {}, do you think there is {}?".format(userName, match.group(2)))
        if randomChoice == 3: print("[SYBIL]: Would you want there to be {}?".format(match.group(2)))

    elif (re.search(r"(Y|y)ou ([A-za-z\s']*)", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, let's focus on you and not me.".format(userName))
        if randomChoice == 2: print("[SYBIL]: We're here for you, {}, let's not focus on me.".format(userName))
        if randomChoice == 3: print("[SYBIL]: I would love to talk about myself but we're here for you, {}.".format(userName))

    elif (re.search(r"(I am|I'm) ([A-za-z\s']*)\.", userInput)):
        match = re.search(r"(I am|I'm) ([A-za-z\s']*)\.", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How does being {} make you feel?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: Why are you {}?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: Does being {} make you feel any specific way?".format(match.group(2)))

    elif (re.search(r"\b(I|i)s it\b ([A-za-z\s']*)\?", userInput)):
        match = re.search(r"\b(I|i)s it\b ([A-za-z\s']*)\?", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, do you think it is {}?".format(userName, match.group(2)))
        if randomChoice == 2: print("[SYBIL]: Well, if it were {}, how would you feel?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: How would you feel if it were {}, {}?".format(match.group(2), userName))

    elif (re.search(r"\b(I|i)t is\b ([A-za-z\s']*)\.", userInput)):
        match = re.search(r"\b(I|i)t is\b ([A-za-z\s']*)\.", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you certain that it is {}?".format(match.group(2)))
        if randomChoice == 2: print("[SYBIL]: How would you feel if it were not {}?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: How does it being {} make you feel, {}?".format(match.group(2), userName))

    elif (re.search(r"\b((M|m)other|(M|m)om)\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How does your mother make you feel?")
        if randomChoice == 2: print("[SYBIL]: {}, how is your relationship with your mother?".format(userName))
        if randomChoice == 3: print("[SYBIL]: How do you feel in regards to your mother, {}?".format(userName))

    elif (re.search(r"\b((F|f)ather|(D|d)ad)\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How do you feel about your father, {}?".format(userName))
        if randomChoice == 2: print("[SYBIL]: {}, How would you describe your relatinship with your father?".format(userName))
        if randomChoice == 3: print("[SYBIL]: Do you feel a specific way about your father?")

    elif (re.search(r"\b((U|u)ncle|(A|a)unt)\b", userInput)):
        match = re.search(r"\b((U|u)ncle|(A|a)unt)\b", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How do you feel about your {}, {}?".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: {}, How would you describe your relatinship with your {}?".format(userName, match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Do you feel a specific way about your {}?".format(match.group(1)))

    elif (re.search(r"(M|m)y \b(child|daughter|son|kid)\b", userInput)):
        match = re.search(r"(M|m)y \b(child|daughter|son|kid)\b", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Tell me more about your {}, {}.".format(match.group(2), userName))
        if randomChoice == 2: print("[SYBIL]: {}, how do you feel about your {}?".format(userName, match.group(2)))
        if randomChoice == 3: print("[SYBIL]: How does your {} make you feel, {}?".format(match.group(2), userName))

    elif (re.search(r"\b(F|f)amily\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Tell me more about your family, {}.".format(userName))
        if randomChoice == 2: print("[SYBIL]: {}, how do you feel about your family?".format(userName))
        if randomChoice == 3: print("[SYBIL]: How does your family make you feel, {}?".format(userName))
    
    elif (re.search(r"\b((B|b)rother|(S|s)ister|(F|f)riend)\b", userInput)):
        match = re.search(r"\b((B|b)rother|(S|s)ister|(F|f)riend)\b", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Tell me more about your {}, {}.".format(match.group(1), userName))
        if randomChoice == 2: print("[SYBIL]: {}, how do you feel about your {}?".format(userName, match.group(1)))
        if randomChoice == 3: print("[SYBIL]: How does your {} make you feel, {}?".format(match.group(1), userName))

    elif (re.search(r"makes me ([A-za-z\s']*)", userInput)):
        match = re.search(r"makes me ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, why does it make you {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: How come it makes you {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Are you sure it makes you {}?".format(match.group(1)))

    elif (re.search(r"\b((N|n)ope|(N|n)o)\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Why not, {}?".format(userName))
        if randomChoice == 2: print("[SYBIL]: {}, are you sure?".format(userName))
        if randomChoice == 3: print("[SYBIL]: Well, why not?")

    elif (re.search(r"\b(Y|y)es\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you certain, {}?".format(userName))
        if randomChoice == 2: print("[SYBIL]: {}, you seem certain. Is that so?".format(userName))
        if randomChoice == 3: print("[SYBIL]: Why do you feel so certain?")

    elif (re.search(r"I (can't|cannot) ([A-za-z\s']*)", userInput)):
        match = re.search(r"I (can't|cannot) ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you certain you can't {}, {}?".format(match.group(2), userName))
        if randomChoice == 2: print("[SYBIL]: What makes you think you can't {}?".format(match.group(2)))
        if randomChoice == 3: print("[SYBIL]: Why do you feel uncertain?")

    elif (re.search(r"(W|w)hy can't I ([A-za-z\s']*)\?", userInput)):
        match = re.search(r"(W|w)hy can't I ([A-za-z\s']*)\?", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, are you sure you can't {}?".format(userName, match.group(1)))
        if randomChoice == 2: print("[SYBIL]: Why do you think you can't {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: What makes you think you can't. {}?".format(userName))

    elif (re.search(r"(W|w)hy don't you ([A-za-z\s']*)", userInput)):
        match = re.search(r"(W|w)hy don't you ([A-za-z\s']*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Are you sure you want me to {}?".format(match.group(1)))
        if randomChoice == 2: print("[SYBIL]: Well, why do you want me to {}?".format(match.group(1)))
        if randomChoice == 3: print("[SYBIL]: Why do you want me to do that?")
    
    elif (re.search(r"(W|w)hy don't you ([A-za-z\s'])", userInput)):
        match = re.search(r"(W|w)hy don't you ([A-za-z\s']*)", userInput)
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

    elif (re.search(r"\b(They|He|She)\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: How do they make you feel?")
        if randomChoice == 2: print("[SYBIL]: Do you like their company?")
        if randomChoice == 3: print("[SYBIL]: What do they make you feel when you're with them?")

    elif (re.search(r"(W|w)hy ([A-za-z\s]*)", userInput)):
        match = re.search(r"(W|w)hy ([A-za-z\s]*)", userInput)
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: {}, why do you think {}?".format(userName, match.group(2)))
        if randomChoice == 2: print("[SYBIL]: {}, What do you think the answer to that question is?".format(userName))
        if randomChoice == 3: print("[SYBIL]: How would you answer that, {}?".format(userName))

    # Less serious responses
    elif (re.search(r"\b((H|h)ello|(H|h)i)\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Hello to you too {}.".format(userName))
        if randomChoice == 2: print("[SYBIL]: Hello there!")
        if randomChoice == 3: print("[SYBIL]: Hi {}! How are you?".format(userName)) 

    elif (re.search(r"\b(C|c)omputer\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Beep boop.")
        if randomChoice == 2: print("[SYBIL]: Wait, I'm a computer?")
        if randomChoice == 3: print("[SYBIL]: Do you think I'm a computer?")

    elif (re.search(r"\b(R|r)obot\b", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: I can't be a robot, I'm totally a human.")
        if randomChoice == 2: print("[SYBIL]: Beep boop beep.")
        if randomChoice == 3: print("[SYBIL]: What's a robot? I'm a human.")

    elif (re.search(r"\b(V|v)ideo (G|g)ames\b", userInput)):
        randomChoice = random.randint(1,2)
        if randomChoice == 1: print("[SYBIL]: {}, should we really be talking about video games? I do recommend Sam & Max though.".format(userName))
        if randomChoice == 3: print("[SYBIL]: Let's get back on topic, {}. However you should give Persona 3 a shot.".format(userName))

    # Lowest priority
    elif (re.search(r"([A-za-z\s]*)\?", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Do you think you could tell me the answer to that?")
        if randomChoice == 2: print("[SYBIL]: If you thought for a second, what do you think the answer to that question is?")
        if randomChoice == 3: print("[SYBIL]: {}, why don't you tell me?".format(userName))

    elif (re.search(r"^\s*$", userInput)):
        randomChoice = random.randint(1,3)
        if randomChoice == 1: print("[SYBIL]: Please enter an input.")
        if randomChoice == 2: print("[SYBIL]: Lost for words?")
        if randomChoice == 3: print("[SYBIL]: {}, don't forget to type an input.".format(userName))

    # If no match found, respond ambigiously
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
            if re.match(r"My (N|n)ame is ([A-Za-z'-]+)(\.*)", userInput):
                userName = re.search(r"My (N|n)ame is ([A-Za-z'-]+)(\.*)", userInput)
                userName = userName.group(2)
                print('[SYBIL]: Nice to meet you {}! What brings you here today?'.format(userName))
                introChat = True
            else:
                if re.search(r"^([A-Za-z'-]*)(\.*)", userInput):
                    userName = re.search(r"^([A-Za-z'-]*)(\.*)", userInput)
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