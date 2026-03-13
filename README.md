# Lighthouse OS
Privacy‑centered offline‑first Linux distribution.

Build on Windows:
    Download the latest version of Docker Desktop at https://www.docker.com/products/docker-desktop/
    
    build-lighthouse.bat

Build on Linux:
    ./build/build-lighthouse.sh

Secret Folders
--------------
This project includes a prototype Secret Folder subsystem.

Capabilities:
- Mark folders as Secret
- Hide/show all Secret Folders with a configurable hotkey
- Persist visibility state
- Integrate controls into Privacy Center
- Prepare for per-folder encryption using fscrypt or LUKS-backed containers
