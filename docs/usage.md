# Usage Guide

Simple guide to using eBook Capture Suite.

## Starting the Tool

**macOS/Linux:**
```bash
./run.sh
```

**Windows:**
Double-click `run.bat`

## The Menu

You'll see this menu:

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

## Option 1: Full Workflow (Recommended)

This is the easiest way - does everything in one go.

### Steps:

1. **Select option 1**

2. **Open your book in a browser**
   - Go to the first page
   - Make the window large (maximize if possible)

3. **Enter the total number of pages**
   ```
   Enter the total number of pages in the book: 200
   ```

4. **Wait for the countdown**
   ```
   Starting in 15 seconds...
   ```
   - During these 15 seconds, click on your browser window to focus it
   - Don't touch anything after the countdown!

5. **Automatic capture begins**
   ```
   📸 Screenshot 1/100 (pages 1-2)
   ➡️  Moving to next page spread...
   ```
   - The tool automatically:
     - Takes a screenshot
     - Presses the right arrow key
     - Waits 3 seconds
     - Repeats until done

6. **Review the crop area**
   ```
   Does this frame detection look good? (y/n/a):
   ```
   - Type `y` if it looks good
   - Type `n` to cancel
   - Type `a` to manually adjust coordinates

7. **Create PDF**
   ```
   📄 Do you want to create a single PDF file? (y/n): y
   📚 Enter book title for PDF: My Book Title
   ```

8. **Choose output location**
   ```
   📁 Where should the PDF be saved?
      Default: /Users/you/Documents/ebooks
      Enter path (or press Enter for default):
   ```
   - Press Enter to use default
   - Or type a custom path

9. **Done!**
   ```
   🎉 PDF created: My_Book_Title.pdf
   📍 Location: /Users/you/Documents/ebooks/My_Book_Title.pdf
   ```

10. **Process another book?**
    ```
    Process another book? (y/n):
    ```
    - Type `y` to process another book
    - Type `n` to exit

## Option 2: Capture Only

Use this if you want to capture screenshots now and process them later.

1. Select option 2
2. Follow steps 2-5 from Option 1 (Full Workflow)
3. After capture completes:
   ```
   Process these screenshots now? (y/n):
   ```
   - Type `y` to process immediately
   - Type `n` to process later

Screenshots are saved to: `~/Documents/ebook_suite/book_YYYYMMDD_HHMMSS/`

## Option 3: Process Only

Use this to convert existing screenshots to PDF.

1. Select option 3
2. Choose which screenshot folder to process
3. Follow steps 6-9 from Option 1 (Full Workflow)

## Tips & Best Practices

### Before Capture

✅ **Do:**
- Open book in browser, go to first page
- Maximize or make browser window large
- Ensure book shows 2 pages side-by-side
- Have stable internet connection
- Close notification popups

❌ **Don't:**
- Touch mouse or keyboard during capture
- Let computer sleep
- Switch windows during capture

### During Capture

- You'll hear/see page navigation happening automatically
- To stop early: Press `Ctrl+C`
- Average time: 3 seconds per screenshot
  - 100 pages = ~3 minutes
  - 200 pages = ~6 minutes

### After Capture

- Screenshots saved to: `~/Documents/ebook_suite/book_TIMESTAMP/`
- Processed images saved to: `~/Documents/ebook_suite/pdf_book_TIMESTAMP/`
- Final PDF saved to: `~/Documents/ebooks/` (or your custom location)

## Customization

### Adjust Page Load Time

If pages load slowly, edit `src/capture.py`:

```python
DELAY_TIMEOUT = 3  # Change to 5 for slower connections
```

### Custom Crop Coordinates

When prompted "Does this frame detection look good?", type `a` to manually enter coordinates.

## Troubleshooting

### Screenshots are blank (macOS)

1. Grant Screen Recording permission:
   - System Preferences → Security & Privacy → Privacy → Screen Recording
   - Enable Terminal
2. Restart Terminal
3. Run `./run.sh` again

### Wrong window captured

- Make sure browser window is focused (clicked) before countdown ends
- Browser window should be in front of all other windows

### Capture stops unexpectedly

- Check internet connection
- Increase `DELAY_TIMEOUT` in `src/capture.py`
- Make sure book uses right arrow key for navigation

### "No screenshot folders found"

- You need to run Option 1 or 2 first to capture screenshots
- Check `~/Documents/ebook_suite/` for folders starting with `book_`

### PDF has wrong crop area

- When processing, choose `a` to manually adjust coordinates
- Check the preview image: `pdf_book_TIMESTAMP/crop_preview.png`

## File Locations

**Screenshots:**
- macOS: `~/Documents/ebook_suite/book_YYYYMMDD_HHMMSS/`
- Windows: `C:\Users\<you>\Documents\ebook_suite\book_YYYYMMDD_HHMMSS\`

**Processed images:**
- macOS: `~/Documents/ebook_suite/pdf_book_YYYYMMDD_HHMMSS/`
- Windows: `C:\Users\<you>\Documents\ebook_suite\pdf_book_YYYYMMDD_HHMMSS\`

**PDFs (default):**
- macOS: `~/Documents/ebooks/`
- Windows: `C:\Users\<you>\Documents\ebooks\`

## Keyboard Shortcuts

- `Ctrl+C` - Stop capture or processing at any time
- `Enter` - Accept default option
- `y` / `n` - Yes / No questions

## Example Session

```bash
./run.sh

# Menu appears
Select option: 1

# Capture phase
Enter total pages: 50
# Wait 15 seconds, click browser
# Automatic capture for ~2 minutes

# Processing phase
Does this frame detection look good? y
Create PDF? y
Enter book title: Python Guide
Output location: [press Enter]

# Done!
✅ PDF created: Python_Guide.pdf

Process another book? n
```

That's it! Simple and straightforward.
