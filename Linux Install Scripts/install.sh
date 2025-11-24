#!/usr/bin/env bash
set -e

# ───────────────────────────────────────────
# ASCII LOGO
# ───────────────────────────────────────────
logo=$(cat << 'EOF'
.___  __                              .__
|   |/  |_  ____   _____   ___________|__|
|   \   __\/  _ \ /     \ /  _ \_  __ \  |
|   ||  | (  <_> )  Y Y  (  <_> )  | \/  |
|___||__|  \____/|__|_|  /\____/|__|  |__|
                       \/
        Itomori TUI Installer
EOF
)

echo "$logo"
echo ""

# ───────────────────────────────────────────
# VARIABLES
# ───────────────────────────────────────────
REPO_URL="https://github.com/TheAhumMaitra/Itomori"
INSTALL_DIR="$HOME/Itomori"
DESKTOP_FILE="$HOME/.local/share/applications/itomori.desktop"

# ───────────────────────────────────────────
# CHECK PYTHON
# ───────────────────────────────────────────
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 not found. Installing..."

    if command -v apt >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y python3 python3-venv python3-pip
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -Sy --noconfirm python python-pip
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y python3 python3-pip
    elif command -v emerge >/dev/null 2>&1; then
        sudo emerge --ask dev-lang/python
    else
        echo "❌ Unsupported distro. Install Python manually."
        exit 1
    fi
fi

echo "✔ Python found or installed."

# ───────────────────────────────────────────
# CLONE REPO
# ───────────────────────────────────────────
if [ -d "$INSTALL_DIR" ]; then
    echo "Directory already exists. Pulling latest changes..."
    git -C "$INSTALL_DIR" pull
else
    echo "Cloning Itomori repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# ───────────────────────────────────────────
# SETUP PYTHON VENV
# ───────────────────────────────────────────
echo "Setting up virtual environment..."
python3 -m venv "$INSTALL_DIR/venv"
source "$INSTALL_DIR/venv/bin/activate"

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r "$INSTALL_DIR/requirements.txt" || true

deactivate

echo "✔ Virtual environment ready."

# ───────────────────────────────────────────
# CREATE DESKTOP LAUNCHER
# ───────────────────────────────────────────
echo "Creating desktop application entry..."

mkdir -p "$HOME/.local/share/applications"

cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Name=Itomori
Comment=Itomori TUI Application
Exec=$INSTALL_DIR/venv/bin/python $INSTALL_DIR/itomori.py
Icon=$INSTALL_DIR/icon.png
Terminal=true
Type=Application
Categories=Utility;
EOF

chmod +x "$DESKTOP_FILE"

echo "✔ Desktop entry created: $DESKTOP_FILE"
echo "✔ You can now search 'Itomori' in your applications menu."

# ───────────────────────────────────────────
echo ""
echo "🎉 Installation complete!"
