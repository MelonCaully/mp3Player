import pygame
import tkinter as tk
from tkinter import filedialog
import os

pygame.init()
pygame.mixer.init()

def choose_and_play():
    filepath = filedialog.askopenfilename(
        title="Choose an MP3 file",
        filetypes=[("MP3 Files", "*.mp3")])
    pygame.mixer.music.load(os.path.abspath(filepath))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def set_volume(val):
    volume = float(val)/100
    pygame.mixer.music.set_volume(volume)

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def display_name():
    pass