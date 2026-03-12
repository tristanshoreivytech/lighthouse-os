#!/usr/bin/env python3
import argparse
from secret_folder_manager import (
    register_folder,
    unregister_folder,
    hide_all,
    show_all,
    toggle_all,
    set_hotkey,
    lock_all,
    enable_encryption,
)

def main() -> None:
    parser = argparse.ArgumentParser(description="Manage Lighthouse Secret Folders")
    sub = parser.add_subparsers(dest="command", required=True)
    p_add = sub.add_parser("add", help="Mark a folder as secret")
    p_add.add_argument("path")
    p_remove = sub.add_parser("remove", help="Remove secret status from a folder")
    p_remove.add_argument("path")
    sub.add_parser("hide-all", help="Hide all secret folders")
    sub.add_parser("show-all", help="Show all secret folders")
    sub.add_parser("toggle", help="Toggle hidden/visible state")
    sub.add_parser("lock-all", help="Lock and hide all secret folders")
    p_hotkey = sub.add_parser("set-hotkey", help="Set toggle hotkey")
    p_hotkey.add_argument("hotkey")
    p_encrypt = sub.add_parser("enable-encryption", help="Mark folder for encryption")
    p_encrypt.add_argument("path")
    args = parser.parse_args()

    if args.command == "add":
        register_folder(args.path)
    elif args.command == "remove":
        unregister_folder(args.path)
    elif args.command == "hide-all":
        hide_all()
    elif args.command == "show-all":
        show_all()
    elif args.command == "toggle":
        hidden = toggle_all()
        print("hidden" if hidden else "visible")
    elif args.command == "lock-all":
        lock_all()
    elif args.command == "set-hotkey":
        set_hotkey(args.hotkey)
    elif args.command == "enable-encryption":
        enable_encryption(args.path)

if __name__ == "__main__":
    main()
