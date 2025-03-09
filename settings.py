import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
is_key =False
coins_count = 0
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Platformer Dino")
pygame.display.set_icon(pygame.image.load("assets/images/player/stand_1.png"))

clock = pygame.time.Clock()
"""ГРУПИ СПРАЙТІВ"""
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

"""КАРТИНКИ СПРАЙТІВ"""
bg = pygame.transform.scale(pygame.image.load("assets/background/level1.png"), (W, H))

platform_image = pygame.image.load("assets/background/platform.png")

player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]

coin_image = pygame.image.load("assets/images/coin/coin.png")
key_image = pygame.image.load("assets/images/key/key.png")
chest_image = pygame.image.load("assets/images/chest/chest.png")

"""ШРИФТИ"""
pygame.font.init()
font1 = pygame.font.Font(None, 50)

