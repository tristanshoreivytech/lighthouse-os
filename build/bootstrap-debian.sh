#!/usr/bin/env bash
source build/variables.sh
mkdir -p $CHROOT
debootstrap --arch=$ARCH $DEBIAN_SUITE $CHROOT $DEBIAN_MIRROR
