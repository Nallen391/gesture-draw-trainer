# Gesture Draw Trainer V1.4

**GitHub Repository:** https://github.com/Nallen391/gesture-draw-trainer

A personal tool for timed gesture drawing practice. It shows you reference photos one at a time with a countdown timer, so you can practice sketching quickly under time pressure — then shows a grid of everything you drew from at the end of the session.

> **Platform:** Windows only (the `.exe` is Windows-specific). Mac/Linux users can run the Python scripts directly — see Option B below.

---

## What It Does

1. You pick a folder of reference images on your computer
2. You set how many images you want to see and how many seconds per image
3. The app shows each image fullscreen with a countdown timer
4. When the timer hits zero, it moves to the next image automatically
5. At the end of the session, all images are shown in a grid so you can review them

Images are shown in **random order** every session.

---

## How to Run It

### Option A — Use the .exe (easiest, no Python needed, Windows only)

1. Open the `main_folder/dist/` folder
2. Double-click **Reference dealer v1.4.exe**
3. The launcher window will open — fill in your settings and click **Start Slideshow**

> **Note:** Some antivirus software may flag PyInstaller-compiled executables from unknown publishers. If Windows Defender blocks it, click "More info" → "Run anyway", or use Option B instead.

### Option B — Run with Python (Mac, Linux, or Windows)

You'll need Python installed (version 3.x) and the Pillow library.

**Install dependencies once:**
```
pip install -r requirements.txt
```

**Then launch the app:**
```
python Safe_Launcher.pyw
```

Or run the slideshow directly with arguments (folder path, number of images, seconds per image):
```
python main.pyw "C:\Your\Image\Folder" 15 30
```

---

## Recommended: Organize Your Reference Library

The app lets you select any folder each session, which means you can build a curated library of reference images and choose exactly what you want to practice that day.

A good folder structure keeps your sessions focused and high quality:

```
Reference Library/
├── Figure Drawing/
│   ├── Full Body/
│   ├── Hands/
│   ├── Feet/
│   ├── Faces/
│   └── Torso/
├── Landscapes/
│   ├── Urban/
│   └── Natural/
├── Weapons & Props/
├── Animals/
└── Clothing & Folds/
```

**How to use it:**
- Point the app at a specific subfolder (e.g. `Hands/`) for targeted practice
- Point it at a parent folder (e.g. `Figure Drawing/`) for a mixed session — the app searches subfolders automatically
- Curate carefully: fewer, better images beats a huge dump of low-quality ones

The more specific your folder, the more focused your session. Practicing hands? Go straight to `Hands/`. Warming up? Use the full `Figure Drawing/` folder.

One of my favorite places for high quality paid referance photos is Proko.com (Tools -> filter: Tool type -> image packs). 
https://www.proko.com/browse/tools?term=&toolTypes=Image%20Pack&specialOffersOnly=false&prokoOriginalOnly=false&freeContentOnly=false&instructorsOnly=true&inProgress=false&savedForLater=false&purchased=false&sort=-trend_score 

I most preffer the packs by Stan Prokopenko, The Mallory, Yoni, Marcia, Ethan, Anthony, Veronica, Ryan, Chanon, Laura, Sekka, and Aaron packs form the core of my own reference dealer. 

---

## The Launcher Window

When you open the app, you'll see three fields:

| Field | What It Does | Default |
|-------|-------------|---------|
| Image Folder | Path to your reference photo folder (use Browse) | — |
| Number of Images | How many images to show in this session | 10 |
| Seconds per Image | How long each image stays on screen | 30 |

Click **Start Slideshow** when ready.

---

## During the Slideshow

- The image fills the window, resized to fit up to 800x600
- The title bar shows your progress (e.g. `3/10`)
- The timer counts down in seconds at the bottom

**Buttons:**

| Button | Action |
|--------|--------|
| ⏮ Back | Go to the previous image |
| ⏸ Pause | Freeze the timer (click again to resume) |
| ⏭ Skip | Jump to the next image immediately |

---

## After the Session

When all images have been shown, a grid review appears:

- Up to 10 images: displayed in a 5-column grid with larger thumbnails
- More than 10 images: displayed in a 10-column grid with smaller thumbnails
- Each thumbnail is numbered so you can identify them
- The window is scrollable if there are many images

---

## Supported Image Formats

`.png` `.jpg` `.jpeg` `.gif` `.bmp`

---

## File Structure

