# Sets current directory to ~/.build/
cd "$(dirname "$0")"
# Installs the dependencies
sudo pip3 install -r requirements.txt
# Changes the current directory to ~/src/
cd ../src/
# Runs the main code
sudo python3 main.py