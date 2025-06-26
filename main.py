import pygame
import time
import os

def main():
    filepath = os.path.abspath("media/cyanide.mp3")
    print("Playing", os.path.basename(filepath)[:-4].title())
    
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    main()