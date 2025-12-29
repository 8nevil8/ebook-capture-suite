#!/bin/bash
# eBook Capture Suite - One-Click Installer
# Download this file and run: bash install.sh

set -e  # Exit on error

echo "=========================================="
echo "📚 eBook Capture Suite - Installer"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo ""
    echo "Please install Python 3 first:"
    echo "  macOS: brew install python3"
    echo "  or download from: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Download the repository
REPO_URL="https://github.com/8nevil8/ebook-capture-suite/archive/refs/heads/main.zip"
INSTALL_DIR="$HOME/ebook-capture-suite"

echo "📥 Downloading eBook Capture Suite..."

# Remove old installation if exists
if [ -d "$INSTALL_DIR" ]; then
    echo "🗑️  Removing old installation..."
    rm -rf "$INSTALL_DIR"
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Download using curl or wget
if command -v curl &> /dev/null; then
    curl -L -o ebook-capture-suite.zip "$REPO_URL"
elif command -v wget &> /dev/null; then
    wget -O ebook-capture-suite.zip "$REPO_URL"
else
    echo "❌ Neither curl nor wget is available!"
    echo "Please install curl: brew install curl"
    exit 1
fi

echo "✅ Downloaded"
echo ""

# Extract
echo "📦 Extracting files..."
unzip -q ebook-capture-suite.zip
mv ebook-capture-suite-main "$INSTALL_DIR"

# Cleanup
cd "$HOME"
rm -rf "$TEMP_DIR"

echo "✅ Installed to: $INSTALL_DIR"
echo ""

# Create desktop launcher script
LAUNCHER_SCRIPT="$HOME/Desktop/eBook-Capture.command"
cat > "$LAUNCHER_SCRIPT" << 'EOF'
#!/bin/bash
cd "$HOME/ebook-capture-suite"
./run.sh
EOF

chmod +x "$LAUNCHER_SCRIPT"

echo "✅ Created launcher on Desktop: eBook-Capture.command"
echo ""
echo "=========================================="
echo "🎉 Installation Complete!"
echo "=========================================="
echo ""
echo "To run the tool:"
echo "  1. Double-click 'eBook-Capture.command' on your Desktop"
echo "  OR"
echo "  2. Run: cd ~/ebook-capture-suite && ./run.sh"
echo ""
echo "Starting the tool now..."
echo ""

# Run the tool
cd "$INSTALL_DIR"
./run.sh
