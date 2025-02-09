from objects import*
from settings import*

level1 = [
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '  ------                                                --------      ',
    '                    ---------                                         ',
    '        --------                   --------                           ',
    '                                                                      ',
    '------                 --------                ----------             ',

]

level1_width = len(level1[0]) * 100
level1_height = len(level1) * 50
level_objects = pygame.sprite.Group()
def draw_level(level:list):
    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 50,platform_image)
                level_objects.add(platform)
            x += 100
        x = 0
        y += 50

    return level_objects 