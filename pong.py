from pygame import *
SCREENWIDTH = 900
SCREENHEIGHT = 600
screen = display.set_mode((SCREENWIDTH, SCREENHEIGHT))

WHITE = (255,255,255)
BGCOLOR = (0,220,160)
BLUE = (50,100,230)
RED = (230, 50, 100)

p1Y = 250
p2Y = 250
paddleWidth = 30
paddleHeight = 100

ballX = 450
ballY = 300
ballDx = 4
ballDy = 4

running = True
myClock = time.Clock()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    p1Paddle = Rect(50, p1Y, paddleWidth, paddleHeight)
    p2Paddle = Rect(850, p2Y, paddleWidth, paddleHeight)
    ball = Rect(ballX, ballY, 10 ,10 )

    keys = key.get_pressed()
    if (keys [K_w] and p1Y > 0):
            p1Y -= 5
    elif (keys[K_s] and p1Y+paddleHeight < SCREENHEIGHT):
            p1Y += 5


    if (keys [K_UP] and p2Y > 0):
            p2Y -= 5
    elif (keys[K_DOWN] and p2Y+paddleHeight < SCREENHEIGHT):
            p2Y += 5


    ballX += ballDx
    ballY += ballDy
    if (ball.colliderect(p1Paddle)):
            ballDx = abs(ballDx)
    elif (ball.colliderect(p2Paddle)):
            ballDx = abs(ballDx) * -1
    elif (ballY <= 0):
            ballDy = abs(ballDy)
    elif (ballY >= SCREENHEIGHT):
            ballDy = abs(ballDy) * -1
    elif (ballX >= SCREENWIDTH or ballX <= 0):
            ballX = 450
            ballY = 300
            p1y = 250
            p2y =250



    screen.fill(BGCOLOR)
    draw.rect(screen, BLUE, p1Paddle)
    draw.rect(screen, RED, p2Paddle)
    draw.rect(screen, WHITE, ball)

    display.flip()
    myClock.tick(60)

quit()

