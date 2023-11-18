import pygame

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    '-1': (200, 200, 200),
    '2': (236, 239, 241),
    '4': (207, 216, 220),
    '8': (176, 190, 197),
    '16': (144, 164, 174),
    '32': (120, 144, 156),
    '64': (96, 125, 139),
    '128': (84, 110, 122),
    '256': (69, 90, 100),
    '512': (55, 71, 79),
    '1024': (38, 50, 56),
    '2048': (29, 37, 41),
}

board = [[-1, -1, -1, -1],
          [-1, -1, -1, -1],
          [-1, -1, -1, -1],
          [-1, -1, -1, -1]]

size = (500, 500)
screen = pygame.display.set_mode(size)

def initScreen():
    screen.fill(colors['white'])
    pygame.display.update()

isGameRunning = True

def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
            else:
                print("키보드 키 입력 이벤트가 감지됨")

def drawDisplay():
    global screen

    baseX = 35
    baseY = 35
    blockHeight = 100
    blockWidth = 100
    margin = 10

    for i in range(4):
        for j in range(4):
            x = (blockWidth + margin) * j + baseX
            y = (blockHeight + margin) * i + baseY
            pygame.draw.rect(screen, colors['-1'], [x, y, blockWidth, blockHeight], 2)

    pygame.display.flip()




def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")

    while isGameRunning:
        setEventListener()
        drawDisplay()

    pygame.quit()

run2048()