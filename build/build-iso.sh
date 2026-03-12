#!/usr/bin/env bash
source build/variables.sh
mkdir -p $IMAGE/boot/grub
cp iso/boot/grub/grub.cfg $IMAGE/boot/grub/
xorriso -as mkisofs -o $ISO -iso-level 3 -full-iso9660-filenames -volid LIGHTHOUSE_OS $IMAGE
