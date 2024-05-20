import random
import string
from rich.console import Console

#Consoles for styling
redConsole = Console(style="red")
yellowConsole = Console(style="yellow")
greenConsole = Console(style="green")

correctWord = ''
wordList = []


def GuessWord(wordL, correctWrd):
    """

    :param wordL:
    :param correctWrd:
    :return:
    """
    global correctWord
    global wordList
    print('Lets Play! - 10 Tries')
    correctWord = correctWrd
    wordList = list(wordL)


def CheckWord():
    """

    :return:
    """
    guessesList = []
    suggestList = []
    usedWordList = []
    unUsedWords = string.ascii_lowercase
    guess = 1
    correctGuess = False
    print(correctWord)
    partialGuess = None
    while guess < 11:
        print('------------------------')
        print(f'Turn : {guess}')
        guessWord = (input('Enter Guess [0 for a Suggestion] : ')).lower()
        if guessWord.isalpha():
            if len(guessWord) == len(correctWord):
                guessesList.append(f'Guess {guess} : {guessWord}')
                if (guessWord == correctWord):
                    greenConsole.print(f'Correct Word : {guessWord}')
                    print(f'It took you {guess} Guesses to GET IT!')
                    correctGuess = True
                    break
                else:
                    guess += 1
                    partialGuess = ShowCorrectChars(guessWord, correctWord)
                    for c in guessWord:
                        if not usedWordList.__contains__(c):
                            usedWordList.append(c)
                            unUsedWords = unUsedWords.replace(c, "_")
                    print('Un-Used Characters : ',end="")
                    print(unUsedWords)
            else:
                print(f'Guess Should be Exactly {len(correctWord)} characters')
        else:
            if guessWord == '0':
                if partialGuess != None:
                    suggest = Suggestion(partialGuess[1], partialGuess[0], partialGuess[2])
                    guessesList.append(f'Suggestion for Guess No. {guess} : {suggest}')
                else:
                    print('No Last Guess Found')
            else:
                print('Please Only Enter Characters')
    return (correctGuess, guess, guessesList)


def Suggestion(guessWord, correctPosition, wrongPos):
    """"""
    correctChars = guessWord.strip()
    goodWord = []

    # Got it from stackoverflow
    # Use of all then looked up it in W3school
    # filterWords = [word for word in wordList if all(char in word for char in correctChars)]
    filterWords = [word for word in wordList if
                   all(word.count(char) == correctChars.count(char) for char in correctChars)]

    for word in filterWords:
        good = 0
        length = len(correctChars) - wrongPos
        for x in range(len(word)):
            if word[x] == correctPosition[x]:
                good += 1
        if good == length:
            goodWord.append(word)

    if len(goodWord) > 0:
        suggest = random.choice(goodWord)
        print(f'Bro needs Suggestion for English : {suggest} ')
        return suggest
    else:
        print('LOL : No Suggestion For You')
        print('')


def ShowCorrectChars(word, correct):
    correctGuess = ''
    correctChars = ''
    wrongPos = 0
    print('Your Guess : ', end="")
    for x in range(len(word)):
        if word[x] == correct[x]:
            correctGuess += word[x]
            correctChars += word[x]
            greenConsole.print(word[x], end="")

        else:

            if correct.__contains__(word[x]):
                correctChars += word[x]
                # correctGuess += word[x]
                correctGuess += '-'
                wrongPos = wrongPos + 1
                yellowConsole.print(word[x], end="")

            else:
                correctGuess += '-'
                redConsole.print(word[x], end="")
    print('')

    return (correctGuess, correctChars, wrongPos)

