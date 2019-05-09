#!/bin/bash

# Upgrades a headless factorio installation using the lastest "experimental"
# build. Assumes that factorio has been set up as a systemd service. Requires
# `sudo` to run.

DIST_URL="https://www.factorio.com/get-download/latest/headless/linux64"
TAR_FILE="$HOME/factorio-latest.tar.xz"
INSTALL_DIR="/factorio"

echo "Downloading archive from: $DIST_URL"
wget "$DIST_URL" -O "$TAR_FILE"

echo "Stopping factorio service..."
systemctl stop factorio.service

echo "Extracting archive..."
tar -xf "$TAR_FILE" -C "$INSTALL_DIR" --strip-components=1

echo "Removing archive..."
rm -f "$TAR_FILE" 

echo "Changing permissions..."
chown -R factorio:factorio "$INSTALL_DIR"

echo "Starting factorio service..."
systemctl start factorio.service

echo "Done."
