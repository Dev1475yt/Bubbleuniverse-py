import pygame as pg
import math as m

n = 74
r = m.tau/235
x, y, v, t, scale = 0, 0, 0, 0, 200
offsetX = 400
offsetY = 400

def clamp(mi,mx,v):
    return max(mi,min(v,mx))

scrn = pg.display.set_mode((800,800), pg.RESIZABLE)
pg.display.set_caption("Bubble Universe")

run = True

while run:
    offsetX = int(pg.display.get_surface().get_size()[0]/2)
    offsetY = int(pg.display.get_surface().get_size()[1]/2)
    scale = min(offsetX,offsetY)/2
    scrn.fill((0,0,0))
    for i in range(n+1):
        for j in range(n+1):
            u = m.sin(i+v)+m.sin(r*i+x)
            v = m.cos(i+v)+m.cos(r*i+x)
            x = u+t
            scrn.set_at((int(u*scale)+offsetX,int(v*scale)+offsetY),(clamp(0,255,2*i),clamp(0,255,2*j),clamp(0,255,i-j)))
    t += 0.005
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
                pg.quit()
