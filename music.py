import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("music player")
        self.root.geometry("300x200")
        self.is_playing = False

        mixer.init()
        self.folder_label = tk.Label(root, text="Select Folder:")
        self.folder_label.pack() 

        self.folder_entry = tk.Entry(root, width=30)
        self.folder_entry.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.browse_button.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder_path)

    def play_music(self):
        folder_path = self.folder_entry.get()
        if folder_path:
            for filename in os.listdir(folder_path):
                if filename.endswith(".mp3"):
                    mixer.music.load(os.path.join(folder_path, filename))
                    mixer.music.play()
                    self.is_playing = True
                    break
            else:
                print("No MP3 files found in the selected folder.")

    def pause_music(self):
        if self.is_playing:
            mixer.music.pause()
            self.is_playing = False

    def stop_music(self):
        mixer.music.stop()
        self.is_playing = False

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()