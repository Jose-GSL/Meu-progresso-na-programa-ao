'''import pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

import miniaudio # type: ignore
import time

stream = miniaudio.stream_file('ex021.mp3')
device = miniaudio.PlayblackDevice()
device.starrt(stream)

time.sleep(10)
device.close()