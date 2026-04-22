import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random

class Slideshow:
    def __init__(self, root, folder, num_images, display_time):
        self.root = root
        self.folder = folder
        self.num_images = num_images
        self.display_time = display_time
        self.total_time = self.display_time * self.num_images
        self.images = self.load_images()
        self.index = 0
        self.running = True
        self.timer_id = None

        self.photo_label = tk.Label(root)
        self.photo_label.pack()

        self.timer_label = tk.Label(root, font=("Helvetica", 14))
        self.timer_label.pack()

        btns = tk.Frame(root)
        btns.pack()
        tk.Button(btns, text="⏮ Back", command=self.go_back).pack(side="left")
        tk.Button(btns, text="⏸ Pause", command=self.toggle_pause).pack(side="left")
        tk.Button(btns, text="⏭ Skip", command=self.next_image).pack(side="left")

        self.remaining_time = self.display_time
        self.show_image()

    def load_images(self):
        supported_ext = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
        all_files = [
            os.path.join(self.folder, f)
            for f in os.listdir(self.folder)
            if f.lower().endswith(supported_ext)
        ]
        if len(all_files) < self.num_images:
            print("Warning: Not enough unique images available.")
        return random.sample(all_files, min(self.num_images, len(all_files)))

    def reset_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        self.remaining_time = self.display_time
        self.timer_label.config(text=f"{self.remaining_time}s")

    def show_image(self):
        if not self.images:
            self.photo_label.config(text="No images found.")
            return

        img_path = self.images[self.index]
        img = Image.open(img_path)
        img.thumbnail((800, 500), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)

        self.photo_label.configure(image=tk_img)
        self.photo_label.image = tk_img
        self.root.title(f"{self.index + 1}/{self.num_images}")

        self.reset_timer()
        if self.running:
            self.schedule_timer()

    def next_image(self):
        self.reset_timer()
        if self.index < self.num_images - 1:
            self.index += 1
            self.show_image()
        else:
            self.show_grid()

    def go_back(self):
        self.reset_timer()
        if self.index > 0:
            self.index -= 1
            self.show_image()

    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            self.schedule_timer()
        elif self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def schedule_timer(self):
        self.timer_id = self.root.after(1000, self.update_timer)

    def update_timer(self):
        if not self.running:
            return
        self.remaining_time -= 1
        self.timer_label.config(text=f"{self.remaining_time}s")
        if self.remaining_time > 0:
            self.schedule_timer()
        else:
            self.next_image()

    def show_grid(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        if self.num_images <= 10:
            cols = 5
            self.root.update_idletasks()
            canvas_width = self.root.winfo_width()
            max_img_width = canvas_width // cols - 40
            max_img_height = 300
        else:
            cols = 10
            max_img_width = 150
            max_img_height = 150

        for idx, img_path in enumerate(self.images):
            row = idx // cols
            col = idx % cols

            img = Image.open(img_path)
            img.thumbnail((max_img_width, max_img_height), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)

            img_label = tk.Label(scrollable_frame, image=tk_img)
            img_label.image = tk_img
            img_label.grid(row=row * 2, column=col, padx=5, pady=(5, 0))

            idx_label = tk.Label(scrollable_frame, text=str(idx + 1))
            idx_label.grid(row=row * 2 + 1, column=col, pady=(0, 10))


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

        try:
            num_images = int(num_images)
            display_time = int(display_time)
        except ValueError:
            print("Please enter valid numbers.")
            return

        slideshow_root = tk.Toplevel(self.root)
        Slideshow(slideshow_root, folder, num_images, display_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = Launcher(root)
    root.mainloop()
