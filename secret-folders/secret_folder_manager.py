#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any

CONFIG_DIR = Path.home() / ".config" / "lighthouse"
STATE_FILE = CONFIG_DIR / "secret_folders.json"

def ensure_state() -> Dict[str, Any]:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not STATE_FILE.exists():
        data = {"hotkey": "Meta+Shift+H", "hidden": False, "folders": []}
        STATE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return data
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))

def save_state(data: Dict[str, Any]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def normalize_path(path: str) -> str:
    return str(Path(path).expanduser().resolve())

def register_folder(path: str) -> None:
    data = ensure_state()
    path = normalize_path(path)
    folder = Path(path)
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Folder does not exist: {path}")
    if any(item["path"] == path for item in data["folders"]):
        return
    data["folders"].append({
        "path": path,
        "name": folder.name,
        "parent": str(folder.parent),
        "encrypted": False,
    })
    save_state(data)

def unregister_folder(path: str) -> None:
    data = ensure_state()
    path = normalize_path(path)
    data["folders"] = [item for item in data["folders"] if item["path"] != path]
    save_state(data)

def _hidden_name(name: str) -> str:
    return name if name.startswith(".") else f".{name}"

def hide_all() -> None:
    data = ensure_state()
    for item in data["folders"]:
        parent = Path(item["parent"])
        visible = parent / item["name"]
        hidden = parent / _hidden_name(item["name"])
        if visible.exists():
            visible.rename(hidden)
            item["path"] = str(hidden.resolve())
        elif hidden.exists():
            item["path"] = str(hidden.resolve())
    data["hidden"] = True
    save_state(data)

def show_all() -> None:
    data = ensure_state()
    for item in data["folders"]:
        parent = Path(item["parent"])
        hidden = parent / _hidden_name(item["name"])
        visible = parent / item["name"]
        if hidden.exists():
            hidden.rename(visible)
            item["path"] = str(visible.resolve())
        elif visible.exists():
            item["path"] = str(visible.resolve())
    data["hidden"] = False
    save_state(data)

def toggle_all() -> bool:
    data = ensure_state()
    if data.get("hidden", False):
        show_all()
        return False
    hide_all()
    return True

def set_hotkey(hotkey: str) -> None:
    data = ensure_state()
    data["hotkey"] = hotkey
    save_state(data)

def lock_all() -> None:
    hide_all()

def enable_encryption(path: str) -> None:
    data = ensure_state()
    path = normalize_path(path)
    for item in data["folders"]:
        if item["path"] == path:
            item["encrypted"] = True
            break
    save_state(data)

if __name__ == "__main__":
    print(json.dumps(ensure_state(), indent=2))
