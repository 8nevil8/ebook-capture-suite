#!/usr/bin/env python3
"""
macOS Script: Book Page Screenshot Tool
Takes screenshots of book pages in browser (2 pages per screenshot)
Calculates iterations based on total pages and navigates with right arrow key
"""

import pyautogui
import time
import os
from datetime import datetime
import sys

DELAY_TIMEOUT = 3

def setup_pyautogui():
    """Configure pyautogui settings for macOS"""
    # Disable fail-safe (move mouse to corner to stop)
    pyautogui.FAILSAFE = True

    # Set pause between actions (recommended for macOS)
    pyautogui.PAUSE = 0.1

    print("PyAutoGUI configured for macOS")


def get_user_input():
    """Get the number of pages from user and calculate iterations"""
    while True:
        try:
            total_pages = int(input("Enter the total number of pages in the book: "))
            if total_pages <= 0:
                print("Please enter a positive number of pages.")
                continue

            # Calculate number of screenshots needed (2 pages per screenshot)
            iterations = (total_pages + 1) // 2  # Ceiling division

            print(f"\nBook details:")
            print(f"Total pages: {total_pages}")
            print(f"Pages per screenshot: 2")
            print(f"Screenshots needed: {iterations}")

            confirm = input(f"\nThis will take approximately {iterations * DELAY_TIMEOUT / 60:.1f} minutes. Continue? (y/n): ")
            if confirm.lower() in ['y', 'yes']:
                return total_pages, iterations
            else:
                print("Operation cancelled.")
                sys.exit(0)

        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)


def create_screenshots_directory(total_pages):
    """Create a directory to store book screenshots"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Base directory for all ebook suite files
    base_dir = os.path.expanduser("~/Documents/ebook_suite")
    screenshots_dir = os.path.join(base_dir, f"book_{timestamp}")

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir, exist_ok=True)

    return screenshots_dir


def get_active_window_screenshot():
    """
    Take a screenshot of the active window on macOS
    Returns the screenshot as a PIL Image object
    """
    try:
        # Get the active window using AppleScript
        import subprocess

        # AppleScript to get active window bounds
        applescript = '''
        tell application "System Events"
            set frontApp to first application process whose frontmost is true
            tell frontApp
                try
                    set windowBounds to bounds of window 1
                    return windowBounds
                on error
                    return "0,0,800,600"
                end try
            end tell
        end tell
        '''

        result = subprocess.run(['osascript', '-e', applescript],
                                capture_output=True, text=True)

        if result.returncode == 0:
            bounds = result.stdout.strip().split(', ')
            if len(bounds) == 4:
                x1, y1, x2, y2 = map(int, bounds)
                width = x2 - x1
                height = y2 - y1

                # Take screenshot of the specified region
                screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
                return screenshot

        # Fallback: take full screen screenshot
        print("Warning: Could not get window bounds, taking full screen")
        return pyautogui.screenshot()

    except Exception as e:
        print(f"Error getting window screenshot: {e}")
        # Fallback to full screen
        return pyautogui.screenshot()


def main():
    """Main function to execute the book screenshot process"""
    print("📚 Book Screenshot Tool for macOS")
    print("=" * 40)
    print("This script will help you capture screenshots of book pages")
    print("from a browser where each screenshot shows 2 pages.")
    print()

    # Check if required modules are available
    try:
        import pyautogui
        from PIL import Image
    except ImportError as e:
        print(f"Error: Required module not found - {e}")
        print("Please install required modules:")
        print("pip install pyautogui pillow")
        sys.exit(1)

    # Get user input
    total_pages, iterations = get_user_input()

    # Setup
    setup_pyautogui()
    screenshots_dir = create_screenshots_directory(total_pages)

    print(f"\n📁 Screenshots will be saved to: {screenshots_dir}")
    print("🌐 Make sure your browser window is active and on the first page...")
    print("⏰ Starting in 15 seconds...")
    time.sleep(15)

    # Main loop
    for i in range(1, iterations + 1):
        try:
            # Calculate which pages this screenshot represents
            page_start = (i - 1) * 2 + 1
            page_end = min(i * 2, total_pages)

            if page_end == page_start:
                page_info = f"page {page_start}"
            else:
                page_info = f"pages {page_start}-{page_end}"

            print(f"📸 Screenshot {i}/{iterations} ({page_info})", end=" - ")

            # Take screenshot first (before pressing key for next iteration)
            screenshot = get_active_window_screenshot()

            # Save screenshot with descriptive filename
            filename = f"pages_{page_start:03d}-{page_end:03d}.png"
            filepath = os.path.join(screenshots_dir, filename)
            screenshot.save(filepath)

            print(f"Saved: {filename}")

            # Press right arrow key to go to next page spread (except on last iteration)
            if i < iterations:
                pyautogui.press('right')
                print("➡️  Moving to next page spread...")
                print(f"⏳ Waiting {DELAY_TIMEOUT} seconds for page to load...")
                time.sleep(DELAY_TIMEOUT)

        except KeyboardInterrupt:
            print(f"\n⚠️  Script interrupted by user at screenshot {i}")
            break
        except Exception as e:
            print(f"❌ Error at screenshot {i}: {e}")
            continue

    print(f"\n✅ Book screenshot process completed!")
    print(f"📊 Captured {min(i, iterations)} screenshots covering {total_pages} pages")
    print(f"📁 All files saved in: {screenshots_dir}")


if __name__ == "__main__":
    # Check if running on macOS
    if sys.platform != "darwin":
        print("Warning: This script is designed for macOS")

    main()