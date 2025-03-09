from setting import*


class MapObjects(pygame.sprite.Sprite):#клас об'єктів мап
    def __init__(self,x, y, width, height, image):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#базовий клас для всіх спрайтів
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__()
        self.width = width
        self.height = height
        self.images = images#список з картинками
        self.anim_count = 0#номер анімації
        self.image =  pygame.transform.scale(self.images[self.anim_count], (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):#клас для гравця
    def __init__(self, x, y, width, height, speed, images):
        super().__init__(x, y, width, height, speed, images)

        self.action = "idle"#поточна дія гравця
        self.animations = {#номери анімацій в залежності від дії гравця
            "idle": list(range(4)), # 0, 1, 2, 3
            "right": list(range(4, 10)), # 4, 5, 6 ,7 ,8 ,9 
            "left": list(range(10, 17)) # 10, 11,12, 13, 14, 15, 16

        }

        self.is_jump = False
        self.jump_count = 25
        self.gravity = 2 
        self.on_ground = False
        self.fall = 0


    def update(self, platforms):#оновлення гравця 
        frames = self.animations[self.action] # [0, 1, 2, 3] номери анімації в залежності від дії гравця 
        self.anim_count += 1#перемикає анімацію 
        if self.anim_count >= len(frames) - 1:
            self.anim_count = 0#обнуляємо номер анімаії коли вони закінчились
        self.image =  pygame.transform.scale(self.images[frames[self.anim_count]], (self.width, self.height))

        self.fall += self.gravity
        self.rect.y += self.fall
        
        hit_platforms = pygame.sprite.spritecollide(self, platforms, False)
        if hit_platforms:
            for platform in hit_platforms:
                if self.fall > 0 and self.rect.bottom > platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.fall = 0 
                    self.on_ground = True
        else:
            self.on_ground = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:#рух в ліво 
            self.action = "left"
            self.rect.x -= self.speed
        elif keys_pressed[pygame.K_d]:#рух вправо 
            self.action = "right"
            self.rect.x += self.speed
        else:
            self.action = "idle"#без руху

        if not self.is_jump:
            if keys_pressed[pygame.K_SPACE]:
                if self.on_ground:
                    self.is_jump = True
                    self.fall -= self.jump_count
        else:
                self.is_jump = not self.on_ground
