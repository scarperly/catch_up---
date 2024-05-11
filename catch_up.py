from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'),(700, 500))

x1 = 100
y1 = 300

x2 = 300
y2 = 300

speed = 10
biba = transform.scale(image.load('sprite1.png'),(100,100))
boba = transform.scale(image.load('sprite2.png'),(100,100))


run = True
clock = time.Clock()
FPS = 60

while run: 
    window.blit(background, (0,0))
    window.blit(biba, (x1, y1))
    window.blit(boba, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            run = False 
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    
    display.update()
    clock.tick(FPS)
    