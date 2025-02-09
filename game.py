from objects import *
from levels import*



pygame.init()

level1_objects = draw_level(level1)

game = True
while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.blit(bg, (0, 0))
    level1_objects.draw(window)

    pygame.display.update()
    clock.tick(FPS)