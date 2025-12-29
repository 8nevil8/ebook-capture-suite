# eBook Capture Suite

Automatically capture book pages from your browser and convert them to PDF. Simple one-click installation!

## 🚀 One-Command Install & Run

### macOS / Linux

**Option 1: One Command (Recommended)**
```bash
bash <(curl -fsSL https://raw.githubusercontent.com/8nevil8/ebook-capture-suite/main/ebook-capture.sh)
```

**Option 2: Download and Run**
1. [Download ebook-capture.sh](https://raw.githubusercontent.com/8nevil8/ebook-capture-suite/main/ebook-capture.sh)
2. Open Terminal: `bash ebook-capture.sh`

### Windows

1. [Download ebook-capture.bat](https://raw.githubusercontent.com/8nevil8/ebook-capture-suite/main/ebook-capture.bat)
2. Double-click it

**That's it!** One script does everything:
- ✅ Downloads all files
- ✅ Installs dependencies
- ✅ Creates desktop shortcut
- ✅ Runs the tool automatically

## 📋 Requirements

- **Python 3.7+** - [Download here](https://www.python.org/downloads/)
  - Windows: Check "Add Python to PATH" during install
- Internet connection

## 🎯 How to Use

After installation:

1. **Start the tool**
   - macOS: Double-click `eBook-Capture.command` on Desktop
   - Windows: Double-click `eBook Capture.bat` on Desktop

2. **Select Option 1** (Full workflow)

3. **Open your book** in browser, go to first page

4. **Enter total pages** and wait 15 seconds

5. **Done!** PDF created automatically

## 📁 Where Files Are Saved

- **Screenshots**: `~/Documents/ebook_suite/`
- **PDFs**: `~/Documents/ebooks/` (you can change this)

## 🆘 Troubleshooting

### "Python is not installed"
Download Python from [python.org](https://www.python.org/downloads/)
- Windows: Check "Add Python to PATH" ✅

### macOS: Screenshots are blank
1. System Preferences → Security & Privacy → Privacy → Screen Recording
2. Enable Terminal ✅
3. Restart Terminal

### Windows: "pygetwindow not installed"
- Don't worry! Tool still works
- It captures full screen instead of just window
- Still creates perfect PDFs

## 📖 Full Documentation

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)

## 🔄 Update

To update to the latest version, just run the script again:
- macOS: `bash ebook-capture.sh`
- Windows: Double-click `ebook-capture.bat`

## 💬 Support

- Works on: macOS 10.14+, Windows 10/11
- Issues: [GitHub Issues](https://github.com/8nevil8/ebook-capture-suite/issues)

## 📄 License

MIT License
