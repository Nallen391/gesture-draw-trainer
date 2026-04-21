import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
import os

class Launcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Gesture Draw Trainer Launcher")

        tk.Label(root, text="Image Folder:").grid(row=0, column=0, sticky="e")
        self.folder_var = tk.StringVar()
        self.folder_entry = tk.Entry(root, textvariable=self.folder_var, width=40)
        self.folder_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse", command=self.browse_folder).grid(row=0, column=2)

        tk.Label(root, text="Number of Images:").grid(row=1, column=0, sticky="e")
        self.num_images_entry = tk.Entry(root)
        self.num_images_entry.insert(0, "10")
        self.num_images_entry.grid(row=1, column=1)

        tk.Label(root, text="Seconds per Image:").grid(row=2, column=0, sticky="e")
        self.display_time_entry = tk.Entry(root)
        self.display_time_entry.insert(0, "30")
        self.display_time_entry.grid(row=2, column=1)

        tk.Button(root, text="Start Slideshow", command=self.start_slideshow).grid(row=3, column=1, pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_var.set(folder)

    def start_slideshow(self):
        folder = self.folder_var.get()
        num_images = self.num_images_entry.get()
        display_time = self.display_time_entry.get()

        if not folder or not num_images or not display_time:
            print("Please fill out all fields.")
            return

        main_script_path = os.path.join(os.path.dirname(__file__), "main.pyw")

        subprocess.Popen([
        sys.executable,
        main_script_path,
        str(folder),
        str(num_images),
        str(display_time)
    ])

if __name__ == "__main__":
    root = tk.Tk()
    app = Launcher(root)
    root.mainloop()
