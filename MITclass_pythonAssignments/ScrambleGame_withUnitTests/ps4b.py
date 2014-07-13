from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore=0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord=None
    # For each word in the wordList
    for words in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord2(words,hand):
            # Find out how much making that word is worth
            score = getWordScore(words,n)
            # If the score for that word is higher than your best score
           
                # Update your best score, and best word accordingly
            if score>maxScore:
                maxScore=score
                bestWord=words

    # return the best word you found.
    return bestWord

def isValidWord2(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    freqDic = hand.copy()
    if word=='':
        return False
    for letters in word:
      if freqDic.get(letters,0)==0:
         return False
      freqDic[letters]-=1
    return True
   




#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    # Keep track of the total score
    totalScore=0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand)>0:    
        # Display the hand
        
        print "Current hand: ", 
        displayHand(hand)
        print
        # Computer chooses the best word possible
        selected_word=compChooseWord(hand, wordList, n)
        
        # If the computer is unable to find a word it will return None and we will break
        if selected_word==None:
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not a single period):
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            totalScore+=getWordScore(selected_word, n);
            print ('"'+selected_word+'"' +' earned '+str(getWordScore(selected_word, n))+' points. Total: ' + str(totalScore)+' points')
            print
            # Update the hand 
            hand=updateHand(hand, selected_word)

    # Game is over computer returned None
    print("Total score:" + str(totalScore)+" points.")
    
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    
    hand={}
    playing=True  
    while playing:
        userInput = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if userInput in 'nr':
            incorrectInput=True                                    
            if (hand and userInput=='r') or userInput=='n':
                while incorrectInput:            
                    userInput2 = raw_input("Enter u to have yourself play, c to have the computer play:")
                    if userInput2=='u':
                        incorrectInput=False
                        if userInput=='n':
                            hand=dealHand(HAND_SIZE)                        
                        playHand(hand, wordList, HAND_SIZE)
                    elif userInput2=='c':
                        incorrectInput=False
                        if userInput=='n':
                            hand=dealHand(HAND_SIZE)
                        compPlayHand(hand, wordList, HAND_SIZE)
                    else:
                        print 'Invalid command.'
            else:
                print('You have not played a hand yet. Please play a new hand first!')
        elif userInput=='e':            
            break
        else:
            print 'Invalid command.'

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    


