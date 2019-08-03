#!/bin/bash
PKGS=(
    libmaxminddb       # GEO
)
brew update && brew upgrade 
brew install -y  "${PKGS[@]}"