# Usage Guide

This comprehensive guide covers all features and use cases for the eBook Capture Suite.

## Table of Contents

1. [Basic Workflow](#basic-workflow)
2. [Interactive Mode: ebook-capture.py](#interactive-mode-ebook-capturepy)
3. [Manual Mode](#manual-mode)
   - [Tool 1: capture.py](#tool-1-capturepy)
   - [Tool 2: process.py](#tool-2-processpy)
4. [Advanced Usage](#advanced-usage)
5. [Tips & Best Practices](#tips--best-practices)
6. [Troubleshooting](#troubleshooting)

## Basic Workflow

The typical workflow consists of two steps:

```
1. Capture → 2. Process
```

### Quick Example - Interactive Mode (Recommended)

```bash
python3 ebook-capture.py
# Select option 1 for full workflow
```

### Quick Example - Manual Mode

```bash
# Step 1: Capture book pages
python3 src/capture.py

# Step 2: Process and create PDF
python3 src/process.py
```

---

## Interactive Mode: ebook-capture.py

### Purpose

The main entry point that provides a user-friendly interactive menu for the entire workflow. This is the recommended way to use the tool for most users.

### How It Works

1. Shows an interactive menu with options
2. Guides you through the complete workflow
3. Handles transitions between capture and processing
4. Optionally loops for processing multiple books

### Step-by-Step Usage

#### Run the Script

```bash
cd /path/to/ebook-capture-suite
python3 ebook-capture.py
```

#### Select an Option

```
📚 eBook Capture Suite
==================================================

What would you like to do?
  1. Full workflow (Capture → Process → PDF)
  2. Capture screenshots only
  3. Process existing screenshots
  4. Exit

Select option (1-4):
```

**Option 1: Full Workflow** (Recommended for new captures)
- Runs capture tool first
- Automatically transitions to processing
- Creates PDF in one session

**Option 2: Capture Only**
- Just captures screenshots
- Useful if you want to review captures before processing
- Offers to process immediately after capture

**Option 3: Process Only**
- Processes existing screenshot folders
- Useful for reprocessing or processing old captures

**Option 4: Exit**
- Quits the application

### Example Session

```
python3 ebook-capture.py

# Select: 1
# Enter pages: 200
# Wait for capture (15 seconds + capture time)
# Press Enter to continue
# Review crop preview: y
# Create PDF: y
# Enter title: "My Book"
# Output directory: [press Enter for default]
# Done!
#
# Process another book? n
```

---

## Manual Mode

For advanced users who want more control, you can run the tools individually.

## Tool 1: capture.py

### Purpose

Automatically captures screenshots of book pages from a browser-based book reader.

### How It Works

1. You specify the total number of pages
2. Script calculates screenshots needed (2 pages per screenshot)
3. Waits 15 seconds for you to focus the browser
4. Takes screenshots and presses right arrow to navigate
5. Saves images with sequential naming

### Step-by-Step Usage

#### 1. Prepare Your Browser

```bash
# Open your book in a browser
# Navigate to the first page or spread
# Maximize or full-screen the browser window
# Ensure the book display shows 2 pages side-by-side
```

#### 2. Run the Script

```bash
cd /path/to/ebook-capture-suite
python3 src/capture.py
```

#### 3. Enter Book Details

```
Enter the total number of pages in the book: 200
```

The script will calculate:
- Total pages: 200
- Pages per screenshot: 2
- Screenshots needed: 100
- Estimated time: ~5 minutes (at 3 seconds per capture)

#### 4. Confirm and Focus

```
This will take approximately 5.0 minutes. Continue? (y/n): y

Screenshots will be saved to: book_20250129_143022
Make sure your browser window is active and on the first page...
Starting in 15 seconds...
```

**During the 15-second countdown:**
- Click on the browser window to focus it
- Ensure the first page is visible
- Don't touch mouse or keyboard after countdown

#### 5. Automated Capture

The script will:
- Take a screenshot
- Press the right arrow key
- Wait 3 seconds for the page to load
- Repeat until all pages are captured

```
Screenshot 1/100 (pages 1-2) - Saved: pages_001-002.png
➡️  Moving to next page spread...
⏳ Waiting 3 seconds for page to load...
Screenshot 2/100 (pages 3-4) - Saved: pages_003-004.png
...
```

#### 6. Stop Early (if needed)

Press `Ctrl+C` to stop the capture at any time:

```
⚠️  Script interrupted by user at screenshot 45
```

### Configuration Options

Edit `src/capture.py` to customize:

```python
# Line 14: Delay between captures
DELAY_TIMEOUT = 3  # Increase for slower page loads

# Line 145: Initial wait time
time.sleep(15)  # Change to give yourself more prep time
```

### Output

Creates a directory: `~/Documents/ebook_suite/book_YYYYMMDD_HHMMSS/`

Contains files:
```
~/Documents/ebook_suite/book_20250129_143022/
├── pages_001-002.png
├── pages_003-004.png
├── pages_005-006.png
...
└── pages_199-200.png
```

All files are stored in `~/Documents/ebook_suite/` for easy navigation and management.

---

## Tool 2: process.py

### Purpose

Processes screenshots by cropping out browser UI and navigation elements, keeping only the book content, and optionally creating a PDF.

### How It Works

1. Detects folders containing screenshots
2. Analyzes first image to find content boundaries
3. Shows preview with crop area highlighted
4. Processes all images with the same crop
5. Optionally creates a single PDF file

### Step-by-Step Usage

#### 1. Run the Script

```bash
python3 src/process.py
```

#### 2. Select Screenshot Folder

If multiple folders exist:

```
📁 Found multiple screenshot folders:
  1. book_20250129_143022
  2. book_20250128_091544

Select folder number: 1
```

#### 3. Review Crop Preview

```
🔍 Analyzing gray frame boundaries using: pages_002-003.png
📸 Preview saved as: pdf_book_20250129_143022/crop_preview.png
🔍 Check the preview - green rectangle shows what will be kept

📏 Detected frame boundaries:
   Left: 215, Top: 48, Right: 2785, Bottom: 1660

Does this frame detection look good? (y/n/a):
```

**Options:**
- `y` - Accept and continue
- `n` - Cancel operation
- `a` - Adjust coordinates manually

#### 4. Manual Adjustment (if needed)

If you select `a`:

```
Enter new coordinates for the frame:
Image size: 2880 x 1800
Left edge (0-2880): 200
Top edge (0-1800): 40
Right edge (200-2880): 2800
Bottom edge (40-1800): 1680

📸 Updated preview saved as: pdf_book_20250129_143022/crop_preview.png
Use this frame? (y/n): y
```

#### 5. PDF Creation

```
📄 Do you want to create a single PDF file? (y/n): y

📚 Enter book title for PDF (or press Enter to skip): Advanced Python Programming
```

#### 6. Processing

```
🔄 Processing 100 images...
📄 Processing 1/100: pages_001-002 - ✅ Created: pages_001-002_frame.png
📄 Processing 2/100: pages_003-004 - ✅ Created: pages_003-004_frame.png
...

✅ Frame cropping completed!
📊 Successfully processed: 100/100 images
📁 Frame content saved in: pdf_book_20250129_143022
🎯 Clean book content extracted from gray frames!
```

#### 7. PDF Generation

```
📄 Creating PDF with 100 pages...
📖 Adding page 1/100: pages_001-002_frame.png
📖 Adding page 2/100: pages_003-004_frame.png
...
💾 Saving PDF: pdf_book_20250129_143022/Advanced_Python_Programming.pdf
✅ PDF created successfully!
📊 Total pages in PDF: 100

🎉 PDF created: Advanced_Python_Programming.pdf
📍 Location: pdf_book_20250129_143022/Advanced_Python_Programming.pdf
```

### Output

Creates directory: `~/Documents/ebook_suite/pdf_book_YYYYMMDD_HHMMSS/`

Contains:
```
~/Documents/ebook_suite/pdf_book_20250129_143022/
├── crop_preview.png                    # Preview showing crop area
├── pages_001-002_frame.png            # Cropped images
├── pages_003-004_frame.png
...
```

Note: The final PDF is saved to the location you specify (defaults to `~/Documents/ebooks/`).

---

## Advanced Usage

### Batch Processing Multiple Books

Using the interactive mode:

```bash
# Just run the tool and select option 1 repeatedly
python3 ebook-capture.py
# The tool will ask "Process another book?" after each completion
```

Using individual scripts:

```bash
# Create a script to process multiple books
for i in {1..5}; do
    echo "Processing book $i"
    python3 src/capture.py
    python3 src/process.py
done
```

### Custom PDF Output Directory

By default, PDFs are saved to `~/Documents/ebooks`. You can change this when prompted:

```
📁 Where should the PDF be saved?
   Default: /Users/yourusername/Documents/ebooks
   Enter path (or press Enter for default): /Users/yourusername/Books/Technical
```

The directory will be created automatically if it doesn't exist.

### Custom Crop Coordinates

For books with consistent layout, hardcode coordinates in `src/process.py`:

```python
# Line 60-64: Modify the analyze_content_frame function
def analyze_content_frame(image_path):
    left_x = 250   # Your custom values
    top_y = 100
    right_x = 2800
    bottom_y = 1700
    return left_x, top_y, right_x, bottom_y
```

### Adjusting Capture Speed

For faster internet/systems:

```python
# src/capture.py, line 14
DELAY_TIMEOUT = 2  # Faster capture
```

For slower systems:

```python
DELAY_TIMEOUT = 5  # More time for pages to load
```

### Single Page Capture

If your book shows 1 page at a time, modify calculation:

```python
# src/capture.py, line 37
iterations = total_pages  # Changed from (total_pages + 1) // 2
```

### PDF Quality Settings

Modify PDF resolution in `src/process.py`:

```python
# Line 138
images[0].save(
    output_path,
    "PDF",
    resolution=150.0,  # Increase for better quality (default: 100.0)
    save_all=True,
    ...
)
```

---

## Tips & Best Practices

### Before Capture

1. **Test with a few pages first**: Run capture for 5-10 pages to verify settings
2. **Check page layout**: Ensure book displays 2 pages side-by-side
3. **Close notifications**: Disable system notifications to avoid interruptions
4. **Stable internet**: Ensure good connection for online books
5. **Battery**: Plug in laptop for long capture sessions

### During Capture

1. **Don't touch the computer**: Any interaction can disrupt the process
2. **Disable sleep**: Prevent display from sleeping
3. **Monitor progress**: Keep Terminal visible to watch progress
4. **Note errors**: If captures fail, note which pages

### After Capture

1. **Review screenshots**: Quickly check for missing or blank pages
2. **Check page numbers**: Verify sequential naming is correct
3. **Backup originals**: Keep original screenshots before processing

### Processing Tips

1. **Use preview**: Always check the crop preview before batch processing
2. **Test on one image**: Process a single image first to verify quality
3. **Meaningful titles**: Use descriptive PDF titles for organization
4. **Keep processed folders**: Don't delete until PDF is verified

---

## Troubleshooting

### Capture Issues

**Screenshots are blank**
- Solution: Grant Screen Recording permission in System Preferences
- Restart Terminal after granting permission

**Wrong window captured**
- Solution: Ensure browser is focused and in front
- Wait full 15 seconds before script starts

**Navigation doesn't work**
- Solution: Book reader may not use arrow keys
- Try clicking on the book before capture starts
- Check if reader uses different navigation

**Capture stops unexpectedly**
- Solution: Check internet connection
- Increase DELAY_TIMEOUT for slower page loads
- Disable browser extensions that may interfere

### Processing Issues

**No folders found**
- Solution: Run capture.py first
- Ensure folders start with `book_`
- Run process.py from correct directory

**Crop area incorrect**
- Solution: Use manual adjustment (option 'a')
- Check preview.png to see crop boundaries
- Measure exact coordinates using image viewer

**PDF creation fails**
- Solution: Check available disk space
- Ensure all images are valid PNG files
- Try processing fewer images first

**Images too large/small in PDF**
- Solution: Adjust resolution in process.py
- Modify crop coordinates to include more/less content

### Permission Issues

**Permission denied**
- Solution: Check Screen Recording permissions
- Verify script has execute permissions: `chmod +x`
- Run with appropriate user permissions

---

## Example Workflows

### Workflow 1: Quick Single Book (Interactive Mode)

```bash
python3 ebook-capture.py
# Select: 1 (Full workflow)
# Enter: 150 pages
# Wait for completion
# Press Enter to continue
# Confirm: y
# PDF: y
# Title: "My Book"
# Output: [Enter for default]
# Process another? n
```

### Workflow 2: Quick Single Book (Manual Mode)

```bash
# 1. Start capture
python3 src/capture.py
# Enter: 150 pages

# 2. Wait for completion

# 3. Process immediately
python3 src/process.py
# Select: 1
# Confirm: y
# PDF: y
# Title: "My Book"
# Output: [Enter for default]
```

### Workflow 3: Multiple Books Session (Interactive)

```bash
python3 ebook-capture.py
# Select: 1 (Full workflow)
# Book 1: 200 pages → Process → PDF
# Process another? y
# Book 2: 180 pages → Process → PDF
# Process another? y
# Book 3: 220 pages → Process → PDF
# Process another? n
# All PDFs saved to ~/Documents/ebooks/
```

### Workflow 4: Capture Now, Process Later

```bash
# Option 1: Using interactive mode
python3 ebook-capture.py
# Select: 2 (Capture only)
# Book 1: 200 pages
# Process now? n

# Repeat for more books...

# Later, process all:
python3 ebook-capture.py
# Select: 3 (Process only)
# Process each folder

# Option 2: Using manual mode
# Day 1: Capture multiple books
python3 src/capture.py  # Book 1
python3 src/capture.py  # Book 2
python3 src/capture.py  # Book 3

# Day 2: Process all at once
python3 src/process.py  # Process book 1
python3 src/process.py  # Process book 2
python3 src/process.py  # Process book 3
```

---

## Keyboard Shortcuts

### During Capture
- `Ctrl+C` - Stop capture immediately

### During Processing
- `Ctrl+C` - Cancel at any prompt
- `Enter` - Use default/skip (where applicable)

---

## Output File Naming

### Screenshots
- Pattern: `pages_XXX-YYY.png`
- Example: `pages_001-002.png`, `pages_199-200.png`

### Processed Images
- Pattern: `pages_XXX-YYY_frame.png`
- Example: `pages_001-002_frame.png`

### PDFs
- Pattern: `BookTitle.pdf` or `book_TIMESTAMP_book.pdf`
- Example: `Advanced_Python_Programming.pdf`

---

## Getting More Help

- Check the main [README](../README.md)
- Review [Installation Guide](installation.md)
- Open an issue on GitHub
- Review source code comments for detailed explanations
