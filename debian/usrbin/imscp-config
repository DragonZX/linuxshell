#!/bin/sh
#
# i-MSCP ConfigScript Debian
# Version: 0.5.0
# License: GPLv2
# Author : i-MSCP Team, DragonZX
# Credits: i-MSCP Development Team
#----------------------------------
# Varibles and functions

read -p "Which version of i-MSCP do you want to install (i.e. 1.3.0)?: " version
case $version in 
'1.2.'*|'1.3.'*|'1.4.'*|'2.0.'*) version=$version;;
'trunk') read -p 'choose a version of trunk 1.3/1.4: ' trunkver ;;
*) version='1.3.0';;
esac

clear
echo '
--------------------------------
Welcome to i-MSCP (' $version $trunkver') installation.
--------------------------------
Choose what you want to do:
1) Install an i-MSCP 
2) Reconfigure i-MSCP
3) Debug mode
4) Uninstall an i-MSCP
5) Full backup of i-MSCP (experimental)
6) Full restore of i-MSCP (experimental)
7) Exit the installer'
read -p "Enter your choice [1-7] " choice
# Installation of a version
if [ $choice -eq 1 ] ; then
    #==== Start i-MSCP installer ====
	aptitude update && aptitude -y safe-upgrade
    aptitude -y install bzip2 wget tar unzip ca-certificates xz-utils
	clear
	if [ -f /usr/local/src/imscp/imscp-$version/imscp-autoinstall || /usr/local/src/imscp/imscp-$trunkver.x/imscp-autoinstall ]; then
		echo "Installation file exists"
	else
		mkdir -p /usr/local/src/imscp
		cd /usr/local/src/imscp
		if [ $version = "trunk" ]; then
			echo '#### Your trunk version is' $trunkver'.x ####';
			wget https://github.com/i-MSCP/imscp/archive/$trunkver.x.zip
			unzip $trunkver.x.zip
			cd imscp-$trunkver.x
		else
			echo '#### DOWNLOADING the latest i-MSCP version ####'
			wget https://github.com/i-MSCP/imscp/archive/$version.tar.gz
			tar xvfz $version.tar.gz
			cd imscp-$version
		clear
		fi
		perl imscp-autoinstall "$@"
	fi
    exit
	# Redownload i-MSCP
elif [ $choice -eq 2 ] ; then
	rm -fR /usr/local/src/imscp/
    mkdir -p /usr/local/src/imscp
    cd /usr/local/src/imscp
    aptitude update && aptitude -y safe-upgrade
    aptitude -y install bzip2 wget tar ca-certificates xz-utils
		if [ $version = "trunk" ]; then
		echo '#### Your trunk version is '$trunkver'.x ###';
		wget https://github.com/i-MSCP/imscp/archive/$trunkver.x.zip
		unzip $trunkver.x.zip
		cd imscp-$trunkver.x
		else
	echo '#### DOWNLOADING the latest i-MSCP version ####'
    wget https://github.com/i-MSCP/imscp/archive/$version.tar.gz
    tar xvfz $version.tar.gz
    cd imscp-$version
	fi
    #==== Start i-MSCP installer ====
    perl imscp-autoinstall -r "$@"
    exit
	# Uninsall i-MSCP
elif [ $choice -eq 3 ] ; then
	rm -fR /usr/local/src/imscp/
	mkdir -p /usr/local/src/imscp
    cd /usr/local/src/imscp
    aptitude update && aptitude -y safe-upgrade
    aptitude -y install bzip2 wget tar ca-sertificates xz-utils
	if [ $version = "trunk" ]; then
		echo '#### Your trunk version is '$trunkver'.x ###';
		wget https://github.com/i-MSCP/imscp/archive/$trunkver.x.zip
		unzip $trunkver.x.zip
		imscp-$trunkver.x
		else
	echo '#### DOWNLOADING the latest i-MSCP version version ####'
    wget https://github.com/i-MSCP/imscp/archive/$version.tar.gz
    tar xvfz $version.tar.gz
    cd imscp-$version
	fi
    #==== Start i-MSCP installer ====
    perl imscp-autoinstall -d "$@"
    exit
	# Uninsall i-MSCP
elif [ $choice -eq 4 ] ; then
	echo '#### UNINSTALLING an i-MSCP ####'
    cd /var/www/imscp/engine/setup
    perl imscp-uninstall
    exit
elif [ $choice -eq 5 ] ; then
	echo '#### Backuping an i-MSCP ####'
	read -p 'Please enter the MySQL root password: ' mypass
	apt-get -y install bzip2 xz-utils
	mkdir /tmp/imscpbkp
	cd /tmp/imscpbkp
	mysqldump -u root --password=$mypass --all-databases > imscp.sql
	tar cvfJ www.txz /var/www/virtual
	tar cvfJ mail.txz /var/mail/virtual
	tar cvfJ config.txz /etc/imscp 
	cd ..
	tar cvf imscp.bkp imscpbkp
	cp imscp.bkp /root/imscp.bkp
	cd /root
	clear
	echo Take it from root directory
	exit
elif [ $choice -eq 6 ] ; then
	echo '#### Restoring an i-MSCP ####'
	read -p 'Please enter the MySQL root password: ' mypass
	apt-get -y install bzip2 xz-utils
	mkdir /tmp/imscpbkp
	cp /root/imscp.bkp /tmp/imscp.bkp
	cd /tmp
	tar xvf imscp.bkp
	cd /tmp/imscpbkp
	tar xvfJ www.txz -C /
	tar xvfJ mail.txz -C /
	tar xvfJ config.txz -C / 
	mysql -u root --password=$mypass < imscp.sql
	rm -f /root/imscp.bkp
	cd /root
	clear
	echo Restoring complete
	exit
else
exit
fi
