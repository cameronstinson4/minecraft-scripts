#!/bin/bash

# Upgrades a headless minecraft installation using the lastest "experimental"
# build. Assumes that minecraft has been set up as a systemd service. Requires
# `sudo` to run.

DIST_URL="https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar"
TAR_FILE="/minecraft/server.jar"
INSTALL_DIR="/minecraft"

UPGRADE="$1"

echo "Downloading archive from: $DIST_URL"
wget "$DIST_URL" -O "$TAR_FILE"

if [ "$UPGRADE" == "upgrade" ]
then

    echo "Stopping minecraft service..."
    systemctl stop minecraft.service
fi

echo "Changing permissions..."
chown -R minecraft:minecraft "$INSTALL_DIR"

if [ "$UPGRADE" == "upgrade" ]
then
    echo "Starting minecraft service..."
    systemctl start minecraft.service
fi

echo "Done."
