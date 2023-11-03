#!/bin/bash

for img in neg-resized/*.jpg; do
    echo "$img" >> bg.txt
done
