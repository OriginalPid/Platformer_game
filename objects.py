from settings import *


class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.width = width 
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, images):
        self.width = width
        self.height = height
        self.images = images
        self.anim_count = 0
        self.image = pygame.transform.scale(self.images[self.anim_count], (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__( x, y, width, height, speed, images)

        self.action = "idle"
        self.animations = {
            "idle": list(range(4)),
            "right": list(range(4, 10)),
            "left": list (range(10, 17))
        }

    def update(self):
        frames = self.animations[self.action] # [0, 1, 2, 3]
        self.anim_count += 1
        if self.anim_count >= len(frames) - 1:
            self.anim_count = 0
        self.image = pygame.transform.scale(self.images[frames[self.anim_count]], (self.width, self.height))
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            self.action = "left"
            self.rect.x -= self.speed
        elif keys_pressed[pygame.K_d]:
            self.action = "right"
            self.rect.x += self.speed
        else:
            self.action = "idle"
