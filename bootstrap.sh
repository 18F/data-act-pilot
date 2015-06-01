#!/usr/bin/env bash

apt-get update
apt-get install git -y
apt-get install python-dev -y
apt-get install python-pip -y
apt-get install libffi-dev -y
apt-get install libssl-dev -y

pip install virtualenv
pip install virtualenvwrapper

sudo su vagrant <<'EOF'
mkdir ~/.virtualenvs
echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv" >> ~/.bashrc
echo "export DOT_GOV_API_KEY='YOUR_SAM_API_KEY'" >> ~/.bashrc
echo "export PYTHONPATH=/vagrant" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv intercessor
pip install -r /vagrant/requirements.txt
EOF
