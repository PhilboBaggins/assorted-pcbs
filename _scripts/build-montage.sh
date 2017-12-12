#!/bin/sh

OUTPUT_FILE_NAME="boards-montage.jpg"

# TODO: Check that imagemagick is installed

heading() {
    local msg_string=$1
    local msg_string="${msg_string:-...}"
    echo "\033[32;1m##\033[0m\033[1m ${msg_string}\033[0m"
}

SCRIPT_DIR="`dirname -- "${0}"`"
cd "$SCRIPT_DIR/../"

clear

heading "Git status of board-photo.jpg image files"
git status */board-photo.jpg
echo

heading "Building montage with:"
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
