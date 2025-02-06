#!/bin/bash
while true; do
    git add .
    git commit -m "Auto-commit: $(date)"
    git push origin main
    sleep 60  # Wait for 1 minute before checking again
done
