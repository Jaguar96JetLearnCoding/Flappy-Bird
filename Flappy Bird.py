import pygame
import random
pygame.init()
WIDTH=864
HEIGHT=768
TITLE="Flappy Bird"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
bird_up=pygame.image.load("Flappy Bird wings down.png")
bird_level=pygame.image.load("Flappy Bird wings level.png")
bird_down=pygame.image.load("Flappy Bird wings up.png")
pole=pygame.image.load("Flappy Pole.png")
floor=pygame.image.load("Flappy Floor surface.png")
background=pygame.image.load("Flappy background.png")
font=pygame.font.SysFont("Impact",50)
last_pole=pygame.time.get_ticks()
pole_duration=3000

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images=[bird_up,bird_level,bird_down]
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vy=0
        self.wing_pos=1
        self.count=0
    def update(self):
        self.count=self.count+1
        if self.count>20:
            self.count=0
            self.index=self.index+self.wing_pos
            if self.index==2:
                self.wing_pos=-1
            if self.index==0:
                self.wing_pos=1
            self.image=self.images[self.index]
            self.vy=self.vy+0.5
        self.rect.y=self.rect.y+self.vy
    
bird=Bird(300,400)
birdgroup=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
birdgroup.add(bird)
all_sprites.add(bird)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,x,y,position):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        if position=="up":
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=(x,y)
        else:
            self.rect.x=x
            self.rect.y=y
    def update(self):
        self.rect.x-=4
        if self.rect.x<=-78:
            self.kill()


            


floor_x=0
obstaclegroup=pygame.sprite.Group()
run=True
while run==True:
    screen.blit(background,(0,0))
    birdgroup.draw(screen)  
    obstaclegroup.draw(screen)
    obstaclegroup.update()
    bird.update()
    screen.blit(floor,(floor_x,700))
    floor_x=floor_x-1
    if floor_x<=-36:
        floor_x=0
    time_now=pygame.time.get_ticks()
    if time_now-last_pole>pole_duration:
      y=random.randint(0,200)
      obstacle=Obstacle(pole,864,320+y,"down")
      obstacle_up=Obstacle(pole,864,120+y,"up")
      obstaclegroup.add(obstacle)
      obstaclegroup.add(obstacle_up)
      all_sprites.add(obstacle)
      all_sprites.add(obstacle_up)
      last_pole=time_now
      if bird.y<=0:
          run=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                bird.vy=-2.50
        if event.type==pygame.MOUSEBUTTONDOWN:
            bird.vy=-2.50
    pygame.display.update()