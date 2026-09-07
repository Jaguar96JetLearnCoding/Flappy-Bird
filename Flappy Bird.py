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
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images=[bird_up,bird_level,bird_down]
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
bird=Bird(300,400)
birdgroup=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
birdgroup.add(bird)
all_sprites.add(bird)
run=True
while run==True:
    screen.blit(background,(0,0))
    birdgroup.draw(screen)
    screen.blit(floor,(0,700))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()