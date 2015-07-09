#!/usr/bin/env bash

apt-get update
apt-get install git -y
apt-get install python-dev -y
apt-get install python-setuptools
apt-get install libffi-dev -y
apt-get install libssl-dev -y

easy_install pip

pip install virtualenv
pip install virtualenvwrapper

sudo su vagrant <<'EOF'
mkdir ~/.virtualenvs 2> /dev/null
echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv" >> ~/.bashrc
echo "export DOT_GOV_API_KEY=JhAodrs4c50i41FtKNCUxgfSUjeQ1jH1Pn7qIjLp" >> ~/.bashrc
echo "export PYTHONPATH=/vagrant" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv data-act-pilot
source ~/.virtualenvs/data-act-pilot/bin/activate
pip install -r /vagrant/requirements.txt
python /vagrant/app/app.py
EOF
