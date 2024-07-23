import pygame
import time
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 30
width = 143
height = 256
gap = 60
score = 0
high_score = 0
pass_pipe = True
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption('Flappy Bird')
font = pygame.font.SysFont('Bauhaus 93', 20)
font_gameover = pygame.font.SysFont('Bauhaus 93', 10)
white = (255,255,255)

scroll = 0
speed = 2
scorecount = 0

background = pygame.image.load('background.png')
text_over = pygame.image.load('game over.png')
ground = pygame.image.load('ground.png')
game_start = pygame.image.load('title.png')
tut = pygame.image.load('tut.png')
flappytitle = pygame.image.load('flappybird.png')
medal = pygame.image.load('medal.png')
golden = pygame.image.load('golden.png')
silver = pygame.image.load('silver.png')
bronze = pygame.image.load('bronze.png')
start_over = pygame.image.load('startover.png')
def draw_text(text, font, text_col,x ,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def reset():
    pipe_group.empty()
    flappy.rect.x = 30
    flappy.rect.y = int(height/2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1,3):
            img = self.image = pygame.image.load(f'bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0

    def update(self):\

        rate = 5
        if speed == 2:
            if self.counter > rate:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            if flying==True and game_over == False: self.image = pygame.transform.rotate(self.images[self.index], self.vel * - 5)
            #elif flying == False and game_over == True: self.image = pygame.transform.rotate(self.images[self.index],self.vel * - 5)

            if flying == True :
                self.vel += 0.5
                if self.vel >10:
                    self.vel = 10
                if self.rect.bottom <  200:
                    self.rect.y += int(self.vel)
                if self.rect.top<0:
                    self.vel = 1
            self.counter += 1

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and game_over == False:
                self.clicked = True
                self.vel = -5
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipebot.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(gap/2)]
        if position == -1:
            self.rect.topleft  = [x,y + int(gap/2)]
    def update(self):
        if game_over == False:
            if flying == False:
                self.rect.x -= 10000
            self.rect.x -= speed
            if self.rect.right<0:
                self.kill()
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(30, int(height/2))
bird_group.add(flappy)
bpipe = Pipe(width,int(height/2),-1)
tpipe = Pipe(width, int(height/2),1)
pipe_group.add(bpipe)
pipe_group.add(tpipe)
button = Button(width/2.8 ,  150, start_over)
game_over = False
flying = False
run = True
pipe_rate = 3000
last_pipe = pygame.time.get_ticks() - pipe_rate



while run:
    clock.tick(fps)
    screen.blit(background, (0,0))
    pipe_group.draw(screen)
    bird_group.draw(screen)
    if game_over == False:
        pipe_group.update()
    screen.blit(ground, (scroll, 200))
    bird_group.update()
    # game over
    if game_over == True:
        screen.blit(text_over, (width/6, 20))
        if score >= 0: screen.blit(medal,(width/10,70))
        if score > 10: screen.blit(bronze, (width / 10, 70))
        if score > 20: screen.blit(silver, (width / 10, 70))
        if score > 30: screen.blit(golden, (width / 10, 70))
        draw_text(str((score)), font_gameover, white, int(width - 45), 87)
        draw_text(str((high_score)), font_gameover, white, int(width - 45), 107)
        if button.draw() == True:
            game_over = False
            score = reset()

    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group .sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right > pipe_group .sprites()[0].rect.right\
            and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                if flying == True:
                    if scorecount == 0:
                        score = score + 1
                        scorecount += 1
                    pass_pipe = False
    screen.blit(game_start,(0,0))
    if flying == False and game_over == False:
        screen.blit(tut,(width/3,100))
        screen.blit(flappytitle, (width / 6, 50))

    if game_over == False :
        draw_text(str((score)),font,white, int(width/2.2),20)
        if high_score < score:
            high_score = score
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        game_over = True
    if flappy.rect.bottom >197:
        game_over = True
        flying = False

    if game_over == False and flying == True:

        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_rate:
            pipe_height = random.randint(-50 ,25)
            bpipe = Pipe(width, int(height / 2) + pipe_height, -1)
            tpipe = Pipe(width, int(height / 2) +pipe_height, 1)
            pipe_group.add(bpipe)
            pipe_group.add(tpipe)
            last_pipe = time_now
            if scorecount ==1: scorecount -=1

        scroll -= speed
        if scroll < -12:
            scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
      #  if event.type == VIDEORESIZE:
            #screen = pygame.display.set_mode((event.weight, event,height), pygame.RESIZABLE)
    pygame.display.update()

pygame.QUIT()
