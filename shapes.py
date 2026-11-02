import pygame

pygame.init()
screen=pygame.display.set_mode([500,500])
screen.fill("Red")
position=(300,300)
raduis=50
wid=2

pygame.draw.circle(screen,"blue",position,raduis,wid)
class myCircle():
    def __init__(self,colour, pos, rad, wid=0):
        self.colour=colour
        self.pos=pos
        self.rad=rad
        self.wid=wid
        self.screen=screen
    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.pos,self.rad,self.wid)
    def grow(self,r):
        self.rad = self.rad+r
        pygame.draw.circle(self.screen,self.colour,self.pos,self.rad,self.wid)
yellowCircle=myCircle("yellow",position,raduis+45,2)
blueCircle=myCircle("blue",position,raduis+60,4)
greenCircle=myCircle("green",position,raduis+80,3)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            yellowCircle.draw()
            blueCircle.draw()
            greenCircle.draw()
        if(event.type == pygame.MOUSEBUTTONUP):
            yellowCircle.grow(1)
            blueCircle.grow(2)
            greenCircle.grow(3)