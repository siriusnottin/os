#!/bin/bash
# download the os package
if [ -d ~/os/.git ]; then
  echo "os package is already downloaded! Updating..."
  cd ~/os && git pull
else
  echo "Downloading the os package..."
  git clone git@github.com:siriusnottin/os.git ~/os
  git clone https://github.com/siriusnottin/os.git ~/os
fi

echo "Setting up the os command..."
ln -s ~/os/__main__.py /usr/local/bin/os 2>/dev/null
echo "os command has been set up!"
