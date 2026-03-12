#!/usr/bin/env bash
source build/variables.sh
mkdir -p $IMAGE/live
mksquashfs $CHROOT $IMAGE/live/filesystem.squashfs -comp xz -b 1M
