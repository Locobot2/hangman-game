import random, time, os, sys, pygame, keyboard

pygame.init()

with open("data/dict.txt", "r") as file: 
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

    word = (random.choice(words))
    # word = "aaaaaaaaaaaaaaaaaaaa"
    print(word)
    # lttrCount = 0
    global dashes
    dashes = ""
    letterCount = 0

    for i in range(len(word)):
        # lttrCount += 1
        dashes = dashes + "_"

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30)
    
    text = font.render(dashes, False, (255, 255, 255))

    usedLttrs = []

    def letterAdd(lttr):
        global dashes
        for letter in range(len(word)):
            if word[letter] == lttr:
                string_list = list(dashes)
                string_list[letter] = "a"
                dashes = "".join(string_list)
        print(dashes)
                
                


    # print(lttrCount)
    # print(dashes)
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        # print(usedLttrs)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if "a" not in usedLttrs:
                        letterAdd("a")
                        usedLttrs.append("a")
                        text = font.render(dashes, False, (255, 255, 255))
#USE A FOR LOOP TO ITERATE THROUGHT THE WORD AND REPLACE IN DASHES









                        
                    # print(usedLttrs)




                elif event.key == pygame.K_b:
                    if "b" not in usedLttrs:
                        usedLttrs.append("b")
                elif event.key == pygame.K_c:
                    if "c" not in usedLttrs:
                        usedLttrs.append("c")
                elif event.key == pygame.K_d:
                    if "d" not in usedLttrs:
                        usedLttrs.append("d")
                elif event.key == pygame.K_e:
                    if "e" not in usedLttrs:
                        usedLttrs.append("e")
                elif event.key == pygame.K_f:
                    if "f" not in usedLttrs:
                        usedLttrs.append("f")
                elif event.key == pygame.K_g:
                    if "g" not in usedLttrs:
                        usedLttrs.append("g")
                elif event.key == pygame.K_h:
                    if "h" not in usedLttrs:
                        usedLttrs.append("h")
                elif event.key == pygame.K_i:
                    if "i" not in usedLttrs:
                        usedLttrs.append("i")
                elif event.key == pygame.K_j:
                    if "j" not in usedLttrs:
                        usedLttrs.append("j")
                elif event.key == pygame.K_k:
                    if "k" not in usedLttrs:
                        usedLttrs.append("k")
                elif event.key == pygame.K_l:
                    if "l" not in usedLttrs:
                        usedLttrs.append("l")
                elif event.key == pygame.K_m:
                    if "m" not in usedLttrs:
                        usedLttrs.append("m")
                elif event.key == pygame.K_n:
                    if "n" not in usedLttrs:
                        usedLttrs.append("n")
                elif event.key == pygame.K_o:
                    if "o" not in usedLttrs:
                        usedLttrs.append("o")
                elif event.key == pygame.K_p:
                    if "p" not in usedLttrs:
                        usedLttrs.append("p")
                elif event.key == pygame.K_q:
                    if "q" not in usedLttrs:
                        usedLttrs.append("q")
                elif event.key == pygame.K_r:
                    if "r" not in usedLttrs:
                        usedLttrs.append("r")
                elif event.key == pygame.K_s:
                    if "s" not in usedLttrs:
                        usedLttrs.append("s")
                elif event.key == pygame.K_t:
                    if "t" not in usedLttrs:
                        usedLttrs.append("t")
                elif event.key == pygame.K_u:
                    if "u" not in usedLttrs:
                        usedLttrs.append("u")
                elif event.key == pygame.K_v:
                    if "v" not in usedLttrs:
                        usedLttrs.append("v")
                elif event.key == pygame.K_w:
                    if "w" not in usedLttrs:
                        usedLttrs.append("w")
                elif event.key == pygame.K_x:
                    if "x" not in usedLttrs:
                        usedLttrs.append("x")
                elif event.key == pygame.K_y:
                    if "y" not in usedLttrs:
                        usedLttrs.append("y")
                elif event.key == pygame.K_z:
                    if "z" not in usedLttrs:
                        usedLttrs.append("z")
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
        pygame.display.update()


    sys.exit(0)
# mainMenu()
game()