import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()

    pygame.draw.rect(screen,(255,0,0),pygame.Rect(30,30,60,60))          
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(100,100,60,60))          
    pygame.draw.circle(screen,(0,255,0),(200,200),50)
    pygame.draw.circle(screen,(0,255,0),(200,300),50,3)
    pygame.display.flip()        
