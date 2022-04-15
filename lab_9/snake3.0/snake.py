import pygame
from random import randrange
pygame.init()

#Basic parameters:
WIDTH, HEIGHT = 800, 600
FPS = 7 # set the frame rate - 60 frames per second
cell = 40 #size of food/each part of snake 

#Colors
WHITE = (255, 255, 255)
GREY = (68, 75, 82)
RED = (252, 108, 133)
GREEN = (0, 168, 107)
BLACK = (0, 0, 0)
BLUE = (121, 160, 193)
BC = (240, 255, 240)

#Fonts for words and their sizes, жирность & курсив
font = pygame.font.SysFont("Copperplate Gothic Bold", 30)
font1 = pygame.font.SysFont("Copperplate Gothic Bold", 75)

#Initializing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')

#Varibles:
level = 1
SCORE = 0
sp = 20
finished = False
lose = False

time_delay = 6000
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

#Creating Food --> its position, color, size; redraw
class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell)) 
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)

#Creating Snake -- > its speed, list coordinates of each its cell, change its position, color
class Snake:
    def __init__(self):
        self.speed = sp
        self.body = [[80, 80],[1000,1000],[1040,1040],[1080,1080],[1120,1120],[1160, 1160]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN
    
    def move(self):
        for event in events:
            if event.type == pygame.KEYDOWN:
                #if we press LEFT button x coordinate decreases, y coord will not be changed
                if event.key == pygame.K_LEFT and self.destination != 'right': 
                    self.dx = -self.speed 
                    self.dy = 0
                    self.destination = 'left'
                #if we press RIGHT button, x coord increases, y coord will not be changed
                if event.key == pygame.K_RIGHT and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                #if we press UP button, x coord will not be changed, y coord decreases
                if event.key == pygame.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                #if we press UP button, x coord will not be changed, y coord increases
                if event.key == pygame.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
                    
        #when first cell moves, the cell next to it will replace it
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        
        # move the snake
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        #in case if snake goes out of the screen:
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT

    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))
    
    #checking collision between food and snake, if they collide add 1 SCORE
    # if SCORE is divisible by 3 add level and increase speed
    def collide_food(self, f:Food):
        global SCORE
        global level
        global FPS
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            SCORE += 1
            if SCORE % 3 == 0:
                level += 1
                FPS += 2
            if (SCORE + 1) % 5 == 0:
                SCORE += randrange(2, 4)
            self.body.append([1000, 1000])
    #check collision of snake with itself, if it is true you are loser:     
    def collide_self(self):
        global lose
        if self.body[0] in self.body[1:]:
            lose = True

    #redraw when snake eats Food
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()

s = Snake() 
f = Food()
clock = pygame.time.Clock() #create the clock
   
# Game event cycle
# Stay in the loop until the user clicks the close window button
while not finished:
    clock.tick(FPS) 
    screen.fill(GREY) #background color

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        if event.type == timer_event:
            f.redraw()
            
    #execute all functions related to classes:
    s.draw() #draw the snake
    s.move() #move the snake 
    f.draw() #draw the food
    s.collide_food(f) #checking collision between food & snake
    s.collide_self()  #checking collision of snake with itself
    
    f.draw()
    s.draw()
    s.move()
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)

   
        # s.draw()
        # s.move()
        # s.collide_food(f)
        # s.collide_self()
        # s.check_food(f)
    
    #all necessary texts that we will show in screen:
    game_over = font1.render(f'GAME OVER', False, BLACK)
    game_over_score = font1.render(f'SCORE: {SCORE} ', False, GREEN) 
    text = font.render(f"LEVEL: {level}", False, WHITE)
    screen.blit(text,(25, 20))  #show the level while playing
    text1 = font.render(f"SCORE: {SCORE}", False, WHITE)
    screen.blit(text1,(25, 40)) #show the score while playing
    
    #when player loses:
    while lose:
        pygame.draw.rect(screen, WHITE, (100, 75, 600, 400)) #create rectangle to show results clearly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False

            #show results:
            text = font.render(f"LEVEL: {level}", False, BLACK)
            text1 = font.render(f"SCORE: {SCORE}", False, BLACK)
            screen.blit(game_over, (240,200))
            screen.blit(text,(350, 270))
            screen.blit(text1,(350, 300))

            pygame.display.flip() 
    pygame.display.flip()  #displaying the entire game window on the screen
pygame.quit() #Finish the Pygame 