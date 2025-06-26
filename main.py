import pygame
import time
import os

def main():
    print("Playing Song...")
    filepath = os.path.abspath("media/cyanide.mp3")
    
    pygame.init()
    pygame.mixer.init()
    print("Mixer init:", pygame.mixer.get_init())
    
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    main()