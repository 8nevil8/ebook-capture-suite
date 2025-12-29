#!/bin/bash
# eBook Capture Suite - Simple Launcher for macOS/Linux
# Just run this script and everything will be set up automatically!

echo "=========================================="
echo "📚 eBook Capture Suite"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3 from: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed"
    echo ""
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Run the interactive tool
echo "🚀 Starting eBook Capture Suite..."
echo ""
python3 ebook-capture.py

# Deactivate virtual environment
deactivate
