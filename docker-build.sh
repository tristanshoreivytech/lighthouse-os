#!/usr/bin/env bash
set -e
bash build/build-lighthouse.sh
cp work/lighthouse-os.iso /output/
