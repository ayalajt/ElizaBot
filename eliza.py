import re
import time

# Can possibly making enums such as FEELINGS to keep track of all possible emotions
# Can possibly call another function that picks a correct question from the given input

infiniteLoop = True
introChat = False
toQuit = False

def chooseResponse(userInput):
    if (re.search("feeling (.*)", userInput)):
        match = re.search("feeling (.*)", userInput)
        print("[SYBIL]: Why are you feeling {}?".format(match.group(1)))
    if (re.search("feel (.*)", userInput)):
        match = re.search("feel (.*)", userInput)
        print("[SYBIL]: Why do you feel {}?".format(match.group(1)))
    #if (re.search("feel (.*)", userInput)):
     #   match = re.search("feel (.*)", userInput)
      #  print("[SYBIL]: Why do you feel {}?".format(match.group(1)))

def checkQuit(userInput):
     if re.match("quit", userInput):
            print("[SYBIL]: Goodbye!")
            quit()

def introText(userInput):
    # need to figure out how to quit from here
    return True

def main():
    global infiniteLoop
    introChat = False
    while infiniteLoop:
        while introChat == False:
            print("[SYBIL]: Hello! I am Sybil, a psychotherapist. What's your name?") 
            userInput = input("[USER]: ")
            checkQuit(userInput)
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

