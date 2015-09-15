---
title: Local development of DATA Act pilot app
---
These instruction explain how to set up the DATA Act pilot for development. The
development environment requires node.js and npm for the front end. For the
backend there are two separate process to run the app: vagrant or python
virtualenv.

## Frontend
1. Install node.js and npm:
[https://github.com/nodejs/node-v0.x-archive/wiki/Installation](instructions)
2. Install all the front end dependencies with `npm install`
3. Run the front end build with `npm run build`. The command `npm run watch` can
also be used to continually watch and rebuild on changes.

## Backend
There are two separate ways to run the backend: python virtualenv or vagrant.
Vagrant should be used if there is not a python environment already set up.
Otherwise python virtualenv is easier.

### Through python virtualenv
1. Ensure python2.7 and python virtualenv are both installed.
2. Make a py2.7 virtualenv for the site: `virtualenv -p /usr/bin/python2.7
~/virtualenvs/data-act`
3. Activate the just created virtualenv: `source
~/virtualenvs/data-act/bin/activate`
4. `cd app/`
5. Install backend dependencies, `pip install -r requirements.txt`
6. Run the app, `python app.py`

### Through vagrant
1. Ensure vagrant and virtualbox are both installed.
2. `vagrant up`
3. `vagrant ssh`
4. In the vagrant app, `cd /vagrant`
5. Run the app, `python app/app.py`
