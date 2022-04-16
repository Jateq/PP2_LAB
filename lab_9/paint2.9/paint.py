import pygame


WIDTH, HEIGHT = 1200, 750   #our screen
FPS = 60
draw = False                #click - draw, not click - not draw
lastPos = (0, 0)            # initial position
radius = 15                 # initial radius
color = 'blue'              # initial color
mode = 'pen'                # initial mode

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white')) # inital layer
fontRadius = pygame.font.SysFont('Arial', 66, bold=True)

class Button(): #to make clickable buttons
    def __init__(self, x, y, image):
        self.image = image 
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y) 
        self.clicked = False

    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == 0:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = 0        

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


def drawLine(screen, start, end, width, color): # pen
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)


def drawCircle(screen, start, end, width, color): # circle
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)


def drawRectangle(screen, start, end, width, color): # rectangle
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)


def drawSquare(screen, start, end, width, color): #square
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))


    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))        

def drawRightTriangle(screen, start, end, width, color): #righttriangle
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))

def drawEquilateralTriangle(screen, start, end, width, color): #equilateraltriangle
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))

def drawRhombus(screen, start, end, width, color): #Rhombus
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)


#Color selection and buttons
black = pygame.transform.scale(pygame.image.load('Images\\black.png'), (50, 50))
gray = pygame.transform.scale(pygame.image.load('Images\\gray.png'), (50, 50))
red_black = pygame.transform.scale(pygame.image.load('Images\\red black.png'), (50, 49))
red = pygame.transform.scale(pygame.image.load('Images\\red.png'), (50, 50))
orange = pygame.transform.scale(pygame.image.load('Images\\orange.png'), (50, 50))
yellow = pygame.transform.scale(pygame.image.load('Images\\yellow.png'), (50, 50))
green = pygame.transform.scale(pygame.image.load('Images\\green.png'), (50, 50))
blue = pygame.transform.scale(pygame.image.load('Images\\blue.png'), (50, 49))
black_blue = pygame.transform.scale(pygame.image.load('Images\\black_blue.png'), (50, 49))
purple = pygame.transform.scale(pygame.image.load('Images\\purple.png'), (50, 50))
black_button = Button(27, 650, black)
gray_button = Button(75, 650, gray)
red_black_button = Button(125, 651, red_black)
red_button = Button(175, 650, red)
orange_button = Button(225, 650, orange)
yellow_button = Button(275, 650, yellow)
green_button = Button(325, 650, green)
blue_button = Button(375, 651, blue)
black_blue_button = Button(425, 651, black_blue)
purple_button = Button(475, 650, purple)

#Eraser, cicrcle, rect, clear, square, righttr, equatr, rhombus and their buttons
eraser = pygame.transform.scale(pygame.image.load('Images\\eraser.png'), (60, 60))
circle = pygame.transform.scale(pygame.image.load('Images\\circle.png'), (60, 60))
rect = pygame.transform.scale(pygame.image.load('Images\\rect.png'), (60, 60))
clear = pygame.transform.scale(pygame.image.load('Images\\clear.png'), (70, 70))
square = pygame.transform.scale(pygame.image.load('Images\\black.png'), (60, 60))
righttr = pygame.transform.scale(pygame.image.load('Images\\rt.png'), (60, 60))
equaltr = pygame.transform.scale(pygame.image.load('Images\\et1.png'), (60, 60))
rhombus = pygame.transform.scale(pygame.image.load('Images\\rohmb.png'), (60, 60))
#buttons
eraser_button = Button(27, 550, eraser)
circle_button = Button(27, 455, circle)
rect_button = Button(27, 100, rect)
clear_button = Button(1100, 650, clear)
square_button = Button(27, 170, square)
righttr_button = Button(27, 240, righttr)
equaltr_button = Button(27, 310, equaltr)
rhombus_buttom = Button(27, 385, rhombus)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        # Click keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))
            if event.key == pygame.K_y:
                color = 'yellow'
            if event.key == pygame.K_b:
                color = 'black'
            if event.key == pygame.K_s:
                mode = 'square'     
            if event.key == pygame.K_t:
                mode = 'right_tri'                           
            if event.key == pygame.K_g:
                color = 'gray'
            if event.key == pygame.K_u:
                mode = 'eq_tri'       
            if event.key == pygame.K_h:
                mode = 'rhombus'                        
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1)   # limit for max radius
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)     # limit for min radius


        # click mouse
        if event.type == pygame.MOUSEBUTTONDOWN: 
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos

        # after click mouse
        if event.type == pygame.MOUSEBUTTONUP: 
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, radius, color) 
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)        
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)                                                       
            draw = False
          

        # mouse move
        if event.type == pygame.MOUSEMOTION: 
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos

    # to show options on screen
    if black_button.draw():
        color = 'black'; mode = 'pen'
    if gray_button.draw():
        color = 'gray'; mode = 'pen'
    if red_black_button.draw():
        color = (136, 0, 21)
    if red_button.draw():
        color = 'red'; mode = 'pen'
    if orange_button.draw():
        color = 'orange'; mode = 'pen'
    if yellow_button.draw():
        color = 'yellow'; mode = 'pen'
    if green_button.draw():
        color = 'green'; mode = 'pen'
    if blue_button.draw():
        color = 'blue'; mode = 'pen'
    if black_blue_button.draw():
        color = (63, 72, 204); mode = 'pen'
    if purple_button.draw():
        color = 'purple'; mode = 'pen'    
    if eraser_button.draw():
        mode = 'erase'
    if circle_button.draw():
        mode = 'circle'
    if rect_button.draw():
        mode = 'rectangle'
    if clear_button.draw():
        screen.fill((255, 255, 255))    
    if square_button.draw():
        mode = 'square'   
    if righttr_button.draw():
        mode = 'right_tri'
    if equaltr_button.draw():
        radius = 4
        mode = 'eq_tri'  
    if rhombus_buttom.draw():
        radius = 4
        mode = 'rhombus'

    # show radius and color
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))

    pygame.display.flip()
    clock.tick(FPS)