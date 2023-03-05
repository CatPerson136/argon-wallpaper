#!/bin/bash

# This is the install script to install the dependences

# This will install it for Debain/Ubuntu systems
if [ -d /etc/apt ]
then
    sudo apt install pip
    pip install customtkinter
    sudo apt install python3-tk
    sudo apt install xwallpaper
fi

# This will install it for Arch and its dirivites
if [ -d /etc/pacman.d ]
then
   sudo pacman -S python3-pip 
   pip install customtkinter
   sudo pacman -S tk  
   sudo pacman -S xwallpaper