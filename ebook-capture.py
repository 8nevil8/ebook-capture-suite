#!/usr/bin/env python3
"""
eBook Capture Suite - Main Entry Point
Simplified workflow for capturing and processing book screenshots
"""

import sys
import os

# Add src directory to path so we can import the modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, 'src')
sys.path.insert(0, src_dir)

import capture
import process


def print_banner():
    """Print welcome banner"""
    print("=" * 50)
    print("📚 eBook Capture Suite")
    print("=" * 50)
    print()


def show_menu():
    """Show main menu and get user choice"""
    print("\nWhat would you like to do?")
    print("  1. Full workflow (Capture → Process → PDF)")
    print("  2. Capture screenshots only")
    print("  3. Process existing screenshots")
    print("  4. Exit")
    print()

    while True:
        try:
            choice = input("Select option (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled.")
            sys.exit(0)


def run_full_workflow():
    """Run the complete capture and process workflow"""
    print("\n" + "=" * 50)
    print("FULL WORKFLOW: Capture → Process → PDF")
    print("=" * 50)

    # Step 1: Capture
    print("\n📸 STEP 1: Capture Screenshots")
    print("-" * 50)
    try:
        capture.main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Capture interrupted. You can process existing screenshots using option 3.")
        return
    except Exception as e:
        print(f"\n❌ Error during capture: {e}")
        return

    # Step 2: Process
    print("\n\n🔄 STEP 2: Process Screenshots")
    print("-" * 50)
    input("Press Enter to continue to processing...")

    try:
        process.main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Processing interrupted.")
        return
    except Exception as e:
        print(f"\n❌ Error during processing: {e}")
        return

    print("\n\n✨ Full workflow completed successfully!")


def run_capture_only():
    """Run capture only"""
    print("\n" + "=" * 50)
    print("CAPTURE SCREENSHOTS")
    print("=" * 50)
    try:
        capture.main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Capture interrupted.")
    except Exception as e:
        print(f"\n❌ Error during capture: {e}")


def run_process_only():
    """Run process only"""
    print("\n" + "=" * 50)
    print("PROCESS SCREENSHOTS")
    print("=" * 50)
    try:
        process.main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Processing interrupted.")
    except Exception as e:
        print(f"\n❌ Error during processing: {e}")


def main():
    """Main entry point"""
    print_banner()

    # Check dependencies
    try:
        from PIL import Image
        import pyautogui
    except ImportError as e:
        print(f"❌ Error: Missing required module - {e}")
        print("\nPlease install required dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)

    while True:
        choice = show_menu()

        if choice == '1':
            run_full_workflow()

            # Ask if user wants to continue
            cont = input("\n\nProcess another book? (y/n): ").lower().strip()
            if cont != 'y':
                break

        elif choice == '2':
            run_capture_only()

            # Ask if user wants to process now
            process_now = input("\n\nProcess these screenshots now? (y/n): ").lower().strip()
            if process_now == 'y':
                run_process_only()

            cont = input("\n\nContinue? (y/n): ").lower().strip()
            if cont != 'y':
                break

        elif choice == '3':
            run_process_only()

            cont = input("\n\nContinue? (y/n): ").lower().strip()
            if cont != 'y':
                break

        elif choice == '4':
            print("\n👋 Thanks for using eBook Capture Suite!")
            break

    print("\n✨ All done!")


if __name__ == "__main__":
    main()
