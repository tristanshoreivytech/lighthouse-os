from secret_folders_bridge import run_cli

def hide_all_secret_folders() -> None:
    run_cli("hide-all")

def show_all_secret_folders() -> None:
    run_cli("show-all")

def toggle_secret_folders() -> None:
    run_cli("toggle")

def lock_all_secret_folders() -> None:
    run_cli("lock-all")

def set_secret_hotkey(hotkey: str) -> None:
    run_cli("set-hotkey", hotkey)

def add_secret_folder(path: str) -> None:
    run_cli("add", path)

def enable_secret_encryption(path: str) -> None:
    run_cli("enable-encryption", path)
