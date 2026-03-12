#!/usr/bin/env bash
set -e
source build/variables.sh
bash build/bootstrap-debian.sh
bash build/install-packages.sh
bash build/build-filesystem.sh
bash build/build-iso.sh
