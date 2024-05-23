#TODO script to set up Python 3.9 as default version
# Gets the current version of Python
ver="$(python -V)"
# Checks if the version is correct
if [ "$ver" = "Python 3.12.3" ]; then
    echo "Correct version"
else
    # Download source code
    wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
    # Install build tools
    sudo apt update
    sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev  libsqlite3-dev
    # Configure, make and install
    tar -xzvf Python-3.12.3.tgz 
    cd Python-3.12.3/
    ./configure
    sudo make altinstall
    # Create a softlink
    sudo rm /usr/bin/python
    sudo ln -s /usr/local/bin/python3.12 /usr/bin/python
    # Deletes the installation directory
    cd /tmp/
    rm -rf rm -rf Python-3.12.3.tgz Python-3.12.3/
fi


# Sets current directory to ~/.build/
cd "$(dirname "$0")"
cd ../../.build/ # Not in final version
sudo pip install --upgrade pip3 setuptools wheel
# Installs the dependencies
sudo pip install -r requirements.txt
# Changes the current directory to ~/src/
cd ../src/
# Runs the main code
sudo python main.py