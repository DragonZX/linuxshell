#!/bin/bash
# You MUST run it under sudoer!!! Not root!!!
# You MUST run it on amd64 os ONLY!!!
read -p 'Which architecture do you want to build [x86/amd64/arm](x86): ' arch
#Installing required packages
sudo apt-get install git-core gitk git-gui subversion curl
#Updating repo
curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
#Configuring git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
#Getting depot tools
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH="$PATH":`pwd`/depot_tools
echo 'export PATH="$PATH":`pwd`/depot_tools' >> .bashrc
#Configuring 
cd /tmp
cat > ./sudo_editor <<EOF
#!/bin/sh
echo Defaults \!tty_tickets > \$1 # Entering your password in one shell affects all shells
echo Defaults timestamp_timeout=180 >> \$1 # Time between re-requesting your password, in minutes
EOF
chmod +x ./sudo_editor
sudo EDITOR=./sudo_editor visudo -f /etc/sudoers.d/relax_requirements
#Getting ChromiumOS
cd ${SOURCE_REPO}
repo init -u https://git.chromium.org/chromiumos/manifest.git
repo sync
#Compiling
cros_sdk -- ./build_packages --board=$arch-generic
cros_sdk -- ./build_image --board=$arch-generic
cros_sdk -- ./image_to_usb.sh --board=$arch-generic