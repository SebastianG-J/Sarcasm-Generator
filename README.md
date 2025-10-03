# 🧠 What it does

You type something normal like:
```css
I really love Python programming
```
And it gives you:
```css
i ReAlLy LoVe PyThOn PrOgRaMmInG 🤡
```

🚀 Features
- 🪄 Random capitalization
- 🤡 Clown emoji at the end
- 🧠 GUI built with Tkinter (no terminal needed)
- ⚡ Works on Windows, macOS, and Linux
- 🖱️ One click to generate sarcasm
- 🪟 Can be turned into a .exe app for instant access

## 1. 💻 Run it locally

### Clone or download the repo

```bash
git clone https://github.com/<your-username>/sarcasm-generator.git
cd sarcasm-generator
```

## 2. Run the app

```bash
python sarcasm_gui.py
```
That’s it! The window will pop up instantly.

## 🪟 Create a one-click app (Windows)

You can turn it into a standalone .exe file so it runs without Python.

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole sarcasm_gui.py
```

After building, check your dist/ folder for:
```bash
dist/
 └── sarcasm_gui.exe
```

Now you can:

- Pin it to your taskbar
- Add a desktop shortcut
- Rickroll your friends with sarcasm
