import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600

gridx = int(SCREEN_WIDTH / 50)
gridy = int(SCREEN_HEIGHT / 50)

grid = [[0]*gridx]*gridy

frogx = 0
frogy = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Unintended consequences')
 #fiils the screen so it has a blue background

### loading images
grassBlockImg = pygame.image.load('Assets/grass_block.png')
dirtBlockImg = pygame.image.load('Assets/dirt_block.png')
titleImg = pygame.image.load('Assets/title.png')

frogCakeImg = pygame.image.load('Assets/frog_and_cake.png')
frogNoCakeImg = pygame.image.load('Assets/frog_no_cake.png')

########################################

FONT = pygame.font.SysFont(None, 32)

class Button:
    def __init__(self, x, y, w, h, text, color=(255, 255, 255), hover_color=(219, 11, 70), text_color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)

        pygame.draw.rect(surface, 
                         self.hover_color if is_hovered else self.color, 
                         self.rect, 
                         border_radius=6)

        text_surf = FONT.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


########################################

button1 = Button(SCREEN_WIDTH / 2 - 0.5*(150), 400, 150, 50, "Begin...")
leftButton = Button(25, 400, 150, 50, "Left choice")
rightButton = Button(575, 400, 150, 50, "Right choice")

beginGame = False
left1 = False
right1 = False

def screen1():
    screen.fill((115, 190, 223))
    start_y = 500 #where row of grass blocks is drawn
    block_dim = 50 #if 50, a block is 50 x 50 pixels

    #draws row of grass blocks across screen
    for i in range(0, SCREEN_WIDTH, block_dim):
        screen.blit(pygame.transform.scale(grassBlockImg, (block_dim, block_dim)), (i, start_y))

    #draws row of dirt blocks across screen for every 'row' under grass block row
    for i in range(start_y + block_dim, SCREEN_HEIGHT, block_dim):
        for j in range(0, SCREEN_WIDTH, block_dim):
            screen.blit(pygame.transform.scale(dirtBlockImg, (block_dim, block_dim)), (j, i))

    screen.blit(pygame.transform.scale(titleImg, (1200, 300)), (10, 10))

    #button1 = Button(SCREEN_WIDTH / 2 - 0.5*(150), 400, 150, 50, "Begin...")
    button1.draw(screen)

def screen2():
    screen.fill((115, 190, 223))
    

    screen.blit(pygame.transform.scale(frogCakeImg, (750, 600)), (0, 0))

    leftButton.draw(screen)
    rightButton.draw(screen)

    text1 = FONT.render("Lily is a frog with a cake. Should she eat the cake (left choice) or give", True, (255, 255, 255))
    screen.blit(text1, (10, 100))

    text2 = FONT.render("it to her friend Fran (right choice)?", True, (255, 255, 255))
    screen.blit(text2, (10, 125))

def screen3():
    screen.fill((115, 190, 223))
    

    screen.blit(pygame.transform.scale(frogNoCakeImg, (750, 600)), (0, 0))

    leftButton.draw(screen)
    rightButton.draw(screen)

    text1 = FONT.render("Lily eats the cake.", True, (255, 255, 255))
    screen.blit(text1, (10, 100))

   


keepRunning = True
while keepRunning:
    
    if(beginGame == False):
        screen1()
    if((beginGame == True) and (left1 == False and right1 == False)):
        screen2()
    elif(left1 == True):
        screen3()




    #screen.blit(pygame.transform.scale(frog_front_img, (50, 50)), (100, 300))

    #checks for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False
        
        if button1.is_clicked(event):
            beginGame = True
        if leftButton.is_clicked(event):
            if(left1 == False or right1 == False):
                left1 = True
                



    pygame.display.update() #updates the display





pygame.quit()