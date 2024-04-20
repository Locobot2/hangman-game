import random, time, os, sys, pygame

pygame.init()

with open("data/clean_words_alpha.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split())) 


width = 500
height = 600


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
    
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return(action)
        


def mainMenu():

    play_img = pygame.image.load("data/playBtn.png")
    quit_img = pygame.image.load("data/quitBtn.png")

    play_button = Button(280, 480, play_img, 0.3)
    quit_button = Button(70, 480, quit_img, 0.3)
    
    
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 50)
    
    text = font.render("Hangman Game", False, (255, 255, 255))



    running = True
    while running:

        bg = pygame.image.load("data/bg.png")
        screen.blit(bg, (0,0))
        
        if play_button.draw():
            rules()
        if quit_button.draw():
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(text, (width/2-170, height/2-30))
        pygame.display.update()
    sys.exit(0)
    # print(random.choice(words))
    
def rules():

    play_img = pygame.image.load("data/contBtn.png")
    quit_img = pygame.image.load("data/quitBlkBtn.png")

    cont_button = Button(280, 380, play_img, 0.3)
    quit_button = Button(70, 380, quit_img, 0.3)
    
    running = True
    while running:
        bg = pygame.image.load("data/rules.png")
        screen.blit(bg, (0, 0))
        
        if cont_button.draw():
            game()
        if quit_button.draw():
            running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        time.sleep(2)
        pygame.display.update()
    sys.exit(0)
    
def game():
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    sys.exit(0)
mainMenu()