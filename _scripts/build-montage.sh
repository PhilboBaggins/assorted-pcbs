#!/bin/sh

OUTPUT_FILE_NAME="boards-montage.jpg"

# TODO: Check that imagemagick is installed

SCRIPT_DIR="`dirname -- "${0}"`"
cd "$SCRIPT_DIR/../"

echo "Building montage with:"
find . -name board-photo.jpg | while read path; do
    echo "* $path"
done

NUM_BOARD_IMAGES="$(find . -name board-photo.jpg | wc -l)"
NUM_BOARD_IMAGES="${NUM_BOARD_IMAGES// /}"  # Strip whitespace from the `wc -l` output
echo "($NUM_BOARD_IMAGES files)"
echo

# Generate image montage
montage */board-photo.jpg "$OUTPUT_FILE_NAME"

ls -lh "$OUTPUT_FILE_NAME"
