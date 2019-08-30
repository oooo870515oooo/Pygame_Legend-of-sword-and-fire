import pygame
pygame.init()

sound=pygame.mixer.Sound('se_maoudamashii_onepoint15.wav')
sound.play()

pygame.time.wait(int(sound.get_length())*1000)
