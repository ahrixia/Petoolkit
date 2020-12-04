#!/bin/bash

#Python Installtion 
if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    Install_directory="$PREFIX/usr/share/doc/petoolkit"
    Bin_directory="$PREFIX/bin/"
    Bash_directory="$PREFIX/bin/bash"
    TERMUX=true
    sudo apt-get install python3
else
    Install_directory="$HOME/.petoolkit"
    Bin_directory="/usr/local/bin/"
    Bash_directory="/bin/bash"
    TERMUX=false
    sudo sudo apt-get install python3.8
fi
sudo apt-get install python3-pip
sudo apt-get install python3-termcolor
sudo pip3 install termcolor

#Checking if Petlookit is installed already
if [ -d "$Install_directory" ]; then
    echo "Petoolkit was found! Do you want to replace it?(y/n): " ;
    read -r check
    if [ "$check" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            sudo rm -rf "$Install_directory"
            sudo rm "$Bin_directorypetoolkit"
        else
            sudo rm -rf "$Install_directory"
            sudo rm "$Bin_directorypetoolkit"
        fi
    else
        echo "If you want to install you must remove previous version.";
        echo "Installation failed!";
        exit
    fi
fi
echo "Cleaning up old directories...";
if [ -d "$Other_directory/ahrixia" ]; then
    echo "$Direcotory_found"
    if [ "$TERMUX" = true ]; then
        rm -rf "$Other_directory/ahrixia"
    else
        sudo rm -rf "$Other_directory/ahrixia"
    fi
fi

echo "Installing ...";
echo "";
git clone --depth=1 https://github.com/ahrixia/Petoolkit "$Install_directory";
echo "#!$Bash_directory
python3 $Install_directory/petoolkit.py" "${1+"$@"}" > "$Install_directory/petoolkit";
chmod +x "$Install_directory/petoolkit";
if [ "$TERMUX" = true ]; then
    cp "$Install_directory/petoolkit" "$Bin_directory"
else
    sudo cp "$Install_directory/petoolkit" "$Bin_directory"
fi
rm "$Install_directory/petoolkit";


if [ -d "$Install_directory" ] ;
then
    echo "Congratulations! Tool is installed successfully!";
else
    echo "Sorry! Installation failed! ";
    exit
fi

