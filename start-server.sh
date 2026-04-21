#!/bin/bash
while true; do
  python3 -m http.server 3000 --directory "/Users/michaeldeangelo/Desktop/Waterbury Site"
  echo "Server crashed, restarting in 1 second..."
  sleep 1
done
