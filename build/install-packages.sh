#!/usr/bin/env bash
source build/variables.sh
cp config/packages.list $CHROOT/root/
chroot $CHROOT bash -c "apt update && xargs apt install -y < /root/packages.list"
