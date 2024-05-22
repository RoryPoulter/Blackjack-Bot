#TODO script to set up Python 3.9 as default version
# Gets the current version of Python
ver="$(python -V)"
# Checks if the version is correct
if [ "$ver" = "Python 3.12.3" ]; then
    echo "Correct version"
else
    echo "Python needs updating to 3.12"
fi


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