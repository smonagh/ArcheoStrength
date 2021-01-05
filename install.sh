#!/bin/sh

# Install python
sudo apt install python3
sudo apt install python3-pip

# Setup python environment
sudo pip3 install virtualenv
python3 -m virtualenv env
. env/bin/activate
pip install -r requirements.txt

# Setup flask database 
flask db init
flask db migrate
flask db upgrade

# Install firefox
sudo apt install firefox

# Move desktop environment to proper folder
currentPath=`pwd`
desktopDir=~/.local/share/applications/archeo-strength.desktop
execPath="$currentPath/ArcheoStrength"
iconPath=$currentPath/resources/as_logo_short.png

rm $desktopDir
echo $currentPath 
echo $execPath
echo $iconPath

touch $desktopDir
echo "[Desktop Entry]" >> $desktopDir
echo "Name=ArcheoStrength" >> $desktopDir
echo "Exec=$execPath" >> $desktopDir
echo "Terminal=false" >> $desktopDir
echo "Type=Application" >> $desktopDir
echo "Icon=$iconPath" >> $desktopDir

