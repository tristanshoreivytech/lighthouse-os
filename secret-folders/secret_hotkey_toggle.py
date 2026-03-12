#!/usr/bin/env python3
from secret_folder_manager import toggle_all

if __name__ == "__main__":
    hidden = toggle_all()
    print("Secret folders hidden" if hidden else "Secret folders visible")
