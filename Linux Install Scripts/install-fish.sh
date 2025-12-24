#!/usr/bin/env fish
#   Copyright (C) 2025  Ahum Maitra
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>

clear

# ───────────────────────────────────────────
# ASCII LOGO
# ───────────────────────────────────────────

echo "Important note : Please do not run this script on bash/zsh. Press CTRL+C to exit it"

set logo '.___  __                              .__
|   |/  |_  ____   _____   ___________|__|
|   \   __\/  _ \ /     \ /  _ \_  __ \  |
|   ||  | (  <_> )  Y Y  (  <_> )  | \/  |
|___||__|  \____/|__|_|  /\____/|__|  |__|
                       \/
    Itomori Installation script for Linux (Fish)'

echo $logo
echo
echo "Installation script by Ahum Maitra. This Linux installation script helps you to install Itomori and it's also creates a desktop shortcut for you!"
echo
echo
echo
echo

# ───────────────────────────────────────────
# VARIABLES
# ───────────────────────────────────────────
set REPO_URL "https://github.com/TheAhumMaitra/Itomori"
set INSTALL_DIR "$HOME/Itomori"
set DESKTOP_FILE "$HOME/.local/share/applications/itomori.desktop"

# ───────────────────────────────────────────
# CHECK PYTHON
# ───────────────────────────────────────────
if not command -v python3 >/dev/null 2>&1
    echo "Python3 not found. Installing..."

    if command -v apt >/dev/null 2>&1
        sudo apt update; and sudo apt install -y python3 python3-venv python3-pip
    else if command -v pacman >/dev/null 2>&1
        sudo pacman -Sy --noconfirm python python-pip
    else if command -v dnf >/dev/null 2>&1
        sudo dnf install -y python3 python3-pip
    else if command -v emerge >/dev/null 2>&1
        sudo emerge --ask dev-lang/python
    else
        echo "Unsupported distro, please install Python manually."
        exit 1
    end
end

echo "Python found! Good luck!"

# ───────────────────────────────────────────
# CLONE REPO
# ───────────────────────────────────────────
if test -d "$INSTALL_DIR"
    echo "Directory already exists. Pulling latest change!"
    git -C "$INSTALL_DIR" pull
else
    echo "Cloning Itomori repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
end

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

printf "[Desktop Entry]
Name=Itomori
Comment=Itomori
Exec=Itomori
Terminal=true
Type=Application
Categories=Utility;
" > "$DESKTOP_FILE"

chmod +x "$DESKTOP_FILE"

echo "Desktop app entry created: $DESKTOP_FILE"
echo "You can now search Itomori in your applications menu."

# ───────────────────────────────────────────
echo
echo "🎉 Installation complete! Have fun!"
echo
echo "Thanks for using Itomori ❤️! Merry Christmas 🎅 🎄!"
