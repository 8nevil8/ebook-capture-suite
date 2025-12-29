# eBook Capture Suite

A comprehensive toolkit for macOS that automates the process of capturing, processing, and converting online book content into clean, high-quality PDF files.

## Overview

This suite provides a simplified workflow to digitize books from online readers:

- **ebook-capture.py** - Single entry point with interactive menu for the complete workflow
- **src/capture.py** - Automated screenshot capture from browser-based book readers
- **src/process.py** - Intelligent image cropping and PDF generation with custom output location

## Features

- **Automated Screenshot Capture**: Captures book pages from browser with configurable page navigation
- **Smart Frame Detection**: Automatically detects and crops out browser UI, navigation panels, and other non-content elements
- **Centralized Storage**: All screenshots stored in `~/Documents/ebook_suite/` for easy access
- **Batch Processing**: Process multiple screenshots at once with progress tracking
- **PDF Generation**: Creates single, searchable PDF files from processed images
- **Custom Output Location**: Save PDFs to any location (defaults to ~/Documents/ebooks)
- **Interactive Workflow**: User-friendly prompts guide you through each step
- **Quality Preservation**: Maintains image quality while removing unnecessary UI elements

## System Requirements

- **OS**: macOS (tested on macOS 10.14+)
- **Python**: 3.7 or higher
- **Dependencies**: Pillow, pyautogui
- **Accessibility**: Screen recording permissions required for screenshot capture

## Quick Start

### Simple Way (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ebook-capture-suite.git
cd ebook-capture-suite

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Run the interactive tool
python3 ebook-capture.py
```

### Advanced Way (Individual Scripts)

```bash
# Run scripts separately for more control
python3 src/capture.py    # Capture screenshots
python3 src/process.py    # Process and create PDF
```

## Installation

See [docs/installation.md](docs/installation.md) for detailed installation instructions.

## Usage

### Interactive Mode (Recommended)

```bash
python3 ebook-capture.py
```

The interactive menu offers three options:

1. **Full workflow** - Captures screenshots, then processes them into a PDF (automated)
2. **Capture only** - Just capture screenshots for later processing
3. **Process only** - Process existing screenshots from previous captures

### Manual Mode (Advanced)

#### Step 1: Capture Book Pages

```bash
python3 src/capture.py
```

- Prompts for total number of pages
- Calculates required screenshots (2 pages per screenshot)
- Waits 15 seconds for browser focus
- Automatically captures and navigates
- Saves to `~/Documents/ebook_suite/book_YYYYMMDD_HHMMSS/` directory

#### Step 2: Process and Create PDF

```bash
python3 src/process.py
```

- Detects screenshot folders
- Analyzes and previews crop area
- Allows manual adjustment
- Processes all images
- Generates PDF with custom title and output location (defaults to ~/Documents/ebooks)

## Workflow Example

### Using Interactive Mode

```bash
python3 ebook-capture.py

# Select option: 1 (Full workflow)
# Enter: 200 pages
# Wait 15 seconds, then automatic capture runs...
# Press Enter to continue to processing
# Select folder: 1
# Review preview: y
# Create PDF: y
# Enter title: "Advanced Python Programming"
# Output location: [Enter for default ~/Documents/ebooks]

# Result: Clean PDF saved to ~/Documents/ebooks!
```

### Using Individual Scripts

```bash
# Capture
python3 src/capture.py
# Enter: 200 pages

# Process
python3 src/process.py
# Follow prompts...
```

## Directory Structure

```
ebook-capture-suite/
├── ebook-capture.py        # Main entry point (recommended)
├── src/
│   ├── capture.py          # Screenshot capture tool
│   ├── process.py          # Image processing & PDF creation
│   └── __init__.py
├── docs/
│   ├── installation.md     # Detailed installation guide
│   ├── usage.md           # Extended usage documentation
│   └── screenshots/       # Example screenshots
├── examples/              # Example outputs
├── tests/                # Unit tests
├── requirements.txt      # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

## Configuration

### Adjusting Capture Settings

Edit `src/capture.py`:
```python
DELAY_TIMEOUT = 3  # Seconds between page captures
```

### Custom Crop Coordinates

Edit `src/process.py` or use interactive mode:
```python
left_x = 215
top_y = 48
right_x = 2785
bottom_y = 1660
```

## Permissions Required

### macOS Screen Recording Permission

1. Open **System Preferences** > **Security & Privacy** > **Privacy**
2. Select **Screen Recording** from the left sidebar
3. Enable permission for **Terminal** (or your Python environment)
4. Restart Terminal after granting permission

### Accessibility Permission (if needed)

Some features may require Accessibility permissions:
1. **System Preferences** > **Security & Privacy** > **Privacy**
2. Select **Accessibility**
3. Add and enable **Terminal**

## Troubleshooting

### "No book screenshot folders found"
- Ensure you've run `capture.py` first
- Check that folders start with `book_`

### Screenshots are blank or incorrect
- Verify Screen Recording permissions are granted
- Ensure browser window is focused during capture
- Try increasing `DELAY_TIMEOUT` for slower systems

### Crop area is incorrect
- Use the interactive adjustment mode (enter 'a' when prompted)
- Manually specify coordinates based on your screen resolution
- Check the preview image to verify crop boundaries

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

[MIT License](LICENSE)

## Author

Created for efficient book digitization workflows.

## Acknowledgments

- Built with Pillow for image processing
- Uses pyautogui for automation
- Inspired by the need for clean, automated book capture

## Disclaimer

This tool is intended for personal use with content you own or have permission to digitize. Please respect copyright laws and terms of service for online book platforms.
