# Updates to latest version
sudo apt update && sudo apt upgrade
# Installs opencv
sudo apt install python3-opencv
# Sets current directory to ~/.build/
cd "$(dirname "$0")"
cd ../../.build/ # Not in final version
# Installs the other dependencies
sudo pip3 install -r requirements.txt
# Changes the current directory to ~/src/
cd ../src/
# Runs the main code
sudo python3 main.py
