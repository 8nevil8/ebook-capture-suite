# Installation Guide

Simple installation guide for eBook Capture Suite.

## Step 1: Install Python

### macOS

Python 3 is usually pre-installed. Check by opening Terminal:
```bash
python3 --version
```

If not installed, download from [python.org](https://www.python.org/downloads/macos/)

### Windows

1. Download Python from [python.org](https://www.python.org/downloads/windows/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" ✅
4. Click "Install Now"

Verify installation in Command Prompt:
```cmd
python --version
```

## Step 2: Download eBook Capture Suite

1. Go to [github.com/8nevil8/ebook-capture-suite](https://github.com/8nevil8/ebook-capture-suite)
2. Click green **Code** button
3. Click **Download ZIP**
4. Extract the ZIP file to your preferred location

## Step 3: Run the Launcher

### macOS/Linux

Open Terminal in the extracted folder and run:
```bash
./run.sh
```

The script automatically:
- Creates a virtual environment
- Installs all dependencies
- Starts the tool

### Windows

Simply **double-click** `run.bat` in the extracted folder.

The batch file automatically:
- Creates a virtual environment
- Installs all dependencies
- Starts the tool

## Step 4: Grant Permissions (macOS Only)

When you first run the tool on macOS:

1. Open **System Preferences** → **Security & Privacy** → **Privacy**
2. Select **Screen Recording** from the list
3. Check the box next to **Terminal**
4. Restart Terminal
5. Run `./run.sh` again

**Windows users**: No permissions needed!

## That's It!

Every time you want to use the tool, just run:
- macOS/Linux: `./run.sh`
- Windows: Double-click `run.bat`

## Troubleshooting

### "Python is not installed" or "command not found"

**macOS**:
```bash
# Install Python 3
brew install python3
# or download from python.org
```

**Windows**:
- Reinstall Python from python.org
- Make sure to check "Add Python to PATH"

### "./run.sh: Permission denied" (macOS/Linux)

Make the script executable:
```bash
chmod +x run.sh
```

### Windows: Script closes immediately

Right-click `run.bat` → "Run as administrator"

### Dependencies fail to install

Check your internet connection and try again. The script will automatically retry installing dependencies.
