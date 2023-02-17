import pygame
import asyncio
import random
import os
import time
#This is only meant for exporting to web, exporting to desktop with asyncio causes the program to be flagged as a virus
from objects import *
#Game version 1.0.0
pygame.init()

Window = pygame.display.set_mode((960, 540))
Screen = Window.copy()
pygame.display.set_caption("SpeedCube")
pygame.display.set_icon(WindowIcon().Image)

Background = BackgroundImage()
Player = SpeedCube()

LargeFont = pygame.font.Font('./RalewayBold.ttf', 75)
MediumFont = pygame.font.Font('./RalewayBold.ttf', 50)
SmallFont = pygame.font.Font('./RalewayBold.ttf', 30)

Clock = pygame.time.Clock()

pygame.mixer.music.load('./Audio/BackgroundMusic.ogg')
pygame.mixer.music.play(-1, 0.0, 500)
PlayerDeath = pygame.mixer.Sound('./Audio/PlayerDeath.wav')
GameStart = pygame.mixer.Sound('./Audio/GameStart.wav')

Platforms = []

for i in range(15): Platforms.append(PlatformBase())

for Platform in Platforms:
    Platform.Speed = random.randint(250, 375)
    Platform.X = random.randint(960, 1460)
    Platform.Y = 450

Player.X = 147
Player.Y = 80
StartPlatform = PlatformBase()
StartPlatform.X = 120
StartPlatform.Y = 90
StartPlatform.Speed = 75
Platforms.append(StartPlatform)

async def Game():
    Running = True
    Grounded = False
    BackgroundColor = (151, 151, 151)
    Gravity = 100
    Score = 0
    ScoreH = False
    ScoreStart = 0
    ScoreCurrent = 0
    Title = True
    HighScore = 0
       
    while Running:
        DeltaTime = Clock.tick(60) / 1000

        if Title:
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                GameStart.play()
                Title = False
                Player.X = 147
                Player.Y = 90
                Player.YForce = 0
                Grounded = False
                ScoreH = False
                for Platform in Platforms:
                    Platform.X = random.randint(960, 1460)
                    Platform.Speed = random.randint(250, 375)
                Platforms[15].X = 120
                Platforms[15].Y = 90
                Platforms[15].Speed = 65
                Player.Dead = False
        
        if not Title:
            if ScoreH == False:
                ScoreH = True
                ScoreStart = int(time.time())
        
            ScoreCurrent = int(time.time())
            Score = ScoreCurrent - ScoreStart
        
            if Score > HighScore:
                HighScore = Score
        
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                if not pygame.key.get_pressed()[pygame.K_LEFT]:
                    Player.X += int(625 * DeltaTime)
        
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                if not pygame.key.get_pressed()[pygame.K_RIGHT]:
                    Player.X -= int(625 * DeltaTime)
        
            for Platform in Platforms:
                Platform.X -= int(Platform.Speed * DeltaTime)
                if Platform.X < -64:
                    Platform.Speed = random.randint(375, 500)
                    Platform.X = random.randint(960, 1460)

                Platform.Rect = Platform.Image.get_rect(topleft=(Platform.X, Platform.Y))
            
                if Player.Rect.colliderect(Platform.Rect):
                    if Player.Falling == False:
                        Player.Y = Platform.Y - 9
                        Grounded = True

            if pygame.key.get_pressed()[pygame.K_UP]:
                if Grounded == True:
                    Grounded = False
                    Player.YForce -= int(875 * DeltaTime)
                    Player.Falling = False

            if Platforms[15].X <= -64:
                if Platforms[15].Speed == 65:
                    Platforms[15].Speed = random.randint(250, 375)
                    Platforms[15].Y = 450

            if not Player.Rect.colliderect(Platforms[0].Rect):
                if not Player.Rect.colliderect(Platforms[1].Rect):
                    if not Player.Rect.colliderect(Platforms[2].Rect):
                        if not Player.Rect.colliderect(Platforms[3].Rect):
                            if not Player.Rect.colliderect(Platforms[4].Rect):
                                if not Player.Rect.colliderect(Platforms[5].Rect):
                                    if not Player.Rect.colliderect(Platforms[6].Rect):
                                        if not Player.Rect.colliderect(Platforms[7].Rect):
                                            if not Player.Rect.colliderect(Platforms[8].Rect):
                                                if not Player.Rect.colliderect(Platforms[9].Rect):
                                                    if not Player.Rect.colliderect(Platforms[10].Rect):
                                                        if not Player.Rect.colliderect(Platforms[11].Rect):
                                                            if not Player.Rect.colliderect(Platforms[12].Rect):
                                                                if not Player.Rect.colliderect(Platforms[13].Rect):
                                                                    if not Player.Rect.colliderect(Platforms[14].Rect):
                                                                        if not Player.Rect.colliderect(Platforms[15].Rect):
                                                                            Grounded = False

            if Grounded == True:
                Gravity = 0
            else:
                Gravity = 100

            if Player.Y < 530:
                if Grounded == False:
                    Player.YForce += int(Gravity * DeltaTime)
                else:
                    Player.YForce = 0
            elif Player.Y > 530:
                Player.Dead = True
        
            if Player.X < -9:
                Player.Dead = True

            if Player.YForce > 25:
                Player.YForce = 25

            if Player.YForce > 0:
                Player.Falling = False
            else:
                Player.Falling = True

            Player.Y += Player.YForce
            Player.Rect = Player.Image.get_rect(topleft=(Player.X, Player.Y))
            ScoreText = MediumFont.render("Current Score: " + str(Score), True, (255, 255, 255))

            if Player.Dead:
                PlayerDeath.play()
                Title = True

        Screen.fill(BackgroundColor)
        Screen.blit(Background.Top, (0, -15))
        Screen.blit(Background.Bottom, (0, 390))
        
        if not Title:
            Screen.blit(Player.Image, Player.Rect)
        
            for Platform in Platforms:
                if Platform.X < 960:
                    Screen.blit(Platform.Image, Platform.Rect)
            
            HighScoreText = SmallFont.render("High Score: " + str(HighScore), True, (255, 255, 255))
            Screen.blit(HighScoreText, (55, 50))
            Screen.blit(ScoreText, (50, 5))
        else:
            TitleText = LargeFont.render("SpeedCube", True, (255, 255, 255))
            StartText = SmallFont.render("Enter to Start", True, (255, 255, 255))
            Screen.blit(TitleText, (270, 100))
            Screen.blit(StartText, (380, 225))
    
        Window.blit(pygame.transform.scale(Screen, Window.get_rect().size), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        
        if not Running:
            pygame.quit()
            return
        
        await asyncio.sleep(0)

asyncio.run(Game())
