import pygame

pygame.init()
screen=pygame.display.set_mode([500,500])
screen.fill("Red")
position=(300,300)
raduis=50
wid=2

pygame.draw.rect(screen, "blue", (250, 250, 100, 100), 2)
class myRectangle():
    def __init__(self,colour, pos, rad, wid=0):
        self.colour=colour
        self.pos=pos
        self.rad=rad
        self.wid=wid
        self.screen=screen
    def draw(self):
        pygame.draw.rect(self.screen, self.colour, (self.pos[0] - self.rad//2, self.pos[1] - self.rad//2, self.rad, self.rad), self.wid)
    def grow(self,r):
        self.rad = self.rad + r
        self.draw()
yellowRectangle=myRectangle("yellow",position,raduis+45,2)
blueRectangle=myRectangle("blue",position,raduis+60,4)
greenRectangle=myRectangle("green",position,raduis+80,3)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            yellowRectangle.draw()
            blueRectangle.draw()
            greenRectangle.draw()
        if(event.type == pygame.MOUSEBUTTONUP):
            yellowRectangle.grow(1)
            blueRectangle.grow(2)
            greenRectangle.grow(3)