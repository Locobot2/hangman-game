from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import random, time, os, sys, pygame, keyboard

pygame.init()

with open("data/dict.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split())) 

global width
w = 500
h = 600


screen = pygame.display.set_mode((w, h))
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
                
        screen.blit(text, (w/2-(text.get_width()/2), h/2-30))
        pygame.display.update()
    sys.exit(0)
    
def rules():

    play_img = pygame.image.load("data/contBtn.png")
    quit_img = pygame.image.load("data/quitBlkBtn.png")

    cont_button = Button(280, 380, play_img, 0.3)
    quit_button = Button(70, 380, quit_img, 0.3)

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30)
    
    text = font.render("Rules:", False, (0, 0, 0))
    text2 = font.render("*You have 6 guesses", False, (0, 0, 0))
    text3 = font.render("*Have Fun", False, (0, 0, 0))
    
    running = True
    while running:
        screen.fill((255, 255, 255))
        
        if cont_button.draw():
            game()
        if quit_button.draw():
            running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(text, (w/2-(text.get_width()/2), 30))
        screen.blit(text2, (w/2-(text2.get_width()/2), 80))
        screen.blit(text3, (w/2-(text3.get_width()/2), 130))

        pygame.display.update()
    sys.exit(0)
    
def game():

    one = False
    two = False
    three = False
    four = False
    five = False
    six = False

    manStand = pygame.image.load("data/stick figure states/stand.png")
    s1 = pygame.image.load("data/stick figure states/1.png")
    s2 = pygame.image.load("data/stick figure states/2.png")
    s3 = pygame.image.load("data/stick figure states/3.png")
    s4 = pygame.image.load("data/stick figure states/4.png")
    s5 = pygame.image.load("data/stick figure states/5.png")
    s6 = pygame.image.load("data/stick figure states/6.png")

    sWidth = manStand.get_width()
    sHeight = manStand.get_height()
    manStand = pygame.transform.scale(manStand, (int(sWidth * 2), int(sHeight * 2)))
    s1 = pygame.transform.scale(s1, (120, 120))
    s2 = pygame.transform.scale(s2, (120, 120))
    s3 = pygame.transform.scale(s3, (120, 120))
    s4 = pygame.transform.scale(s4, (120, 120))
    s5 = pygame.transform.scale(s5, (120, 120))
    s6 = pygame.transform.scale(s6, (120, 120))

    global word
    word = (random.choice(words))
    # word = "aaaaaaaaaaaaaaaaaaaa"
    # print(word)
    # lttrCount = 0
    global dashes, letterCount, text, text2
    dashes = ""
    letterCount = len(word)

    for i in range(len(word)):
        # lttrCount += 1
        dashes = dashes + "_"

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 35)
    
    text = font.render(dashes, False, (255, 255, 255))
    text2 = font.render("letters remaining: " + str(letterCount), False, (255, 255, 255))
    

    usedLttrs = []

    def letterAdd(lttr):
        global dashes, letterCount, text, text2
        for letter in range(len(word)):
            if word[letter] == lttr:
                letterCount -= 1
                string_list = list(dashes)
                string_list[letter] = lttr
                dashes = "".join(string_list)
                text = font.render(dashes, False, (255, 255, 255))
                text2 = font.render("letters remaining: " + str(letterCount), False, (255, 255, 255))
        usedLttrs.append(lttr)
        # print(dashes)
                
                


    # print(lttrCount)
    # print(dashes)
    
    running = True
    while running:
        lettersVar = ""
        badLttr = 0

        for i in usedLttrs:
            if word.find(str(i)) == -1:
                lettersVar = lettersVar + i
                badLttr += 1
        text3 = font.render("letters used: " + lettersVar, False, (255, 255, 255))
        screen.fill((0, 0, 0))
        # print(usedLttrs)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if "a" not in usedLttrs:
                        letterAdd("a")

                elif event.key == pygame.K_b:
                    if "b" not in usedLttrs:
                        if "b" not in usedLttrs:
                            letterAdd("b")
                elif event.key == pygame.K_c:
                    if "c" not in usedLttrs:
                        if "c" not in usedLttrs:
                            letterAdd("c")
                elif event.key == pygame.K_d:
                    if "d" not in usedLttrs:
                        if "d" not in usedLttrs:
                            letterAdd("d")
                elif event.key == pygame.K_e:
                    if "e" not in usedLttrs:
                        if "e" not in usedLttrs:
                            letterAdd("e")
                elif event.key == pygame.K_f:
                    if "f" not in usedLttrs:
                        if "f" not in usedLttrs:
                            letterAdd("f")
                elif event.key == pygame.K_g:
                    if "g" not in usedLttrs:
                        if "g" not in usedLttrs:
                            letterAdd("g")
                elif event.key == pygame.K_h:
                    if "h" not in usedLttrs:
                        if "h" not in usedLttrs:
                            letterAdd("h")
                elif event.key == pygame.K_i:
                    if "i" not in usedLttrs:
                        if "i" not in usedLttrs:
                            letterAdd("i")
                elif event.key == pygame.K_j:
                    if "j" not in usedLttrs:
                        if "j" not in usedLttrs:
                            letterAdd("j")
                elif event.key == pygame.K_k:
                    if "k" not in usedLttrs:
                        if "k" not in usedLttrs:
                            letterAdd("k")
                elif event.key == pygame.K_l:
                    if "l" not in usedLttrs:
                        if "l" not in usedLttrs:
                            letterAdd("l")
                elif event.key == pygame.K_m:
                    if "m" not in usedLttrs:
                        if "m" not in usedLttrs:
                            letterAdd("m")
                elif event.key == pygame.K_n:
                    if "n" not in usedLttrs:
                        if "n" not in usedLttrs:
                            letterAdd("n")
                elif event.key == pygame.K_o:
                    if "o" not in usedLttrs:
                        if "o" not in usedLttrs:
                            letterAdd("o")
                elif event.key == pygame.K_p:
                    if "p" not in usedLttrs:
                        if "p" not in usedLttrs:
                            letterAdd("p")
                elif event.key == pygame.K_q:
                    if "q" not in usedLttrs:
                        if "q" not in usedLttrs:
                            letterAdd("q")
                elif event.key == pygame.K_r:
                    if "r" not in usedLttrs:
                        if "r" not in usedLttrs:
                            letterAdd("r")
                elif event.key == pygame.K_s:
                    if "s" not in usedLttrs:
                        if "s" not in usedLttrs:
                            letterAdd("s")
                elif event.key == pygame.K_t:
                    if "t" not in usedLttrs:
                        if "t" not in usedLttrs:
                            letterAdd("t")
                elif event.key == pygame.K_u:
                    if "u" not in usedLttrs:
                        if "u" not in usedLttrs:
                            letterAdd("u")
                elif event.key == pygame.K_v:
                    if "v" not in usedLttrs:
                        if "v" not in usedLttrs:
                            letterAdd("v")
                elif event.key == pygame.K_w:
                    if "w" not in usedLttrs:
                        if "w" not in usedLttrs:
                            letterAdd("w")
                elif event.key == pygame.K_x:
                    if "x" not in usedLttrs:
                        if "x" not in usedLttrs:
                            letterAdd("x")
                elif event.key == pygame.K_y:
                    if "y" not in usedLttrs:
                        if "y" not in usedLttrs:
                            letterAdd("y")
                elif event.key == pygame.K_z:
                    if "z" not in usedLttrs:
                        if "z" not in usedLttrs:
                            letterAdd("z")


        if badLttr == 1:
            one = True
        if badLttr == 2:
            two = True
        if badLttr == 3:
            three = True
        if badLttr == 4:
            four = True
        if badLttr == 5:
            five = True
        if badLttr == 6:
            six = True

        screen.blit(manStand, (150, 60))
        if one:
            screen.blit(s1, (152, 90))
        if two:
            screen.blit(s2, (152, 90))
            one=False
        if three:
            screen.blit(s3, (152, 90))
            two = False
        if four:
            screen.blit(s4, (152, 90))
            three = False
        if five:
            screen.blit(s5, (152, 90))
            four = False
        if six:
            screen.blit(s6, (152, 90))
            five = False


            
        # randomWord()
        # print(word)
        screen.blit(text, (0, 400))
        screen.blit(text2, (15,500))
        screen.blit(text3, (15, 550))
        pygame.display.update()

        if letterCount == 0:
            endScreen(True)

        if six:
            time.sleep(1)
            endScreen(False)


    sys.exit(0)

def endScreen(boolean):
    global word

    playAgain_img = pygame.image.load("data/pAgainBtn.png")
    quit_img = pygame.image.load("data/quitBtn.png")

    playAgain_button = Button(280, 480, playAgain_img, 0.3)
    quit_button = Button(70, 480, quit_img, 0.3)

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 35)
    font2 = pygame.font.SysFont("Comic Sans MS", 25)
    
    
    

    if boolean == False:
        text = font.render("You Lose!", False, (255, 255, 255))
        text2 = font2.render("The word was \"" + word + "\"", False, (255, 255, 255))
    
    if boolean == True:
        text = font.render("You Win!", False, (255, 255, 255))
        text2 = font2.render("The word is \"" + word + "\"", False, (255, 255, 255))
    
    running = True
    while running:

        

        bg = pygame.image.load("data/bg.png")
        screen.blit(bg, (0, 0))

        if playAgain_button.draw():
            game()
        if quit_button.draw():
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.blit(text, (w/2-(text.get_width()/2), h/2-30))
        # text_rect = text.get_rect(center=(w/2, 350))
        screen.blit(text2, (w/2-(text2.get_width()/2), h/2+20))
        pygame.display.update()
    sys.exit(0)

# mainMenu()
rules()