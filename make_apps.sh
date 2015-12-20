#!/bin/sh
# make_apps.sh
# Composite each app onto the tile
# This requires ImageMagick

[ -d res/apps ] || mkdir res/apps
cd res/apps-raw
for file in * ; do
    newfile="../apps/$file"
    # Only convert new images or modified images
    if [ ! -e "$newfile" -o "$file" -nt "$newfile" ]; then
        composite "$file" ../tile.tiff -gravity center "../apps/$file"
    fi
done
