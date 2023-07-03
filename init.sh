#!/bin/bash

# Copy py scripts to bin
cp -r find_top_songs /usr/bin

# Make logs and results directory
mkdir -p /find_top_songs/stream_logs /find_top_songs/top50_results_daily 

# Copy systemd files 
cp systemd/top50songs.timer /etc/systemd/system
cp systemd/top50songs.service /etc/systemd/system

sudo systemctl daemon-reload

# Enable and start the timer:
sudo systemctl enable top50songs.timer
sudo systemctl start top50songs.timer