```
gesture_draw_trainer_V1.4/
└── main_folder/
    ├── Safe_Launcher.pyw       ← Launch this to open the config window
    ├── main.pyw                ← Main slideshow logic (called by launcher)
    ├── gesture_draw_trainer.py ← All-in-one alternative version
    ├── slideshow.py            ← Grid review module
    ├── dist/
    │   └── Reference dealer v1.4.exe  ← Run this to launch the app (Windows)
    ├── build/                  ← Local only (gitignored) — PyInstaller artifacts
    └── How to import to a new computer .txt  ← Setup notes
```

---

## Setting It Up on a New Computer — Complete Beginner Guide

Follow whichever path matches your situation.

---

### Windows — Quickest Method (no technical knowledge needed)

**Step 1 — Download the project**

1. Go to https://github.com/Nallen391/gesture-draw-trainer in your web browser
2. Click the green **Code** button near the top right
3. Click **Download ZIP**
4. Once it downloads, find the ZIP file in your Downloads folder
5. Right-click it and select **Extract All**, then click **Extract**
6. You now have a folder called `gesture-draw-trainer-main`

**Step 2 — Run the app**

1. Open the `gesture-draw-trainer-main` folder
2. Open the `main_folder` folder
3. Open the `dist` folder
4. Double-click **Reference dealer v1.4.exe**

If Windows shows a warning saying "Windows protected your PC":
- Click **More info**
- Click **Run anyway**

The app will open. You're ready to go.

---

### Windows — If the .exe Doesn't Work (Python method)

**Step 1 — Download the project** (same as above)

**Step 2 — Install Python**

1. Go to https://www.python.org/downloads/
2. Click the big yellow **Download Python** button
3. Run the installer
4. **Important:** On the first screen of the installer, check the box that says **"Add Python to PATH"** before clicking Install
5. Click **Install Now** and let it finish

**Step 3 — Install the required library**

1. Press the **Windows key**, type `cmd`, and press Enter — this opens a black Command Prompt window
2. Type the following and press Enter (replace the path with wherever you extracted the project):
```
pip install pillow
```
3. Wait for it to finish — you'll see "Successfully installed" when done

**Step 4 — Run the app**

1. Open the `gesture-draw-trainer-main` folder, then `main_folder`
2. Double-click **Safe_Launcher.pyw**

If double-clicking doesn't work:
1. Open Command Prompt again
2. Type `python ` (with a space after), then drag and drop the `Safe_Launcher.pyw` file into the Command Prompt window — it will fill in the path automatically
3. Press Enter

---

### Mac or Linux (Python method)

**Step 1 — Download the project**

1. Go to https://github.com/Nallen391/gesture-draw-trainer
2. Click the green **Code** button → **Download ZIP**
3. Extract the ZIP file (double-click it on Mac)

**Step 2 — Install Python** (if not already installed)

- **Mac:** Go to https://www.python.org/downloads/ and download the Mac installer
- **Linux:** Python is usually pre-installed. Check by opening a Terminal and typing `python3 --version`

**Step 3 — Install the required library**

Open a Terminal and run:
```
pip3 install pillow
```

**Step 4 — Run the app**

In Terminal, navigate to the `main_folder` and run:
```
python3 Safe_Launcher.pyw
```

---

### First Time Using the App

Once the launcher opens:

1. Click **Browse** next to Image Folder and navigate to a folder of images on your computer
2. Set how many images you want to see (start with 10)
3. Set how many seconds per image (30 seconds is a good starting point for gesture drawing)
4. Click **Start Slideshow**

---

## Dependencies

| Package | What it's for | How to install |
|---------|--------------|----------------|
| Python 3.x | Running the scripts | python.org |
| tkinter | The GUI windows | Included with Python |
| Pillow | Loading and resizing images | `pip install -r requirements.txt` |

---

## Quick Troubleshooting

**Images not showing up?**
- Make sure the folder you selected actually contains `.jpg`, `.png`, or similar files
- The app searches the folder and all subfolders automatically

**Antivirus blocking the .exe?**
- Click "More info" → "Run anyway" in Windows Defender, or use `python Safe_Launcher.pyw` instead

**Timer not working / app freezes?**
- Close and relaunch
- If using the `.exe`, try running `Safe_Launcher.pyw` with Python instead

**No .exe in dist folder?**
- Use `python Safe_Launcher.pyw` as an alternative
- To rebuild the exe: run `pyinstaller Launcher.spec` from inside `main_folder/` (requires `pip install pyinstaller`)

---

## License

This project is licensed under **CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)**.

You are free to use, share, and adapt this project, provided that:
- **Attribution** is given (credit the original project and author)
- **Non-commercial** use only — it may not be used for commercial purposes

See the [LICENSE](LICENSE) file for full details.

---

## Credits

Coded with assistance from ChatGPT and [Claude Code](https://claude.ai/code) (Anthropic).

---

*Last updated: April 2026 — V1.4*
