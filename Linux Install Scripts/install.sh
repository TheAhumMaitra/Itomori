#!/bin/bash

echo "🚀 Welcome to the Itomori Installation Script!"
echo ""
echo "Author : Ahum Maitra"
echo ""

# Detect home directory
USER_HOME="$HOME"
INSTALL_DIR="$USER_HOME/Itomori"

echo "📦 Cloning repository..."
git clone https://github.com/TheAhumMaitra/Itomori "$INSTALL_DIR"

echo "📁 Moving into project..."
cd "$INSTALL_DIR" || exit

echo "🐍 Creating virtual environment..."
python3 -m venv .venv

echo "📁 Activating environment and installing dependencies..."
source .venv/bin/activate
pip install textual

echo "✅ Installation completed successfully!"
echo ""

# Create launcher script
LAUNCHER="$HOME/.local/bin/itomori"

echo "📝 Creating launcher script at $LAUNCHER"

mkdir -p "$HOME/.local/bin"

cat <<EOF > "$LAUNCHER"
#!/bin/bash
cd "$INSTALL_DIR/src"
source "$INSTALL_DIR/.venv/bin/activate"
python main.py
EOF

chmod +x "$LAUNCHER"

echo "🎉 Launcher created: run 'itomori' from terminal!"

# Create desktop entry
DESKTOP_FILE="$HOME/.local/share/applications/itomori.desktop"

echo "🖥 Creating desktop shortcut at $DESKTOP_FILE"

mkdir -p "$HOME/.local/share/applications"

cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Type=Application
Name=Itomori
Comment=Minimal TUI notes application
Exec=$LAUNCHER
Icon=utilities-terminal
Terminal=true
Categories=Utility;TextEditor;
EOF

echo "✔ Desktop shortcut created!"
echo "📌 Check your applications menu for Itomori."

echo ""
echo "🎀 Thank you for installing Itomori!"
