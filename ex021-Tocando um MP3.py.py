import pygame
pygame.init()
pygame.mixer.music.load('1107.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

import playsound

playsound.playsound('1107.mp3')