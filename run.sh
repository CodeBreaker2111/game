#!/bin/bash

if which python &>/dev/null; then
    echo "python is installed"
else
    echo "python is not installed... So type in your pasword!!"
    sudo pacman -Syu; sudo pacman -S python3

if pip show pygame &>/dev/null; then
    echo "pygame is installed"
else
    echo "pygame is not installed, so type in your pasword if it asks you... NOW!!!!!!"
    pip3 install pygame

if pip show Pillow &>/dev/null; then
    echo "Pillow is installed"
else
    echo "Pillow is not installed so type in your pasword if it asks."

echo "running program..."
python3 main.py