# import pygame module
import pygame


class Block(pygame.sprite.Sprite):
    # constructor
    def __init__(self, color, width, height):
        # call the parent class
        super(Block, self).__init__()

        # create an image of the block, and fill it with a color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # fetch rectangle object
        self.rect = self.image.get_rect()
        self.rect.centerx = 140
        self.rect.centery  = 50

# show the pygame window
pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Memory Maze: Level 3")

# colors
off_black = (37, 40, 51)
atom_off_black = (40, 44, 52)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


circle_order = 0

# TEXT
font = pygame.font.Font("Rajdhani-Regular.ttf", 60)

red_text = [font.render("0 / 3 Red", True, (255,0,0)), font.render("1 / 3 Red", True, (255,0,0)), font.render("2 / 3 Red", True, (255,0,0)), font.render("3 / 3 Red", True, (255,0,0))]
green_text = [font.render("0 / 3 Green", True, (0,255,0)), font.render("1 / 3 Green", True, (0,255,0)), font.render("2 / 3 Green", True, (0,255,0)), font.render("3 / 3 Green", True, (0,255,0))]
blue_text = [font.render("0 / 3 Blue", True, (0,0,255)), font.render("1 / 3 Blue", True, (0,0,255)), font.render("2 / 3 Blue", True, (0,0,255)), font.render("3 / 3 Blue", True, (0,0,255))]

win = font.render("You win!", True, white)
thanks = font.render("Thanks for playing Memory Maze!", True, white)

