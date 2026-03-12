# Secret Folders

This subsystem adds encrypted secret folders with quick hide/show support.

Main components:
- secret_folder_manager.py: tracks secret folders and visibility state
- secret_folder_cli.py: command-line interface for managing folders
- secret_hotkey_toggle.py: toggles hidden/visible state
- dolphin_secret_menu.desktop: file manager integration entry
- lighthouse-secret-folders.service: background manager service

State file:
    ~/.config/lighthouse/secret_folders.json

Visibility strategy in this prototype:
- Marked secret folders are renamed with a leading dot when hidden
- Visible folders are restored to their original names
- Metadata is tracked in a JSON state file
- Encryption command stubs are provided for future fscrypt/LUKS integration
