import pygame
#Mixer Inicialization
pygame.mixer.init()
#Pygame Inicialization
pygame.init()
pygame.mixer.music.load("27 — music.mp3")
pygame.mixer.music.play()
pygame.event.wait()
