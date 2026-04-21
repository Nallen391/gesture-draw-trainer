import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import os
import random
import sys
print("Args:", sys.argv)
print("Arg count:", len(sys.argv))


# === Get User Input ===
def get_user_settings():
    temp_root = tk.Tk()
    temp_root.withdraw()

    folder = filedialog.askdirectory(title="Select your gesture folder")
    if not folder:
        print("No folder selected.")
        exit()

    num_images = simpledialog.askinteger("Session Length", "How many images to show?", minvalue=1, maxvalue=1000)
    display_time = simpledialog.askinteger("Display Time", "How many seconds per image?", minvalue=1, maxvalue=60) * 1000

    temp_root.destroy()
    return folder, num_images, display_time

# === Collect Images ===
def collect_images(folder):
    print(f"[DEBUG] collect_images received folder: {repr(folder)}")
    images = []

    print(f"[collect_images] Scanning folder: '{folder}'")  # extra quotes to see whitespace issues

    try:
        for file in os.listdir(folder):
            print(f"[collect_images] Checking: {file}")
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(folder, file)
                print(f"[collect_images] Added: {full_path}")
                images.append(full_path)
    except Exception as e:
        print("[collect_images] os.listdir failed:", e)

    try:
        for root_dir, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_path = os.path.join(root_dir, file)
                    if full_path not in images:
                        print(f"[collect_images] Walk added: {full_path}")
                        images.append(full_path)
    except Exception as e:
        print("[collect_images] os.walk failed:", e)

    print(f"[collect_images] Total collected: {len(images)}")
    return images
    print(f"[DEBUG] collect_images received folder: {folder}")
    print(f"[DEBUG] Folder exists: {os.path.exists(folder)}")
    print(f"[DEBUG] Folder is dir: {os.path.isdir(folder)}")


   




# === Slideshow GUI ===
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
        img.thumbnail((800, 600), Image.Resampling.LANCZOS)
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


# === Run App ===
import sys
import os
import random
from tkinter import Tk

print("Args:", sys.argv)

if len(sys.argv) == 4:
    folder = sys.argv[1].strip("'").strip('"')
    print(f"Folder from argv: '{folder}'")
    print(f"Exists? {os.path.exists(folder)}")
    print(f"Is directory? {os.path.isdir(folder)}")

    NUM_IMAGES = int(sys.argv[2])
    DISPLAY_TIME = int(sys.argv[3]) * 1000

    images = collect_images(folder)
    print(f"[DEBUG] Images collected: {len(images)}")

    if len(images) < NUM_IMAGES:
        print("Not enough images.")
        exit()

    random.shuffle(images)
    session_images = images[:NUM_IMAGES]

    root = Tk()
    app = Slideshow(root, session_images, DISPLAY_TIME)
    root.mainloop()

else:
    print("Expected 3 arguments (folder, num_images, display_time).")
    exit()

