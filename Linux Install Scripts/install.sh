#   Copyright (C) 2025  Ahum Maitra

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>

#!/usr/bin/env bash
set -e

clear
# ───────────────────────────────────────────
# ASCII LOGO
# ───────────────────────────────────────────
echo "Important note : Please do not run this script on fish shell. Press CTR+C to exit it"
logo=$(cat << 'EOF'
.___  __                              .__
|   |/  |_  ____   _____   ___________|__|
|   \   __\/  _ \ /     \ /  _ \_  __ \  |
|   ||  | (  <_> )  Y Y  (  <_> )  | \/  |
|___||__|  \____/|__|_|  /\____/|__|  |__|
                       \/
                Itomori
EOF
)

echo "$logo"
echo ""
echo "Installation script by Ahum Maitra. This Linux installation script helps you to install Itomori and it's also creates a desktop shortcut for you!"
echo ""
echo ""
echo ""
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
    echo "Python3 not Icon=$INSTALL_DIR/icon.pngfound. Installing..."

    if command -v apt >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y python3 python3-venv python3-pip
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -Sy --noconfirm python python-pip
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y python3 python3-pip
    elif command -v emerge >/dev/null 2>&1; then
        sudo emerge --ask dev-lang/python
    else
        echo "Unsupported distro, please install Python manually."
        exit 1
    fi
fi

echo "Python found....."

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
# Installing Itomori
# ───────────────────────────────────────────
echo "Installing Itomori!"
cd "$INSTALL_DIR"
uv tool install git+https://github.com/TheAhumMaitra/Itomori.git


# ───────────────────────────────────────────
# CREATE DESKTOP LAUNCHER
# ───────────────────────────────────────────
echo "Creating desktop application entry..."

mkdir -p "$HOME/.local/share/applications"

cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Name=Itomori
Comment=Itomori
Exec=Itomori
Terminal=true
Type=Application
Categories=Utility;
EOF

chmod +x "$DESKTOP_FILE"

echo "Desktop app entry created: $DESKTOP_FILE"
echo "You can now search Itomori' in your applications menu."

# ───────────────────────────────────────────
echo ""
echo "🎉 Installation complete!"
