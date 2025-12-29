#!/usr/bin/env python3
"""
Book Content Cropping Tool
Analyzes screenshots from book capture and crops out the left navigation panel
Keeps only the main book content area (the actual book pages)
"""

import os
import sys
from PIL import Image, ImageDraw
import glob
from datetime import datetime


def find_screenshot_folders():
    """Find all book screenshot folders in ebook_suite directory"""
    base_dir = os.path.expanduser("~/Documents/ebook_suite")

    # Create base directory if it doesn't exist
    if not os.path.exists(base_dir):
        return []

    folders = []
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and item.startswith('book_'):
            folders.append(item)
    return sorted(folders)


def select_folder():
    """Let user select which screenshot folder to process"""
    folders = find_screenshot_folders()
    base_dir = os.path.expanduser("~/Documents/ebook_suite")

    if not folders:
        print("❌ No book screenshot folders found!")
        print("Please run the screenshot script first.")
        print(f"Looking for folders starting with 'book_' in: {base_dir}")
        sys.exit(1)

    if len(folders) == 1:
        print(f"📁 Found screenshot folder: {folders[0]}")
        return os.path.join(base_dir, folders[0])

    print("📁 Found multiple screenshot folders:")
    for i, folder in enumerate(folders, 1):
        print(f"  {i}. {folder}")

    while True:
        try:
            choice = int(input("\nSelect folder number: ")) - 1
            if 0 <= choice < len(folders):
                return os.path.join(base_dir, folders[choice])
            else:
                print("Invalid selection. Please try again.")
        except (ValueError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            sys.exit(0)


def analyze_content_frame(image_path):
    """
    Analyze the image to find the gray frame boundaries
    Returns the crop coordinates (left, top, right, bottom) for the content frame
    """

    left_x=215
    top_y=48
    right_x=2785
    bottom_y=1660
    return left_x, top_y, right_x, bottom_y


def crop_content_frame(image_path, crop_coords, output_dir, base_filename):
    """
    Crop the image to keep only the content inside the gray frame
    """
    try:
        img = Image.open(image_path)
        left_x, top_y, right_x, bottom_y = crop_coords

        # Crop to the frame boundaries
        content_frame = img.crop((left_x, top_y, right_x, bottom_y))

        # Save the cropped frame content
        output_filename = f"{base_filename}_frame.png"
        output_path = os.path.join(output_dir, output_filename)
        content_frame.save(output_path, 'PNG')

        return output_filename

    except Exception as e:
        print(f"❌ Error cropping {image_path}: {e}")
        return None


def get_book_title():
    """Ask user for book title for PDF metadata"""
    try:
        title = input("\n📚 Enter book title for PDF (or press Enter to skip): ").strip()
        return title if title else None
    except KeyboardInterrupt:
        return None


def get_pdf_output_directory():
    """Ask user where to save the PDF file"""
    try:
        default_dir = os.path.expanduser("~/Documents/ebooks")
        print(f"\n📁 Where should the PDF be saved?")
        print(f"   Default: {default_dir}")
        user_input = input("   Enter path (or press Enter for default): ").strip()

        if not user_input:
            output_dir = default_dir
        else:
            output_dir = os.path.expanduser(user_input)

        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        print(f"✅ PDF will be saved to: {output_dir}")

        return output_dir
    except KeyboardInterrupt:
        return None
    except Exception as e:
        print(f"⚠️  Error with directory: {e}")
        print(f"   Using default: {default_dir}")
        os.makedirs(default_dir, exist_ok=True)
        return default_dir


def create_pdf_from_images(image_files, output_path, book_title=None):
    """
    Create a single PDF from all cropped images
    """
    try:
        if not image_files:
            print("❌ No images to convert to PDF")
            return False

        print(f"\n📄 Creating PDF with {len(image_files)} pages...")

        # Load and prepare images
        images = []
        for i, image_path in enumerate(image_files, 1):
            try:
                print(f"📖 Adding page {i}/{len(image_files)}: {os.path.basename(image_path)}")
                img = Image.open(image_path)

                # Convert to RGB if necessary (PDF requires RGB)
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                images.append(img)

            except Exception as e:
                print(f"⚠️  Error loading {image_path}: {e}")
                continue

        if not images:
            print("❌ No valid images to create PDF")
            return False

        # Create PDF
        print(f"💾 Saving PDF: {output_path}")

        # Save the first image as PDF and append the rest
        images[0].save(
            output_path,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=images[1:] if len(images) > 1 else [],
            title=book_title or "Book",
            author="Book Scanner",
            subject="Scanned Book Content"
        )

        print(f"✅ PDF created successfully!")
        print(f"📊 Total pages in PDF: {len(images)}")
        return True

    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
        return False


def create_preview_image(original_path, crop_coords, output_dir):
    """Create a preview image showing the crop rectangle"""
    try:
        img = Image.open(original_path)
        preview_img = img.copy()
        draw = ImageDraw.Draw(preview_img)

        left_x, top_y, right_x, bottom_y = crop_coords

        # Draw a green rectangle indicating the crop area
        draw.rectangle([left_x, top_y, right_x, bottom_y], outline='green', width=3)

        # Save preview
        preview_filename = "crop_preview.png"
        preview_path = os.path.join(output_dir, preview_filename)
        preview_img.save(preview_path)

        return preview_filename
    except Exception as e:
        print(f"⚠️  Could not create preview: {e}")
        return None


def process_screenshots(folder_path):
    """Process all screenshots in the folder"""

    # Create output directory in the same base location
    base_dir = os.path.expanduser("~/Documents/ebook_suite")
    folder_name = os.path.basename(folder_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(base_dir, f"pdf_{folder_name}")
    os.makedirs(output_dir, exist_ok=True)

    # Find all PNG files in the folder
    image_files = glob.glob(os.path.join(folder_path, "*.png"))
    image_files.sort()

    if not image_files:
        print(f"❌ No PNG files found in {folder_path}")
        return

    print(f"📊 Found {len(image_files)} images to process")

    # Process first image to show preview and get confirmation
    first_image = image_files[1]
    print(f"\n🔍 Analyzing gray frame boundaries using: {os.path.basename(first_image)}")

    crop_coords = analyze_content_frame(first_image)
    left_x, top_y, right_x, bottom_y = crop_coords
    preview_file = create_preview_image(first_image, crop_coords, output_dir)

    if preview_file:
        print(f"📸 Preview saved as: {os.path.join(output_dir, preview_file)}")
        print("🔍 Check the preview - green rectangle shows what will be kept, red areas will be removed")

    print(f"📏 Detected frame boundaries:")
    print(f"   Left: {left_x}, Top: {top_y}, Right: {right_x}, Bottom: {bottom_y}")

    # Ask for confirmation
    response = input("\nDoes this frame detection look good? (y/n/a): ").lower().strip()

    if response == 'n':
        print("Operation cancelled.")
        return
    elif response == 'a':
        print("Enter new coordinates for the frame:")
        while True:
            try:
                img = Image.open(first_image)
                w, h = img.size
                print(f"Image size: {w} x {h}")

                left_x = int(input(f"Left edge (0-{w}): "))
                top_y = int(input(f"Top edge (0-{h}): "))
                right_x = int(input(f"Right edge ({left_x}-{w}): "))
                bottom_y = int(input(f"Bottom edge ({top_y}-{h}): "))

                crop_coords = (left_x, top_y, right_x, bottom_y)
                preview_file = create_preview_image(first_image, crop_coords, output_dir)
                if preview_file:
                    print(f"📸 Updated preview saved as: {os.path.join(output_dir, preview_file)}")

                if input("Use this frame? (y/n): ").lower() == 'y':
                    break
            except (ValueError, KeyboardInterrupt):
                print("Invalid input or cancelled.")
                return

    # Ask about PDF creation
    create_pdf = input("\n📄 Do you want to create a single PDF file? (y/n): ").lower().strip() == 'y'
    book_title = None
    pdf_output_dir = None
    if create_pdf:
        book_title = get_book_title()
        pdf_output_dir = get_pdf_output_directory()
        if pdf_output_dir is None:
            print("⚠️  PDF creation cancelled")
            create_pdf = False

    # Process all images
    print(f"\n🔄 Processing {len(image_files)} images...")
    successful = 0
    cropped_files = []

    for i, image_path in enumerate(image_files, 1):
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        print(f"📄 Processing {i}/{len(image_files)}: {base_name}", end=" - ")

        content_file = crop_content_frame(image_path, crop_coords, output_dir, base_name)

        if content_file:
            print(f"✅ Created: {content_file}")
            successful += 1
            cropped_files.append(os.path.join(output_dir, content_file))
        else:
            print("❌ Failed")

    print(f"\n✅ Frame cropping completed!")
    print(f"📊 Successfully processed: {successful}/{len(image_files)} images")
    print(f"📁 Frame content saved in: {output_dir}")
    print(f"🎯 Clean book content extracted from gray frames!")

    # Create PDF if requested
    if create_pdf and cropped_files and pdf_output_dir:
        pdf_filename = f"{os.path.basename(folder_path)}_book.pdf"
        if book_title:
            # Clean title for filename
            clean_title = "".join(c for c in book_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            if clean_title:
                pdf_filename = f"{clean_title.replace(' ', '_')}.pdf"

        pdf_path = os.path.join(pdf_output_dir, pdf_filename)

        if create_pdf_from_images(cropped_files, pdf_path, book_title):
            print(f"\n🎉 PDF created: {pdf_filename}")
            print(f"📍 Location: {pdf_path}")
        else:
            print("\n⚠️  PDF creation failed, but individual images are available")


def main():
    """Main function"""
    print("📚 Book Frame Extraction & PDF Tool")
    print("=" * 40)
    print("This tool will:")
    print("1. Detect and extract content from the gray frame in your screenshots")
    print("2. Remove all browser UI, navigation panels, and external elements")
    print("3. Keep only the clean book content from inside the frame")
    print("4. Optionally create a single PDF file from all pages")
    print()

    # Check PIL availability
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("❌ Error: PIL (Pillow) not found")
        print("Please install: pip install pillow")
        sys.exit(1)

    # Select folder to process
    folder_path = select_folder()

    print(f"\n📂 Selected folder: {folder_path}")

    # Process the screenshots
    process_screenshots(folder_path)

    print("\n🎉 All done! Your book content has been extracted from the frames and is ready!")


if __name__ == "__main__":
    main()