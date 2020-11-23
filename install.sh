#!/bin/bash

#Python Installtion 
if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/petoolkit"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true
    pkg install -y git python3
else
    INSTALL_DIR="$HOME/.petoolkit"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
    sudo apt install -y git python3.9
fi

#Checking if Petlookit is installed already
if [ -d "$INSTALL_DIR" ]; then
    echo "Petoolkit was found! Do you want to replace it?(y/n): " ;
    read -r check
    if [ "$check" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/petoolkit*"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/petoolkit*"
        fi
    else
        echo "If you want to install you must remove previous version.";
        echo "Installation failed!";
        exit
    fi
fi
echo "Cleaning up old directories...";
if [ -d "$ETC_DIR/ahrixia" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/ahrixia"
    else
        sudo rm -rf "$ETC_DIR/ahrixia"
    fi
fi

echo " Installing ...";
echo "";
git clone --depth=1 https://github.com/ahrixia/Petoolkit "$INSTALL_DIR";
echo "#!$BASH_PATH
python3 $INSTALL_DIR/petoolkit.py" "${1+"$@"}" > "$INSTALL_DIR/petoolkit";
chmod +x "$INSTALL_DIR/petoolkit";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/petoolkit" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/petoolkit" "$BIN_DIR"
fi
rm "$INSTALL_DIR/petoolkit";


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "Congratulations! Tool is installed successfully!";
    echo "";
    echo "***************************************************************************";
    echo "    Installation done!! You can run the tool by typing petoolkit !";
    echo "***************************************************************************";
    echo "";
else
    echo "Sorry! Installation failed! ";
    exit
fi

