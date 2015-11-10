# Development of the DATA Act Broker Prototype

If you're a developer who wants to work on the broker prototype, you're in the right place.

## Setup

These instructions explain how to set up the DATA Act pilot for development. The
development environment requires node.js and npm for the front end. For the
back end there are two separate process to run the app: vagrant or python
virtualenv.

### Get the Code

From the command line, clone the project repository from GitHub to your local environment:

        $ git clone git@github.com:18F/data-act-pilot.git

**Note:** if you don't have a GitHub account and want to get a read-only version of the code, use this command instead:

        $ git clone git://github.com/18F/data-act-pilot.git

### Install Front End Dependencies
1. Install node.js, which also installs the npm package manager needed to get the website up and running:
[https://github.com/nodejs/node-v0.x-archive/wiki/Installation](instructions)

2. Install the front end dependencies:

        npm install

3. Run the front end build:

        npm run build

### Install Back End Dependencies
There are two separate ways to run the Python-based backend:

1. Python virtualenv
2. Vagrant

Use Vagrant if your machine doesn't already have a Python environment set up. Also use Vagrant if you're developing on a Windows machine. Otherwise, python virtualenv is the easier option.

#### 1. Through Python Virtualenv
1. Make sure that Python 2.7 and Python virtualenv are installed.
2. Create a virtual environment for the site:

        virtualenv -p /usr/bin/python2.7 ~/virtualenvs/data-act`
3. Activate the virtualenv you just created:

        source ~/virtualenvs/data-act/bin/activate
4. Change to the folder that contains the web application:

        cd app/

5. Install the backend dependencies:

        pip install -r requirements.txt

6. Run the web app:

        python app.py

7. Visit `http://127.0.0.1:5000` in your web browser to see the live application.

Note: The username and password are both blank with this setup

#### 2. Through Vagrant

1. Install VirtualBox ([https://www.virtualbox.org/wiki/Downloads](download))
and Vagrant ([https://www.vagrantup.com/](download)).

2. Run the command to bring Vagrant up. This can take a significant amount of time the first time you run it but should be faster on subsequent
runs.

        $ vagrant up

3. Once the Vagrant box is up and running, ssh into it and start the web application:

    $ vagrant ssh  
    [you should now be on the Vagrant box]  
    $ cd /vagrant/app  
    $ python app.py

4. Visit `http://127.0.0.1:5050` in your web browser to see the live application.
5. Once you're finished developing, you can bring down the Vagrant box by typing `vagrant
halt` on the command line and bring it up again by typing `vagrant up`.

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
