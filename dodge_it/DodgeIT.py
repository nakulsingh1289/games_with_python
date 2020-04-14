import pygame 
import time 
import random 

pygame.init()

display_width = 800
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
bright_green = (0, 200, 0)
bright_red = (200, 0, 0)

car_width = 73
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing game")
clock = pygame.time.Clock()

carImg = pygame.image.load("racecar.png")
gameIcon = pygame.image.load("racecar.png")

pygame.display.set_icon(gameIcon)


crash = True

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+ str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things( tx, ty, tw, th, color):
    pygame.draw.rect(gameDisplay, color, [tx, ty, tw, th])

def car(x, y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render (text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf , TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, TextRect)

    pygame.display.update()

    time.sleep(2.0)

    game_loop()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w> mouse[0] > x and y+h > mouse[1]> y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))

        if click[0]==1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def crash():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green ,bright_green , game_loop)
        button("Quit", 550, 450, 100, 50 ,red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

pause = True
def paused():


    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green ,bright_green , unpause)
        button("Quit", 550, 450, 100, 50 ,red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pause = False

def game_intro():

    intro = True 

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects(" DODGE IT ", largeText)
        textRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(textSurf, textRect)

        button("GO!", 150,450,100,50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_loop():

    x = (display_width*0.45)
    y = (display_height*0.85)

    x_change = 0

    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 7
    thing_width = 80
    thing_height = 80

    thingCount = 1

    dodged= 0

    gameExit= False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:

                    x_change=0

        x +=  x_change

        gameDisplay.fill(white)

        things(thing_start_x, thing_start_y, thing_width, thing_height, red)

        thing_start_y += thing_speed

        car(x,y)

        things_dodged(dodged)

        if x> display_width- car_width or x < 0:
            crash()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            dodged += 1
            thing_speed +=1
            thing_width += (dodged* 1.0)

        if y < thing_start_y +thing_height:
            

            if (x > thing_start_x and x < thing_start_x + thing_width) or (x+ car_width > thing_start_x and x+ car_width < thing_start_x + thing_width):
                crash()
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()

            
                
