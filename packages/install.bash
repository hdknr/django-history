#!/bin/bash
for i in *; do
    if [ -d $i ]; then
       pip install -e $i; 
    fi
done
# 
## init
# git submodule update --init --recursive
## update 
# git pull --recurse-submodules
