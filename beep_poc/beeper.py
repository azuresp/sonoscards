import pygame
import os.path


#pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)

pygame.mixer.init()

#beepsound = pygame.mixer.Sound(file = 'all-eyes-on-me.ogg')
#beepsound.play()

pygame.mixer.music.load('all-eyes-on-me.mp3')
pygame.mixer.music.play(1)

#def beep():
#    global beepsound
#    beepsound.play()


#beep()
