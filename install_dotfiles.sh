#!/bin/bash
WORKING_DIR=$(pwd)
# emacs
git clone https://github.com/syl20bnr/spacemacs $HOME/.emacs.d || (cd $HOME/.emacs.d ; git pull; cd $WORKING_DIR)
cp emacs/.spacemacs $HOME/.spacemacs
# i3
mkdir -p $HOME/.config/i3
cp i3/config $HOME/.config/i3/config
# i3blocks
git clone https://github.com/vivien/i3blocks-contrib $HOME/.config/i3blocks || (cd $HOME/.config/i3blocks ; git pull; cd $WORKING_DIR)
cp i3blocks/config $HOME/.config/i3blocks/config
# ssh
mkdir -p $HOME/.ssh
cp ssh/config $HOME/.ssh/config
# zsh
cp zsh/.zshrc $HOME/.zshrc
# X11
cp X11/.xinitrc $HOME/.xinitrc
cp X11/.nvidia-settings-rc $HOME/.nvidia-settings-rc
# g13
sudo cp g13/g13 /usr/bin/g13
sudo mkdir -p /etc/g13
sudo cp g13/*.bind /etc/g13/
# terminator
mkdir -p $HOME/.config/terminator
cp terminator/config $HOME/.config/terminator/config
