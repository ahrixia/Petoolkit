#!/bin/bash

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    Install_directory="$PREFIX/usr/share/doc/petoolkit"
    Bin_directory="$PREFIX/bin/"
    Bash_directory="$PREFIX/bin/bash"
    TERMUX=true
else
    Install_directory="$HOME/.petoolkit"
    Bin_directory="/usr/local/bin/"
    Bash_directory="/bin/bash"
    TERMUX=false
fi
#Checking Petoolkit Directory 
if [ -d "$Install_directory" ]; then
        rm -rf "$Install_directory"
        rm "$Bin_directory/petoolkit*"
        sudo rm -rf "$Install_directory"
        sudo rm "$Bin_directory/petoolkit*"
    else
        echo "If you want to uninstall you must remove previous version";
        echo "Failed! Try Again! ";
fi
echo "Cleaning up old directories...";
if [ -d "$Other_directory/ahrixia" ]; then
    echo "$Directory_found_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$Other_directory/ahrixia"
    else
        sudo rm -rf "$Other_directory/ahrixia"
    fi
fi
clear
echo "Uninstallation Successful!"