#TODO script to set up Python 3.9 as default version
# Sets current directory to ~/.build/
cd "$(dirname "$0")"
cd ../../.build/ # Not in final version
sudo pip3 install --upgrade pip3 setuptools wheel
# Installs the dependencies
sudo pip3 install -r requirements.txt
# Changes the current directory to ~/src/
cd ../src/
# Runs the main code
sudo python3 main.py