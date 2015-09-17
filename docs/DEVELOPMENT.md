# Development of the DATA Act Broker Prototype

If you're a developer who wants to work on the broker prototype, you're in the right place.

## Setup

These instruction explain how to set up the DATA Act pilot for development. The
development environment requires node.js and npm for the front end. For the
backend there are two separate process to run the app: vagrant or python
virtualenv.

### Frontend
1. Install node.js, which also installs the npm package manager needed to get the website up and running:
[https://github.com/nodejs/node-v0.x-archive/wiki/Installation](instructions)
2. Install all the front end dependencies with `npm install`
3. Run the front end build with `npm run build`. The command `npm run watch` can
also be used to continually watch and rebuild on changes.

### Backend
There are two separate ways to run the backend: python virtualenv or vagrant.
Vagrant should be used if there is not a python environment already set up or
the system is any Windows. Otherwise python virtualenv is the easier option.

#### Through python virtualenv
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

#### Through vagrant
1. Ensure and virtualbox ([https://www.virtualbox.org/wiki/Downloads](download))
vagrant ([https://www.vagrantup.com/](download)) are both installed.
2. Run the command to bring vagrant up, this command can take a signifigant
amount of time the first time it is run but should run faster on subsequent
runs. `vagrant up`
6. Visit `http://127.0.0.1:5050` to see the live app.
7. Once finished developing, the vagrant box can be brought down with `vagrant
halt` and brought back up with `vagrant up`.

Note: The username and password are both blank with this setup

## Orientation

This project is a prototype, so we don't expect the code to run in a production environment. That said, there may be a need to update things like data element names and validation rules as the pilot progresses. These directions are for developers who want to do that.

### Updating the Standardized CSV Templates

If you need to add a data element to one of the [four csv templates](https://github.com/18F/data-act-pilot/tree/master/schema "csv templates") or update one of the current data element names:

1. Make your change to the templates .csv files that are stored in the project's [schema folder](https://github.com/18F/data-act-pilot/tree/master/schema).
2. If you add a row and or change the _elementMappingName_ in a current row, you'll have to make some changes to the website's validation process. Keep reading!
3. For each .csv template you update, make sure to also update its corresponding _rules.csv_ file. These files drive the validation process.
    * Find the ```*._rules.csv``` files [here](https://github.com/18F/data-act-pilot/tree/master/app/validator/rules "rules files").
    * Make sure values of the _fieldname_ column in the ```*_rules.csv``` files match the values in the _elementMappingName_ columns of the .csv templates (see previous step).
    * Update the _VALIDATION_ dictionary in [app.py](https://github.com/18F/data-act-pilot/blob/master/app/app.py) to make sure the field names there match any changes you make to the .csv templates.

### Updating Validation rules

Validations in this prototype are driven by rules expressed in .csv files.

To update the basic validations (required fields, data types, field length, and uniqueness/cardinality), update the corresponding file in the [rules folder]("https://github.com/18F/data-act-pilot/tree/master/app/validator/rules "rules files").
