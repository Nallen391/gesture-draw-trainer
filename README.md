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

## Setting It Up on a New Computer

See `main_folder/How to import to a new computer .txt` for step-by-step notes.

Short version:
1. Clone or download the repo from https://github.com/Nallen391/gesture-draw-trainer
2. On Windows: run the `.exe` directly from `main_folder/dist/`
3. On Mac/Linux: install Python + Pillow (`pip install -r requirements.txt`), then run `python Safe_Launcher.pyw`

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
