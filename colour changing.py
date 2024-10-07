import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
white=(255,255,255)
red=(255,0,0)
w=60
h=40
rect_x=400//2-w//2
rect_y=400//2-h//2
velocity=5
clock=pygame.time.Clock()

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
    
      rect_speed_x = -velocity

    elif keys[pygame.K_RIGHT]:

     rect_speed_x = velocity

    else:

      rect_speed_x = 0

    if keys[pygame.K_UP]:

      rect_speed_y = -velocity

    elif keys[pygame.K_DOWN]:

     rect_speed_y = velocity

    else:

      rect_speed_y = 0

# Update rectangle position

    rect_x += rect_speed_x

    rect_y += rect_speed_y

# Check for collisions with window borders (bounce effect)

    if rect_x <= 0 or rect_x + w>= 200:

      rect_speed_x = -rect_speed_x

    if rect_y <= 0 or rect_y + h >=200:

     rect_speed_y = -rect_speed_y

# Fill screen with white

    screen.fill(white)

# Draw the rectangle

    pygame.draw.rect(screen, red, (rect_x, rect_y, w, h))

    pygame.display.flip()        
    
