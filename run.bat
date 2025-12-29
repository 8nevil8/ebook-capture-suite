@echo off
REM eBook Capture Suite - Simple Launcher for Windows
REM Just double-click this file and everything will be set up automatically!

echo ==========================================
echo 📚 eBook Capture Suite
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ Python found: %PYTHON_VERSION%
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
    echo.
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo 📥 Installing dependencies...
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Run the interactive tool
echo 🚀 Starting eBook Capture Suite...
echo.
python ebook-capture.py

REM Deactivate virtual environment
call venv\Scripts\deactivate.bat

echo.
echo Press any key to exit...
pause >nul
