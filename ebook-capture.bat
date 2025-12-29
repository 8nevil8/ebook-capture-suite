@echo off
REM eBook Capture Suite - One-Click Installer
REM Download this file and double-click to run

echo ==========================================
echo 📚 eBook Capture Suite - Installer
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo.
    echo Please install Python 3 first:
    echo   Download from: https://www.python.org/downloads/
    echo   Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ Python found: %PYTHON_VERSION%
echo.

REM Set installation directory
set INSTALL_DIR=%USERPROFILE%\ebook-capture-suite
set REPO_URL=https://github.com/8nevil8/ebook-capture-suite/archive/refs/heads/main.zip

echo 📥 Downloading eBook Capture Suite...

REM Remove old installation if exists
if exist "%INSTALL_DIR%" (
    echo 🗑️  Removing old installation...
    rmdir /s /q "%INSTALL_DIR%"
)

REM Create temp directory
set TEMP_ZIP=%TEMP%\ebook-capture-suite.zip
set TEMP_EXTRACT=%TEMP%\ebook-capture-suite-temp

REM Download using PowerShell
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%REPO_URL%' -OutFile '%TEMP_ZIP%'}"

if errorlevel 1 (
    echo ❌ Failed to download!
    echo Please check your internet connection.
    pause
    exit /b 1
)

echo ✅ Downloaded
echo.

REM Extract using PowerShell
echo 📦 Extracting files...
if exist "%TEMP_EXTRACT%" rmdir /s /q "%TEMP_EXTRACT%"
powershell -Command "& {Expand-Archive -Path '%TEMP_ZIP%' -DestinationPath '%TEMP_EXTRACT%' -Force}"

REM Move to installation directory
move "%TEMP_EXTRACT%\ebook-capture-suite-main" "%INSTALL_DIR%"

REM Cleanup
del "%TEMP_ZIP%"
rmdir /s /q "%TEMP_EXTRACT%"

echo ✅ Installed to: %INSTALL_DIR%
echo.

REM Create desktop shortcut
set DESKTOP=%USERPROFILE%\Desktop
set SHORTCUT=%DESKTOP%\eBook Capture.bat

echo @echo off > "%SHORTCUT%"
echo cd /d "%INSTALL_DIR%" >> "%SHORTCUT%"
echo call run.bat >> "%SHORTCUT%"

echo ✅ Created launcher on Desktop: eBook Capture.bat
echo.
echo ==========================================
echo 🎉 Installation Complete!
echo ==========================================
echo.
echo To run the tool:
echo   1. Double-click "eBook Capture.bat" on your Desktop
echo   OR
echo   2. Run: %INSTALL_DIR%\run.bat
echo.
echo Starting the tool now...
echo.

REM Run the tool
cd /d "%INSTALL_DIR%"
call run.bat
