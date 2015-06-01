#!/usr/bin/env bash

apt-get update
apt-get install git -y
apt-get install python-dev -y
apt-get install python-pip -y
apt-get install libffi-dev -y

# Add Postgres repository to apt
cd /etc/apt/sources.list.d/
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade -y

# Install the Postgresql 9.4 packages
sudo apt-get install postgresql-9.4 -y
sudo apt-get install postgresql-contrib-9.4 -y

apt-get install python-psycopg2 -y
apt-get install libpq-dev -y

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
