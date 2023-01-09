from english_words import get_english_words_set
import random

wordList = get_english_words_set(['web2'], lower=True)

stepsToHung = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
  -----------
    """,
    r"""
     +---+
     |   |
     0   |
         |
         |
         |
  -----------
    """,
    r"""
     +---+
     |   |
     0   |
     |   |
         |
         |
  -----------
    """,
    r"""
     +---+
     |   |
     0   |
    /|   |
         |
         |
  -----------
    """,
    r"""
     +---+
     |   |
     0   |
    /|\  |
         |
         |
  -----------
    """,
    r"""
     +---+
     |   |
     0   |
    /|\  |
    /    |
         |
  -----------
    """,
        r"""
     +---+
     |   |
     0   |
    /|\  |
    / \  |
         |
  -----------
    """

]

def guess(wordCharArray, correctLetters):
  guessedLetter = input("Guess a letter? \n")
  isMatch = guessedLetter in wordCharArray
  index = None
  if isMatch:
    correctLetters.append(guessedLetter)
  return (isMatch, correctLetters)

def game(numberWrong, wordCharArray, answerSection, correctLetters):
    hangmanImage = stepsToHung[numberWrong]
    print(r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
    
    """)
    print(hangmanImage)
    displayedAnswer = ""
    for i in answerSection:
      displayedAnswer += i
    print(displayedAnswer)
    if "_" not in displayedAnswer:
      print("You Won!!!!!!!!")
    input = guess(wordCharArray, correctLetters)
    if input[0]:
      correctLetters = input[1]
      i = 0
      for x in wordCharArray:
          for y in correctLetters:
            if x == y:
              answerSection[i] = y
          i += 2
    elif not input[0]:
      numberWrong += 1
    return (numberWrong, answerSection, correctLetters)

playing = True
while playing:
  wonOrLostAndPlayAgain = False
  numberWrong = 0
  answerSection = []
  correctLetters = []
  selectedIndex = random.randint(0, len(wordList))
  selectedWord = list(wordList)[selectedIndex]
  for char in list(selectedWord):
    answerSection += "_ "
  while not wonOrLostAndPlayAgain:
      wordCharArray = list(selectedWord)
      turnResults = game(numberWrong, wordCharArray, answerSection, correctLetters)
      answerSection = turnResults[1]
      numberWrong = turnResults[0]
      lost = len(stepsToHung) == numberWrong
      won = "_" not in answerSection
      wonOrLostAndPlayAgain = won or lost
      if won:
        playing = (input("You Won!!!!!!!!\n\nPlay Again y/n\n") == "y")
        break
      if lost:
        playing = (input("You Lost.......\n\nPlay Again y/n\n") == "y")


