print("[Slideshow.py] Module loaded")
import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
import os

class Slideshow:
    from PIL import Image, ImageTk

    def __init__(self, root, images, display_time):
        print("[Slideshow] Initializing slideshow...")
        print(f"[Slideshow] Number of images: {len(images)}")
        print(f"[Slideshow] Display time: {display_time}")
        print(f"[Slideshow] Root is: {root}")
        self.root = root
        self.images = images
        self.num_images = len(images)
        self.index = 0
        self.running = True
        self.display_time = display_time
        self.timer_id = None

        self.photo_label = tk.Label(root)
        self.photo_label.pack()
        self.timer_label = tk.Label(root, font=("Helvetica", 14))
        self.timer_label.pack()
        self.remaining_time = self.display_time // 1000
        self.timer_label.config(text=f"{self.remaining_time}s")  # Show immediately
            


        # Buttons
        btns = tk.Frame(root)
        btns.pack()
        tk.Button(btns, text="⏮ Back", command=self.go_back).pack(side="left")
        tk.Button(btns, text="⏸ Pause", command=self.toggle_pause).pack(side="left")
        tk.Button(btns, text="⏭ Skip", command=self.next_image).pack(side="left")

        self.show_image()
        self.remaining_time = DISPLAY_TIME // 1000
        self.update_timer()


    def show_image(self):
        img_path = self.images[self.index]
        img = Image.open(img_path)

        # Resize while keeping aspect ratio
        img.thumbnail((800, 500), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)

        self.photo_label.configure(image=tk_img)
        self.current_image = tk_img  # Prevent garbage collection
        self.root.title(f"{self.index + 1}/{self.num_images}")

        # Reset and show the timer
        self.timer_label.config(text=f"{self.remaining_time}s")

        if self.running:
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None
            self.schedule_timer()



    def next_image(self):
        if self.index < self.num_images - 1:
            self.index += 1
            self.remaining_time = self.display_time // 1000
            self.show_image()
        else:
            self.show_grid()  # Show grid when done
            self.show_image()

    def go_back(self):
        if self.index > 0:
            self.index -= 1
            self.remaining_time = self.display_time // 1000
            self.show_image()

    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            self.show_image()
        else:
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None

    def show_grid(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # === Set up scrollable canvas ===
        canvas = tk.Canvas(self.root)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

      # === Display images in grid ===
        if self.num_images <= 10:
            cols = 5
            rows = 2

            # Use root width to size thumbnails nicely
            self.root.update_idletasks()  # Ensure width is up-to-date
            canvas_width = self.root.winfo_width()
            max_img_width = canvas_width // cols - 40  # adjust for padding/margins
            max_img_height = 300  # arbitrary vertical cap
        else:
            cols = 10
            max_img_width = 150
            max_img_height = 150

        for idx, img_path in enumerate(self.images[:self.num_images]):
            row = idx // cols
            col = idx % cols

            # Load and resize image
            img = Image.open(img_path)
            img.thumbnail((max_img_width, max_img_height), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)

            # Image label
            img_label = tk.Label(scrollable_frame, image=tk_img)
            img_label.image = tk_img
            img_label.grid(row=row * 2, column=col, padx=5, pady=(5, 0))

            # Index number
            idx_label = tk.Label(scrollable_frame, text=str(idx + 1))
            idx_label.grid(row=row * 2 + 1, column=col, pady=(0, 10))


    def schedule_timer(self):
        if self.remaining_time > 0 and self.running:
            self.timer_id = self.root.after(1000, self.update_timer)

    def update_timer(self):
        if self.running:
            self.remaining_time -= 1
            self.timer_label.config(text=f"{self.remaining_time}s")
            if self.remaining_time > 0:
                self.schedule_timer()
            else:
                self.next_image()

