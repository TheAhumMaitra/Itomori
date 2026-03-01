# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later


"""
This library helps to access all, components for creating Itomori.

All core components/ widgets of Itomori.
"""

from pathlib import Path

__version__ = "1.1.2"

# Paths
ITOMORI_DATA_DIR = Path.home() / ".local/share/Itomori"
ITOMORI_STATE_DIR = Path.home() / ".local/state/Itomori"
ITOMORI_CONFIG_DIR = Path.home() / ".config/Itomori"

LOG_PATH = ITOMORI_STATE_DIR / "log/app.log"
DB_PATH = ITOMORI_DATA_DIR / "notes.json"
CONFIG_PATH = ITOMORI_CONFIG_DIR / "config.toml"

# Ensure directories exist
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
ITOMORI_DATA_DIR.mkdir(parents=True, exist_ok=True)
ITOMORI_CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_settings():
    """Load settings from config.toml"""
    import tomllib
    
    if not CONFIG_PATH.exists():
        return {"logs": True}
    
    try:
        with open(CONFIG_PATH, "rb") as f:
            return tomllib.load(f)
    except Exception:
        return {"logs": True}


def save_settings(settings):
    """Save settings to config.toml"""
    # Simple TOML generator to avoid external dependencies if not present
    # since we only have one boolean setting for now.
    lines = []
    for key, value in settings.items():
        if isinstance(value, bool):
            lines.append(f'{key} = {str(value).lower()}')
        elif isinstance(value, str):
            lines.append(f'{key} = "{value}"')
        else:
            lines.append(f'{key} = {value}')
    
    CONFIG_PATH.write_text("\n".join(lines) + "\n")
