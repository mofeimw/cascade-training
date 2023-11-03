#!/bin/bash

cd neg-resized

i=1
for img in *.jpg; do
    # new=${img#"neg-"}
    mv "$img" ${i}.jpg
    ((i++))
done
