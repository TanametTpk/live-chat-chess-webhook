import pyautogui

A_ASCII = 97
Z_ASCII = 122
ASCII_RANGE = Z_ASCII - A_ASCII + 1

BLOCK_SIZE = 98
FIRST_BLOCK_X = 360
FIRST_BLOCK_Y = 912

pyautogui.FAILSAFE = False

def getPosition(code):
    if len(code) != 2:
        return -1, -1
    
    x = code[0]
    y = code[1]

    if not x.isalpha() or not y.isnumeric():
        return -1, -1

    positionX = ord(x) - A_ASCII + 1
    positionY = int(y)

    if positionX > ASCII_RANGE or positionX < 1 or positionY > 8 or positionY < 1:
        return -1, -1

    targetX = FIRST_BLOCK_X + (positionX - 1) * BLOCK_SIZE
    targetY = FIRST_BLOCK_Y - (positionY - 1) * BLOCK_SIZE
    
    return targetX, targetY

def move(command):
    commands = command.split(" ")
    if len(commands) != 3:
        return

    start = commands[0]
    end = commands[2]

    startX, startY = getPosition(start)
    endX, endY = getPosition(end)

    checkList = [startX, startY, endX, endY]
    for position in checkList:
        if position == -1:
            return

    pyautogui.moveTo(startX, startY)
    pyautogui.mouseDown()
    pyautogui.moveTo(endX, endY)
    pyautogui.mouseUp()