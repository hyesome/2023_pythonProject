from pythonBasic.games.updown import runUpDown
from pythonBasic.games.hangman import runHangMan
from pythonBasic.games.game2048 import run2048

def menuPrint():
    print("=======GAME=======")
    print("1. 행맨")
    print("2. 업다운")
    print("3. 2048")
    print("0. 종료")
    print("==================")

userInput = -1

while userInput != 0:
    menuPrint()
    userInput = int(input("SELECT MENU ::: "))

    if userInput == 1:
        runHangMan()
    elif userInput == 2:
        runUpDown()
    elif userInput == 3:
        run2048()
