import pygame

class WindowIcon():
    def __init__(self):
        self.Image = pygame.image.load('./Sprites/Icon.png')
        self.Image.convert()

class BackgroundImage():
    def __init__(self):
        self.Top = pygame.image.load('./Sprites/BackgroundTop.png')
        self.Bottom = pygame.image.load('./Sprites/BackgroundBottom.png')
        self.Top.convert_alpha()
        self.Bottom.convert_alpha()

class SpeedCube():
    X = 0
    Y = 0
    YForce = 0
    Dead = False
    Falling = False

    def __init__(self):
        self.Image = pygame.image.load('./Sprites/Player.png')
        self.Rect = self.Image.get_rect(topleft=(self.X, self.Y))
        self.Image.convert()

class PlatformBase():
    X = 0
    Y = 0
    Speed = 0
    CollideX = 0
    Once = False
    
    def __init__(self):
        self.Image = pygame.image.load('./Sprites/Platform.png')
        self.Rect = self.Image.get_rect(topleft=(self.X, self.Y))
        self.Image.convert()