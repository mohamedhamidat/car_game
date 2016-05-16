import pygame
import time
import random 

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")


display_width = 800
display_height = 600

car_width = 70
car_height = 140


black = (0,0,0)
white = (255,255,255)
blue =(53, 115, 255)


red = (200,0,0)
green = (0, 200, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fast_and-Curious/hamidat')
clock = pygame.time.Clock()


carImg = pygame.image.load('racecar2.png')
gameIcon = pygame.image.load('carIcon.png')
pygame.display.set_icon(gameIcon)

backgroundImg = pygame.image.load ('way.png')
carThingImg = pygame.image.load('carcar.png')
treeThingImg = pygame.image.load('trees.jpg')

carCrash = pygame.image.load('carcrash.png')


pause = False


##############---------FONCTIONS--------------##################

def thing_dodged(count, x,y):
    """display the score"""
   # max_dodged = 10 
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render ("Dodged: "+ str(count), True, black)
    gameDisplay.blit(text, (x,y ))

def thing_speeds(count, x,y):
    """display the score"""
   # max_dodged = 10 
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render ("Spd: %d px/s"%(count*60), True, red)
    gameDisplay.blit(text, (x,y ))

def things(thingX, thingY, thingW, thingH, color):
    """draw random rectangles""" 
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])


def line(lineX, lineY, lineW, lineH, color):
    """draw way lines """ 
    pygame.draw.rect(gameDisplay, color, [lineX,lineY, lineW,lineH])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def car_thing(x, y):
    gameDisplay.blit(carThingImg, (x, y))

def tree_thing(x, y):
    gameDisplay.blit(treeThingImg, (x, y))

def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    """display message after crash"""
    largeText = pygame.font.SysFont("comicsansms",115)
    textSurf, textRect = text_object(text, largeText)
    textRect.center = ((display_width/2) , (display_height/2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash(x, y):
    gameDisplay.blit(carCrash, ((x - 45), (y - 30)))
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    #gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms",90)
    textSurf, textRect = text_object("You Crashed!", largeText)
    textRect.center = ((display_width/2) , (display_height/4))
    gameDisplay.blit(textSurf, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        

        button("Play Again", 150,250,100,50, green, bright_green, game_loop)
        button("Quit", 550,250,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None): 
    """message, dimension, active/inactive color"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x, y,w,h))
        if click[0] == 1 and action != None:
            action()
            # if action == "play":
            #     game_loop ()
            # elif action == "quit":
            #     pygame.quit()
            #     quit()

    else:
        pygame.draw.rect(gameDisplay, ic,(x, y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()

def game_unpause():
    global pause
    pause = False

def game_pause():
    ############
    pygame.mixer.music.pause()
    #############
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",90)
        textSurf, textRect = text_object("Pause!", largeText)
        textRect.center = ((display_width/2) , (display_height/4))
        gameDisplay.blit(textSurf, textRect)

        button("Continue !", 150,250,100,50, green, bright_green, game_unpause)
        button("Quit", 550,250,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)


def game_intro():

    pygame.mixer.music.load("atlanta.wav")
    pygame.mixer.music.play(-1)

    intro = True 

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)         
        # gameDisplay.blit(backgroundImg,(100,0))
    
        largeText = pygame.font.SysFont("comicsansms",80)
        textSurf, textRect = text_object("Let's Ride !", largeText)
        textRect.center = ((display_width/2) , (display_height/2))
        gameDisplay.blit(textSurf, textRect)

        button("GO !", 150,450,100,50, green, bright_green, game_loop)
        button("Quit", 550,450,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)



def game_loop():
    global pause

    pygame.mixer.music.load('coffee_stains.wav')
    pygame.mixer.music.play(-1)


    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change=0
    y_change=0
    speed_change=0

    thing_width = 70
    thing_height = 140

    thing_startx = random.randrange(100, display_width-200)
    thing_starty = -600
    thing_speed = 4 

    lineX = 400
    lineY = 0
    lineW = 20 
    lineH = 450
    line_speed = 10

    tree_y_right = 600
    tree_y_left = 300
    tree_h = 600 
    tree_speed = 10

    dodged = 0 

    gameExit= False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type== pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key == pygame.K_RIGHT:
                    x_change=5

                if event.key == pygame.K_p:
                    pause = True
                    game_pause()


                
                # elif event.key == pygame.K_UP:
                #     speed_change = 0.01
                #     # y_change = -5
                # elif event.key == pygame.K_DOWN:
                #     # y_change = 5
                #     if thing_speed > 4 : 
                #         speed_change = -0.01
                    
            if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                x_change= 0
                # y_change= 0
                # speed_change = 0


        x += x_change
        # y += y_change
        # thing_speed += speed_change

        gameDisplay.fill(white)         
        # gameDisplay.blit(backgroundImg,(100,0))
        
        line(150, 0, 20, display_height, blue)
        line(display_width-150, 0, 20, display_height, blue)

        #things (thing_startx, thing_starty, thing_width, thing_height, red)
        line(lineX, lineY, lineW, lineH, blue)
        car_thing(thing_startx, thing_starty)
        tree_thing (80, tree_y_left)
        tree_thing (700, tree_y_right)
        
        # line(lineX, lineY+150, lineW, lineH)

        thing_starty += thing_speed
        lineY += line_speed
        tree_y_left += tree_speed
        tree_y_right += tree_speed
        car(x,y)
        thing_dodged(dodged, 5, 5)
        thing_speeds(thing_speed, 5, 50)



        if x > display_width - car_width - 150 or x < 150 :
            # 100 way background image
            crash(x,y)
        



        if thing_starty > display_height :
            #thing_width = random.randrange(100, 300)  

            thing_starty = 0 - thing_height # reset y 
            thing_startx = random.randrange(170, display_width-thing_width-150)
            dodged += 1 
            # dodged += (1 +1 *(thing_speed*0.1))
            ###CHALLANGE####

            thing_speed += 1/20 # accelarate
            #thing_width += (dodged * 1.2)
            #thing_height = random.randrange(100, 300)
        

        if lineY > display_height  :
            #thing_width = random.randrange(100, 300)  

            lineY = 0 - lineH # reset y 
            thing_speed += 1/15

        if tree_y_left > display_height  :
        #thing_width = random.randrange(100, 300)  

            tree_y_left = 0 - tree_h # reset y 
            thing_speed += 1/15

        if tree_y_right > display_height  :
        #thing_width = random.randrange(100, 300)  

            tree_y_right = 0 - tree_h # reset y 
            thing_speed += 1/15

        ### crash with rec 
        if y < (thing_starty + thing_height) and y+ car_height >= thing_starty + thing_height:
        
            #print ("y crossover")
            if x > thing_startx and x < (thing_startx + thing_width) or x + car_width > thing_startx \
            and x + car_width < thing_startx + thing_width :
                #print ("x crossover")
                crash(x, y)


        


        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
