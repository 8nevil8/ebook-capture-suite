# Installation Guide

Super simple - just one script does everything!

## macOS / Linux

### Option 1: One Command (Easiest)

Open Terminal and run:
```bash
bash <(curl -fsSL https://raw.githubusercontent.com/8nevil8/ebook-capture-suite/main/ebook-capture.sh)
```

Done! It will:
1. Check Python installation
2. Download everything
3. Install dependencies
4. Create desktop shortcut
5. Run the tool

### Option 2: Download First

1. [Download ebook-capture.sh](https://raw.githubusercontent.com/8nevil8/ebook-capture-suite/main/ebook-capture.sh) (right-click → Save As)
2. Open Terminal in download folder
3. Run: `bash ebook-capture.sh`

## Windows

1. [Download ebook-capture.bat](https://raw.githubusercontent.com/8nevil8/ebook-capture-suite/main/ebook-capture.bat) (right-click → Save As)
2. Double-click the file

Done! It will:
1. Check Python installation
2. Download everything
3. Install dependencies
4. Create desktop shortcut
5. Run the tool

## Requirements

### Python 3.7+

**Check if installed:**

macOS/Linux:
```bash
python3 --version
```

Windows:
```cmd
python --version
```

**Install if needed:**
- [Download Python](https://www.python.org/downloads/)
- Windows: ✅ Check "Add Python to PATH" during installation

## macOS: Grant Permission

First time only - when you run the tool:

1. **System Preferences** → **Security & Privacy** → **Privacy**
2. Select **Screen Recording**
3. Check ✅ **Terminal**
4. Restart Terminal
5. Run `bash ebook-capture.sh` again

## Next Time

After installation, just use the desktop shortcut:
- **macOS**: Double-click `eBook-Capture.command` on Desktop
- **Windows**: Double-click `eBook Capture.bat` on Desktop

## Files Location

Everything is installed to:
- **macOS/Linux**: `~/ebook-capture-suite/`
- **Windows**: `C:\Users\<you>\ebook-capture-suite\`

## Update

To get the latest version, just run the script again:
```bash
bash ebook-capture.sh
```

It will replace the old version with the new one.

## Troubleshooting

### "Python is not installed"

Install Python first:
- [python.org](https://www.python.org/downloads/)
- Windows: Check "Add Python to PATH" ✅

### "curl: command not found" (macOS)

Use Option 2 (Download First) instead.

### Windows: "Cannot be loaded because running scripts is disabled"

Right-click `ebook-capture.bat` → "Run as administrator"

### "Permission denied" (macOS)

Make script executable:
```bash
chmod +x ebook-capture.sh
bash ebook-capture.sh
```

That's it! Super simple.
