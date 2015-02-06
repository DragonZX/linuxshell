#!/bin/bash
ver=3.17.4
# uncomment it if you don't have developer packages
apt-get -y install make kernel-package libncurses5-dev fakeroot wget build-essential bc
echo Installing $ver
cd /usr/src
wget kernel.org/pub/linux/kernel/v3.x/linux-$ver.tar.xz
tar xvf linux-$ver.tar.xz
rm linux
ln -s linux-$ver linux
cd /usr/src/linux
cp /boot/config-`uname -r` ./.config
make oldconfig
make menuconfig
# uncomment it if you want to reconfigure the kernel
make-kpkg clean
fakeroot make-kpkg --initrd kernel_image kernel_headers kernel_doc kernel_source
cd /usr/src
dpkg -i linux-image*.deb
#rm -f *.deb