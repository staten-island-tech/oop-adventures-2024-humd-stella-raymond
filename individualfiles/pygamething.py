import time
import pygame

pygame.init()  # Initialize all pygame modules
pygame.mixer.init()  # Initialize mixer

# Load your own music file
pygame.mixer.music.load("audio-_1_.ogg")  # Replace with the name of your music file

pygame.mixer.music.set_volume(0.4)

# Play the background music (looping indefinitely, from 0-1.0)
pygame.mixer.music.play(-1, 0.0)

# Keep the program running while music plays
while True:
    time.sleep(1)


#THANKS CHATGPT