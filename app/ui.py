import tkinter as tk
from player import set_volume, choose_and_play, stop_music, pause, resume

root = tk.Tk()
root.name = "MP3 Player"

# Create and pack the buttons
play_button = tk.Button(root, text="Choose & Play", command=choose_and_play)
play_button.grid(columnspan=3, row=0)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.grid(column=0, row=1, pady=10, padx=5)

pause_button = tk.Button(root, text="Pause", command=pause)
pause_button.grid(column=1, row=1, pady=10, padx=5)

resume_button = tk.Button(root, text="Resume", command=resume)
resume_button.grid(column=2, row=1, pady=10, padx=5)

# Create and pack the slider
volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="volume", command=set_volume)
volume_slider.set(50)
volume_slider.grid(columnspan=3, row=2)

root.mainloop()