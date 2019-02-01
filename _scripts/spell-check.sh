#!/bin/sh

for file in */*.md */notes.txt; do
    aspell check "$file"
done
