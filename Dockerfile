FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y debootstrap squashfs-tools xorriso grub-pc-bin grub-efi-amd64-bin mtools rsync curl git python3 sudo

WORKDIR /builder
COPY . /builder

RUN chmod +x docker-build.sh build/*.sh

CMD ["./docker-build.sh"]
