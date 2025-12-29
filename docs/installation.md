# Installation Guide

This guide will walk you through installing the eBook Capture Suite on macOS and Windows.

## Prerequisites

### 1. System Requirements

- **Operating System**:
  - macOS 10.14 (Mojave) or later
  - Windows 10 or Windows 11
- **Python**: Version 3.7 or higher
- **Free Disk Space**: At least 500MB for screenshots and PDFs

### 2. Check Python Installation

**macOS/Linux:**
Open Terminal and verify Python is installed:
```bash
python3 --version
```

**Windows:**
Open Command Prompt or PowerShell and verify Python is installed:
```cmd
python --version
```

Expected output: `Python 3.7.0` or higher

**If Python is not installed:**
- macOS: Download from [python.org](https://www.python.org/downloads/macos/)
- Windows: Download from [python.org](https://www.python.org/downloads/windows/)

## Installation Steps

### Option 1: Install via Git (Recommended)

**macOS/Linux:**
```bash
# Clone the repository
git clone https://github.com/8nevil8/ebook-capture-suite.git

# Navigate to the directory
cd ebook-capture-suite

# Install dependencies
pip3 install -r requirements.txt
```

**Windows:**
```cmd
# Clone the repository
git clone https://github.com/8nevil8/ebook-capture-suite.git

# Navigate to the directory
cd ebook-capture-suite

# Install dependencies
python -m pip install -r requirements.txt
```

### Option 2: Manual Installation

1. Download the repository as a ZIP file from GitHub
2. Extract to your desired location
3. Open Terminal (macOS) or Command Prompt (Windows) and navigate to the extracted folder:

   **macOS/Linux:**
   ```bash
   cd /path/to/ebook-capture-suite
   ```

   **Windows:**
   ```cmd
   cd C:\path\to\ebook-capture-suite
   ```

4. Install dependencies:

   **macOS/Linux:**
   ```bash
   pip3 install -r requirements.txt
   ```

   **Windows:**
   ```cmd
   python -m pip install -r requirements.txt
   ```

## Installing Dependencies

### Using pip

```bash
pip3 install -r requirements.txt
```

This will install:
- **Pillow** (10.0.0+): Image processing library
- **pyautogui** (0.9.54+): GUI automation for screenshots

### Manual Dependency Installation

If you prefer to install dependencies manually:

```bash
pip3 install Pillow>=10.0.0
pip3 install pyautogui>=0.9.54
```

### Using a Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

To deactivate the virtual environment later:
```bash
deactivate
```

## Granting Permissions

### macOS

The suite requires specific macOS permissions to function properly.

**Screen Recording Permission** (Required for `capture.py` to take screenshots):

1. Open **System Preferences**
2. Go to **Security & Privacy** > **Privacy** tab
3. Select **Screen Recording** from the left sidebar
4. Click the lock icon to make changes (enter your password)
5. Check the box next to:
   - **Terminal** (if running scripts directly)
   - **iTerm** (if using iTerm instead of Terminal)
   - **Python** (if you see it listed)
6. Click the lock icon again to save changes
7. **Important**: Restart Terminal for changes to take effect

**Accessibility Permission** (Optional - for advanced automation features):

1. Open **System Preferences**
2. Go to **Security & Privacy** > **Privacy** tab
3. Select **Accessibility** from the left sidebar
4. Click the lock icon to make changes
5. Click the **+** button
6. Navigate to and add:
   - `/Applications/Utilities/Terminal.app`
   - Or your Python installation path
7. Click the lock icon to save

### Windows

No special permissions required! The application will work out of the box.

**Optional Enhancement:**
For better window detection, install pygetwindow:
```cmd
python -m pip install pygetwindow
```

Without pygetwindow, the tool will capture the full screen instead of just the active window, which still works perfectly fine.

## Verifying Installation

### 1. Check Python Dependencies

**macOS/Linux:**
```bash
python3 -c "import PIL; import pyautogui; print('All dependencies installed successfully!')"
```

**Windows:**
```cmd
python -c "import PIL; import pyautogui; print('All dependencies installed successfully!')"
```

Expected output: `All dependencies installed successfully!`

### 2. Test Script Execution

**macOS/Linux:**
```bash
# Test capture script (will start in 15 seconds, press Ctrl+C to cancel)
python3 src/capture.py
# Press Ctrl+C to cancel

# Test process script (should show folder selection or "no folders found")
python3 src/process.py
```

**Windows:**
```cmd
# Test capture script (will start in 15 seconds, press Ctrl+C to cancel)
python src/capture.py
# Press Ctrl+C to cancel

# Test process script (should show folder selection or "no folders found")
python src/process.py
```

## Troubleshooting Installation

### "Command not found: python3"

**Solution**: Install Python 3 from [python.org](https://www.python.org/downloads/macos/)

### "No module named 'PIL'"

**Solution**: Reinstall Pillow:
```bash
pip3 install --upgrade Pillow
```

### "No module named 'pyautogui'"

**Solution**: Install pyautogui:
```bash
pip3 install pyautogui
```

### Permission Denied Errors

**Solution**: Use `pip3` with user flag:
```bash
pip3 install --user -r requirements.txt
```

### SSL Certificate Errors

**Solution**: Update certificates:
```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

### pyautogui Installation Fails on macOS

**Solution**: Install Xcode Command Line Tools:
```bash
xcode-select --install
```

Then retry:
```bash
pip3 install pyautogui
```

## Updating the Suite

To update to the latest version:

```bash
# Navigate to the repository
cd ebook-capture-suite

# Pull latest changes (if using Git)
git pull origin main

# Update dependencies
pip3 install --upgrade -r requirements.txt
```

## Uninstallation

To remove the suite:

```bash
# Remove the directory
rm -rf /path/to/ebook-capture-suite

# (Optional) Uninstall Python packages
pip3 uninstall Pillow pyautogui
```

## Next Steps

Once installation is complete:

1. Read the [Usage Guide](usage.md) for detailed usage instructions
2. Try the Quick Start example in the main [README](../README.md)
3. Configure settings if needed

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting-installation) section above
2. Review the main [README](../README.md) troubleshooting section
3. Open an issue on GitHub with:
   - macOS version
   - Python version
   - Error messages
   - Steps to reproduce

## Additional Notes

### Python Version Management

If you have multiple Python versions, ensure you're using Python 3:

```bash
# Check which python3 is being used
which python3

# Create an alias (optional)
alias python=python3
```

### IDE Setup

If using an IDE like PyCharm or VS Code:

1. Set the Python interpreter to your Python 3 installation
2. Install dependencies through the IDE's package manager
3. Ensure the interpreter has the correct permissions

### Running from Anywhere

To run scripts from any directory, add to your `.zshrc` or `.bash_profile`:

```bash
# Add this line
export PATH="$PATH:/path/to/ebook-capture-suite/src"

# Create aliases
alias capture="python3 /path/to/ebook-capture-suite/src/capture.py"
alias process="python3 /path/to/ebook-capture-suite/src/process.py"
```

Then reload your shell:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```
