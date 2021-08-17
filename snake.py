#Snake.py
import pygame
import random
import time

pygame.init()   #Initializes the modules present in pygame

def main_snake(snake_size, snake_list):
    for a in snake_list:
        pygame.draw.rect(dis, snake_color, [a[0], a[1], snake_size, snake_size])

def message(msg,color):
    m = font_style.render(msg, True, color) #I dont know how render() works yet. But basically it creates the Game over message and then it is blitted onto the screen.
    dis.blit(m, [dis_width/8, dis_height/2])    #blit basically draws onto the screen. The message m is drawn onto the screen and the x & y coordinates are the position of the top left corner of the message on the screen.

dis_width = 1000 #Display Width
dis_height  = 600   #Display Height

dis = pygame.display.set_mode((dis_width,dis_height))    #Creates the screen and returns an object of the screen so the object can be used like it has for .fill() and for pygame.draw.rect(). 

bg_color = (0,128,0)    #Background color 'Green'
dis.fill(bg_color)  #Fills the color for the screen using the fill method on the screen object. This should be placed here as the snake will be affected. That's why I also placed it in the for loop.

snake_color = (255,215,0)   #Color of the snake 
snake_size = 20
snake_speed = 20

pygame.display.set_caption('The Snake by Prajwal Shenoy')   #This is the name that appears on the game window at the top

font_style = pygame.font.SysFont(None, 40,bold = True, italic = True)
score_font = pygame.font.SysFont("comicsansms", 35, italic = True)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (0,0,0))
    dis.blit(value, [0, 0])

clock = pygame.time.Clock() #creates a clock object so that fps can be specified

def gameLoop():
    run = True  #For controlling the while loop below
    end = False

    x = dis_width/2; x_change = 0
    y = dis_height/2; y_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, dis_width - snake_size) / 20.0) * 20.0 #Creates the food block location. For some reason the value 20 should be same as the snake_size variable otherwise the food might not be consumable by the snake
    foody = round(random.randrange(0, dis_height - snake_size) / 20.0) * 20.0

    while run:
        
        #dis.fill()
        pygame.draw.rect(dis,snake_color,[x,y,snake_size,snake_size])   #Rectangle that represents the snake
        pygame.draw.rect(dis,(0,0,0),[foodx,foody,snake_size,snake_size])
        pygame.display.update()     #Updates the game screen. It should generally be within a loop
        clock.tick(snake_speed)  #Makes updates at 30 fps. If increased then the speed of the snake increases as the clock will tick faster.

        while end == True:
            dis.fill((255,255,255))
            message("Game Over. Press Q to Quit or C to play again.",(255,0,0))  #Function that displays the message when boundary is reached
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        end = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Close(x) button pressed on the window
                run = False
            if event.type == pygame.KEYDOWN:    #KEYDOWN is the pygame class that contains the different keys as shown below
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_size
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_size

        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            end = True

        x += x_change
        y += y_change

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for a in snake_list[:-1]:
            if a == snake_head:
                end = True

        dis.fill(bg_color) #This is placed here because otherwise the snakes length will increase as the background doesnt get updated
        main_snake(snake_size, snake_list)
        Your_score(snake_length - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width - snake_size) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_size) / 20.0) * 20.0
            snake_length += 1
        

    
    #time.sleep(2) #2 means 2 seconds. Requires time package to be imported. Makes sure the game window closes after 2 seconds. Not same as pygame.time()

    pygame.quit()
    quit()

gameLoop()