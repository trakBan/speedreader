#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
   echo "Uninstall script must be run as root" 
   exit 1
fi

# Deletes speedreader from /usr/bin/
rm /usr/bin/speedreader

# Deletes config file directory
rm -rf ~/.config/speedreader

speedreader || echo "speedreader has been sucesfully uninstalled."