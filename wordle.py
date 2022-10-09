# Wordle
import random
from termcolor import colored

# set dictionary with long list of random words
def buildList(filename):
    wordfile = open(filename, 'r')
    words = wordfile.read()
    wordledictionary = words.split("\n")
    #print (wordleDictionary)
    wordfile.close()
    return wordledictionary

# select a wordle from dictionary
def choosewordle(wlist):
    return random.choice(wlist).upper()

# Input 5-letter word and convert to uppercase
def inputRealFiveLetterWordUpperCase():
    conted = True
    while conted:
        word = input("Enter a 5-letter word:").lower()
        if len(word) == 5:
            conted = False
            if (word not in wordleList):
                conted = True
                print("This is not a word...")
    return word.upper()

# Check if word letters match
# uses X for exact match
# uses O for wrong location
# uses - for no match
def match(win,att):
    # no letter at right place to begin
    result = list("-----")

    # Check all well positioned letters first
    # and cross them out
    for a in range(len(att)):
        alet = att[a]
        wlet = win[a]
        if alet == wlet:
            result[a] = "X"
            # Remove letter from wordle to avoid further comparisons
            win[a]='~'
            # Remove letter from attempt word to avoid further comparisons
            att[a]='@'
    #print("Exact matches:", result)

    # Look for letter at wrong place
    for a in range(len(att)):
        alet = att[a]
        for w in range(a, len(win)+a):
            wlet = win[w % (len(win))]
            if (alet == wlet):
                win[w % (len(win))]='~'
                #print("Letter in:",alet, win)
                result[a] = "O"
        # rebuild str from list
    return "".join(result)


###########
# Main Wordle
# 2022-10-08
###########

# 5 attempts allowed
nbMaxTries = 6

# Load up dictionary from file
wordleList = buildList('fiveletterwords.csv')
print(len(wordleList), "words in the list")

# Select random word
wordle = choosewordle(wordleList)
#print(wordle)

# List of attempts
attempt = ["","","","","",""]

# List of letter placement
result=["","","","","",""]

# Let's go
i = 0
while i < nbMaxTries:
    # Enter word of exactly 5 characters
    attempt[i] = inputRealFiveLetterWordUpperCase()

    # Check if word match - pass List of letters
    result[i] = match(list(wordle), list(attempt[i]))
    # Display result
    print()

    # Show results
    print("Attempt #", i+1)
    for j in range(i+1):
        print (j+1,": ",attempt[j])
        print (j+1,": ",result[j])

    if result[i] == "XXXXX":
        if (i == 0):
            print("Bravo! You won in 1 attempt!")
        else:
            print("Bravo! You won in "+str(i+1)+" attempts!")
        break
    # if not, try again
    i +=1

# Loser
if i == nbMaxTries: print ("Oh no... The wordle was: ", wordle)