def check_text():
    if (circle_order == 0): # none
        screen.blit(red_text[0], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[0], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 1): # 1 red
        screen.blit(red_text[1], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[0], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 2): # 2 red
        screen.blit(red_text[2], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[0], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 3): # 3 red
        screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[0], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 4): # 1 green
        screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[1], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 5): # 2 green
        screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[2], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 6): # 3 green
        screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[3], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[0], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 7): # 1 blue
        screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[3], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[1], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 8): # 2 blue
        screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        screen.blit(green_text[3], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        screen.blit(blue_text[2], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))

    if (circle_order == 9): # 3 blue
        # screen.blit(red_text[3], (800 - red_text[0].get_width() // 2, 150 - red_text[0].get_height() // 2))
        # screen.blit(green_text[3], (800 - green_text[0].get_width() // 2, 350 - green_text[0].get_height() // 2))
        # screen.blit(blue_text[3], (800 - blue_text[0].get_width() // 2, 550 - blue_text[0].get_height() // 2))
        screen.fill(atom_off_black)
        screen.blit(win, (500 - win.get_width() // 2, 300 - win.get_height() // 2))
        screen.blit(thanks, (500 - thanks.get_width() // 2, 400 - thanks.get_height() // 2))


# draws only maze, no circles
def only_draw_maze():
    screen.fill(atom_off_black)
    # draw maze
    pygame.draw.line(screen, white, (100,100), (100,600)) # left border
    pygame.draw.line(screen, white, (100,600), (600,600)) # bottom border
    pygame.draw.line(screen, white, (600,200), (600,600)) # right border
    pygame.draw.line(screen, white, (200,100), (600,100)) # top border

    pygame.draw.line(screen, white, (300,100), (300,200)) # vertical 1
    pygame.draw.line(screen, white, (200,200), (200,300)) # vertical 2
    pygame.draw.line(screen, white, (400,200), (400,300)) # vertical 3
    pygame.draw.line(screen, white, (200,300), (200,400)) # vertical 4
    pygame.draw.line(screen, white, (400,400), (400,500)) # vertical 5

    pygame.draw.line(screen, white, (300,200), (400,200)) # horizontal 1
    pygame.draw.line(screen, white, (500,200), (600,200)) # horizontal 2
    pygame.draw.line(screen, white, (200,300), (500,300)) # horizontal 3
    pygame.draw.line(screen, white, (200,400), (300,400)) # horizontal 4
    pygame.draw.line(screen, white, (400,400), (600,400)) # horizontal 5
    pygame.draw.line(screen, white, (200,500), (500,500)) # horizontal 6

    check_text()

def draw_maze():
    screen.fill(atom_off_black)
    # draw maze
    pygame.draw.line(screen, white, (100,100), (100,600)) # left border
    pygame.draw.line(screen, white, (100,600), (600,600)) # bottom border
    pygame.draw.line(screen, white, (600,200), (600,600)) # right border
    pygame.draw.line(screen, white, (200,100), (600,100)) # top border

    pygame.draw.line(screen, white, (300,100), (300,200)) # vertical 1
    pygame.draw.line(screen, white, (200,200), (200,300)) # vertical 2
    pygame.draw.line(screen, white, (400,200), (400,300)) # vertical 3
    pygame.draw.line(screen, white, (200,300), (200,400)) # vertical 4
    pygame.draw.line(screen, white, (400,400), (400,500)) # vertical 5

    pygame.draw.line(screen, white, (300,200), (400,200)) # horizontal 1
    pygame.draw.line(screen, white, (500,200), (600,200)) # horizontal 2
    pygame.draw.line(screen, white, (200,300), (500,300)) # horizontal 3
    pygame.draw.line(screen, white, (200,400), (300,400)) # horizontal 4
    pygame.draw.line(screen, white, (400,400), (600,400)) # horizontal 5
    pygame.draw.line(screen, white, (200,500), (500,500)) # horizontal 6

    # draw circles
    # red
    pygame.draw.circle(screen, red, (250,150), 10, 0)
    pygame.draw.circle(screen, red, (350,150), 10, 0)
    pygame.draw.circle(screen, red, (450,450), 10, 0)
    # green
    pygame.draw.circle(screen, green, (350,250), 10, 0)
    pygame.draw.circle(screen, green, (250,350), 10, 0)
    pygame.draw.circle(screen, green, (550,550), 10, 0)
    # blue
    pygame.draw.circle(screen, blue, (550,150), 10, 0)
    pygame.draw.circle(screen, blue, (550,350), 10, 0)
    pygame.draw.circle(screen, blue, (550,450), 10, 0)

    check_text()


draw_maze()


# sprite
sprite_one = Block(white, 20, 15)
# sprite_one.centerx = 140
# sprite_one.centery = 50


screen.blit(sprite_one.image, (sprite_one.rect.centerx,sprite_one.rect.centery))
# update the display
pygame.display.flip()

# booleans
red1 = False
red2 = False
red3 = False

green1 = False
green2 = False
green3 = False

blue1 = False
blue2 = False
blue3 = False

def get_circles():
    global circle_order
    global red1, red2, red3, green1, green2, green3, blue1, blue2, blue3
    # red
    if (sprite_one.rect.centerx>=240 and sprite_one.rect.centerx<=260 and red1 == False):
        if (sprite_one.rect.centery>=140 and sprite_one.rect.centery<=160):
            if (circle_order == 0):
                circle_order = 1
                red1 = True
            elif (circle_order == 1):
                circle_order = 2
                red1 = True
            elif (circle_order == 2):
                circle_order = 3
                red1 = True
    if (sprite_one.rect.centerx>=340 and sprite_one.rect.centerx<=360 and red2 == False):
        if (sprite_one.rect.centery>=140 and sprite_one.rect.centery<=160):
            if (circle_order == 0):
                circle_order = 1
                red2 = True
            elif (circle_order == 1):
                circle_order = 2
                red2 = True
            elif (circle_order == 2):
                circle_order = 3
                red2 = True
    if (sprite_one.rect.centerx>=440 and sprite_one.rect.centerx<=460 and red3 == False):
        if (sprite_one.rect.centery>=440 and sprite_one.rect.centery<=460):
            if (circle_order == 0):
                circle_order = 1
                red3 = True
            elif (circle_order == 1):
                circle_order = 2
                red3 = True
            elif (circle_order == 2):
                circle_order = 3
                red3 = True

    # green
    if (sprite_one.rect.centerx>=340 and sprite_one.rect.centerx<=360 and sprite_one.rect.centery>=240 and sprite_one.rect.centery<=260 and green1 == False):
        if (circle_order == 3):
            circle_order = 4
            green1 = True
        elif (circle_order == 4):
            circle_order = 5
            green1 = True
        elif (circle_order == 5):
            circle_order = 6
            green1 = True
        elif (circle_order < 3):
            circle_order = 0
            sprite_one.rect.centerx = 140
            sprite_one.rect.centery = 50
            only_draw_maze()
            screen.blit(sprite_one.image, sprite_one.rect)
            pygame.display.flip()
            red1 = False
            red2 = False
            red3 = False
            green1 = False
            green2 = False
            green3 = False
            blue1 = False
            blue2 = False
            blue3 = False
    if (sprite_one.rect.centerx>=240 and sprite_one.rect.centerx<=260 and sprite_one.rect.centery>=340 and sprite_one.rect.centery<=360 and green2 == False):
        if (circle_order == 3):
            circle_order = 4
            green2 = True
        elif (circle_order == 4):
            circle_order = 5
            green2 = True
        elif (circle_order == 5):
            circle_order = 6
            green2 = True
        elif (circle_order < 3):
            circle_order = 0
            sprite_one.rect.centerx = 140
            sprite_one.rect.centery = 50
            only_draw_maze()
            screen.blit(sprite_one.image, sprite_one.rect)
            pygame.display.flip()
            red1 = False
            red2 = False
            red3 = False
            green1 = False
            green2 = False
            green3 = False
            blue1 = False
            blue2 = False
            blue3 = False
    if (sprite_one.rect.centerx>=540 and sprite_one.rect.centerx<=560 and sprite_one.rect.centery>=540 and sprite_one.rect.centery<=560 and green3 == False):
        if (circle_order == 3):
            circle_order = 4
            green3 = True
        elif (circle_order == 4):
            circle_order = 5
            green3 = True
        elif (circle_order == 5):
            circle_order = 6
            green3 = True
        elif (circle_order < 3):
            circle_order = 0
            sprite_one.rect.centerx = 140
            sprite_one.rect.centery = 50
            only_draw_maze()
            screen.blit(sprite_one.image, sprite_one.rect)
            pygame.display.flip()
            red1 = False
            red2 = False
            red3 = False
            green1 = False
            green2 = False
            green3 = False
            blue1 = False
            blue2 = False
            blue3 = False

    # blue
    if (sprite_one.rect.centerx>=540 and sprite_one.rect.centerx<=560 and sprite_one.rect.centery>=140 and sprite_one.rect.centery<=160 and blue1 == False):
        if (circle_order == 6):
            circle_order = 7
            blue1 = True
        elif (circle_order == 7):
            circle_order = 8
            blue1 = True
        elif (circle_order == 8):
            circle_order = 9
            blue1 = True
        elif (circle_order < 6):
            circle_order = 0
            sprite_one.rect.centerx = 140
            sprite_one.rect.centery = 50
            only_draw_maze()
            screen.blit(sprite_one.image, sprite_one.rect)
            pygame.display.flip()
            red1 = False
            red2 = False
            red3 = False
            green1 = False
            green2 = False
            green3 = False
            blue1 = False
            blue2 = False
            blue3 = False
    if (sprite_one.rect.centerx>=540 and sprite_one.rect.centerx<=560 and sprite_one.rect.centery>=340 and sprite_one.rect.centery<=360 and blue2 == False):
        if (circle_order == 6):
            circle_order = 7
            blue2 = True
        elif (circle_order == 7):
            circle_order = 8
            blue2 = True
        elif (circle_order == 8):
            circle_order = 9
            blue2 = True
        elif (circle_order < 6):
            circle_order = 0
            sprite_one.rect.centerx = 140
            sprite_one.rect.centery = 50
            only_draw_maze()
            screen.blit(sprite_one.image, sprite_one.rect)
            pygame.display.flip()
            red1 = False
            red2 = False
            red3 = False
            green1 = False
            green2 = False
            green3 = False
            blue1 = False
            blue2 = False
            blue3 = False
    if (sprite_one.rect.centerx>=540 and sprite_one.rect.centerx<=560 and sprite_one.rect.centery>=440 and sprite_one.rect.centery<=460 and blue3 == False):
        if (circle_order == 6):
            circle_order = 7
            blue3 = True
        elif (circle_order == 7):
            circle_order = 8
            blue3 = True
        elif (circle_order == 8):
            circle_order = 9
            blue3 = True
        elif (circle_order < 6):
            circle_order = 0
            sprite_one.rect.centerx = 140
            sprite_one.rect.centery = 50
            only_draw_maze()
            screen.blit(sprite_one.image, sprite_one.rect)
            pygame.display.flip()
            red1 = False
            red2 = False
            red3 = False
            green1 = False
            green2 = False
            green3 = False
            blue1 = False
            blue2 = False
            blue3 = False

def bounce_back(x,y):
    # borders
    # left
    if (sprite_one.rect.centerx==100 and sprite_one.rect.centery>=100 and sprite_one.rect.centery<=600):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # bottom
    if (sprite_one.rect.centerx>=100 and sprite_one.rect.centerx<=600 and sprite_one.rect.centery==600):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # right
    if (sprite_one.rect.centerx==600 and sprite_one.rect.centery>=200 and sprite_one.rect.centery<=600):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # top
    if (sprite_one.rect.centerx>=200 and sprite_one.rect.centerx<=600 and sprite_one.rect.centery==100):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()

    # vertical
    # 1
    if (sprite_one.rect.centerx==300 and sprite_one.rect.centery>=100 and sprite_one.rect.centery<=200):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 2
    if (sprite_one.rect.centerx==200 and sprite_one.rect.centery>=200 and sprite_one.rect.centery<=300):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 3
    if (sprite_one.rect.centerx==400 and sprite_one.rect.centery>=200 and sprite_one.rect.centery<=300):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 4
    if (sprite_one.rect.centerx==200 and sprite_one.rect.centery>=300 and sprite_one.rect.centery<=400):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 5
    if (sprite_one.rect.centerx==400 and sprite_one.rect.centery>=400 and sprite_one.rect.centery<=500):
        sprite_one.rect.centerx = x
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()

    # horizontal
    # 1
    if (sprite_one.rect.centerx>=300 and sprite_one.rect.centerx<=400 and sprite_one.rect.centery==200):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 2
    if (sprite_one.rect.centerx>=500 and sprite_one.rect.centerx<=600 and sprite_one.rect.centery==200):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 3
    if (sprite_one.rect.centerx>=200 and sprite_one.rect.centerx<=500 and sprite_one.rect.centery==300):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 4
    if (sprite_one.rect.centerx>=200 and sprite_one.rect.centerx<=300 and sprite_one.rect.centery==400):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 5
    if (sprite_one.rect.centerx>=400 and sprite_one.rect.centerx<=600 and sprite_one.rect.centery==400):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
    # 6
    if (sprite_one.rect.centerx>=200 and sprite_one.rect.centerx<=500 and sprite_one.rect.centery==500):
        sprite_one.rect.centery = y
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()

    # circles
    get_circles()


only_draw_maze()
screen.blit(sprite_one.image, sprite_one.rect)
pygame.display.flip()

space_count = 0
done=True

left_flag = False
right_flag = False
up_flag = False
down_flag = False

while done==True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            done = False
        if event.type == pygame.KEYDOWN:

            if (event.key == pygame.K_SPACE and space_count==0):
                space_count = 10
                draw_maze()
                screen.blit(sprite_one.image, sprite_one.rect)
                pygame.display.flip()
                pygame.time.delay(5000)
                only_draw_maze()
                screen.blit(sprite_one.image, sprite_one.rect)
                pygame.display.flip()

            x = sprite_one.rect.centerx
            y = sprite_one.rect.centery

            if event.key == pygame.K_LEFT:
                left_flag = True
                print('left')
                sprite_one.rect.centerx -= 10
                only_draw_maze()
                screen.blit(sprite_one.image, sprite_one.rect)
                pygame.display.flip()
                bounce_back(x,y)

            if event.key == pygame.K_RIGHT:
                right_flag = True
                print('right')
                sprite_one.rect.centerx += 10
                only_draw_maze()
                screen.blit(sprite_one.image, sprite_one.rect)
                pygame.display.flip()
                bounce_back(x,y)

            if event.key == pygame.K_UP:
                up_flag = True
                print('up')
                sprite_one.rect.centery -= 10
                only_draw_maze()
                screen.blit(sprite_one.image, sprite_one.rect)
                pygame.display.flip()
                bounce_back(x,y)

            if event.key == pygame.K_DOWN:
                down_flag = True
                sprite_one.rect.centery += 10
                print ('down')
                only_draw_maze()
                screen.blit(sprite_one.image, sprite_one.rect)
                pygame.display.flip()
                bounce_back(x,y)

        if event.type == pygame.KEYUP:

            if (left_flag == True):
                left_flag = False
            if (right_flag == True):
                right_flag = False
            if (up_flag == True):
                up_flag = False
            if (down_flag == True):
                down_flag = False

    if (left_flag == True):
        sprite_one.rect.centerx -= 10
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
        bounce_back(x,y)
    if (right_flag == True):
        sprite_one.rect.centerx += 10
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
        bounce_back(x,y)
    if (up_flag == True):
        sprite_one.rect.centery -= 10
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
        bounce_back(x,y)
    if (down_flag == True):
        sprite_one.rect.centery += 10
        only_draw_maze()
        screen.blit(sprite_one.image, sprite_one.rect)
        pygame.display.flip()
        bounce_back(x,y)



# This stops the pygame window from closing straight away
input("Press enter to close")
pygame.quit()
