---
title: Local development of DATA Act pilot app
---
These instruction explain how to set up the DATA Act pilot for development. The
development environment requires node.js and npm for the front end. For the
backend there are two separate process to run the app: vagrant or python
virtualenv.

## Frontend
1. Install node.js, which also installs the npm package manager needed to get the website up and running:
[https://github.com/nodejs/node-v0.x-archive/wiki/Installation](instructions)
2. Install all the front end dependencies with `npm install`
3. Run the front end build with `npm run build`. The command `npm run watch` can
also be used to continually watch and rebuild on changes.

## Backend
There are two separate ways to run the backend: python virtualenv or vagrant.
Vagrant should be used if there is not a python environment already set up or
the system is any Windows. Otherwise python virtualenv is the easier option.

### Through python virtualenv
1. Ensure python2.7 and python virtualenv are both installed.
2. Make a py2.7 virtualenv for the site: `virtualenv -p /usr/bin/python2.7
~/virtualenvs/data-act`
3. Activate the just created virtualenv: `source
~/virtualenvs/data-act/bin/activate`
4. `cd app/`
5. Install backend dependencies, `pip install -r requirements.txt`
6. Run the app, `python app.py`
7. Visit `http://127.0.0.1:5000` to see the live app.

Note: The username and password are both blank with this setup

### Through vagrant
1. Ensure and virtualbox ([https://www.virtualbox.org/wiki/Downloads](download))
vagrant ([https://www.vagrantup.com/](download)) are both installed.
2. Run the command to bring vagrant up, this command can take a signifigant
amount of time the first time it is run but should run faster on subsequent
runs. `vagrant up`
6. Visit `http://10.0.0.2:5000` to see the live app.
7. Once finished developing, the vagrant box can be brought down with `vagrant
halt` and brought back up with `vagrant up`.

Note: The username and password are both blank with this setup
