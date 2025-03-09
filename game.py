from objects import *
from levels import *

pygame.init()

level1_objects, key, chest = draw_level(level1)
player = Player(50, H - 90, 40, 50, 10, player_images)

level1_objects.add(player)

game = True
while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.blit(bg, (0, 0))
    for obj in level1_objects:
        window.blit(obj.image, camera.apply(obj))
    camera.update(player)

    player.update(platforms)

    if pygame.sprite.spritecollide(player,coins, True):
        coins_count += 1

    window.blit(pygame.transform.scale(coin_image, (50, 50)), (10, 10))
    coins_txt = font1.render(f":{coins_count}", True, (200, 100, 122))
    window.blit(coins_txt, (55, 12))

    if pygame.sprite.collide_rect(player, key):
        is_key = True 
        key.rect.x = -200

    if pygame.sprite.collide_rect(player, chest) and is_key:
        coins_count += 10
        chest.rect.x = -300

    pygame.display.update()
    clock.tick(FPS)
