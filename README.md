# eBook Capture Suite

A simple tool for macOS and Windows that captures book pages from your browser and converts them into clean PDF files.

## What It Does

1. **Captures** screenshots of book pages from your browser automatically
2. **Processes** images to remove browser UI and navigation
3. **Creates** a clean PDF file ready to read

## Quick Start

### macOS/Linux

1. **Download** this repository (click "Code" → "Download ZIP" and extract)
2. **Run** the launcher script:
   ```bash
   ./run.sh
   ```
   That's it! The script will install everything needed and start the tool.

### Windows

1. **Download** this repository (click "Code" → "Download ZIP" and extract)
2. **Double-click** `run.bat`

   That's it! The batch file will install everything needed and start the tool.

## First Time Setup

### macOS Only - Grant Screen Recording Permission

1. Open **System Preferences** → **Security & Privacy** → **Privacy**
2. Select **Screen Recording**
3. Enable permission for **Terminal**
4. Restart Terminal

### Windows

No setup needed! Just run `run.bat`

## Requirements

- **Python 3.7+** ([Download here](https://www.python.org/downloads/))
  - Windows: Make sure to check "Add Python to PATH" during installation
- **Internet connection** (for first-time dependency installation)

## How To Use

1. Run the launcher (`./run.sh` or `run.bat`)
2. Select option **1** for full workflow
3. Open your book in browser, go to first page
4. Enter total number of pages
5. Wait 15 seconds, then automatic capture begins
6. Review and confirm the crop area
7. Enter book title
8. Done! Your PDF is ready

## Where Files Are Saved

- **Screenshots**: `~/Documents/ebook_suite/` (or `C:\Users\<you>\Documents\ebook_suite\` on Windows)
- **PDFs**: `~/Documents/ebooks/` (or `C:\Users\<you>\Documents\ebooks\` on Windows)

You can choose a different location when prompted.

## Troubleshooting

### "Python is not installed"
- Download Python from [python.org](https://www.python.org/downloads/)
- Windows: Check "Add Python to PATH" during installation

### macOS: Screenshots are blank
- Grant Screen Recording permission (see setup above)
- Restart Terminal after granting permission

### Windows: "pygetwindow not installed" message
- This is optional - the tool works without it
- It will capture full screen instead of just the window
- Still works perfectly!

## What's In The Menu

When you run the tool, you'll see:

1. **Full workflow** - Capture and create PDF in one go (recommended)
2. **Capture only** - Just take screenshots
3. **Process only** - Convert existing screenshots to PDF
4. **Exit**

## Support

- Works on: macOS 10.14+, Windows 10/11
- For issues: [Create an issue on GitHub](https://github.com/8nevil8/ebook-capture-suite/issues)

## License

MIT License - See [LICENSE](LICENSE) file
