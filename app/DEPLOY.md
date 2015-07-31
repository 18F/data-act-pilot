---
title: Deploying DATA Act Pilot app to Cloud Foundry
---
These are instructions for the internal 18F team on deploying the DATA Act pilot to Cloud Foundry. The following steps are instructions for deployment and is best done through the command line. 

1. Set up Cloud Foundry on your computer. Follow the documentation [https://docs.18f.gov/getting-started/setup/](https://docs.18f.gov/getting-started/setup/)
2. Set up your account by [creating an issue in the DevOps issue tracker](https://github.com/18F/DevOps/issues/new). 
4. Login: `cf login`
3. Connect to the 18F api: `cf api https://api.18f.gov`
5. Enter you username (gsa email) and password
6. A prompt will display to choose an org - select org #2. data-act
7. Followed by another promt to choose a space - select space #3. pilot-dev
8. Steps 5 and 6 can be done using the command `cf target -o data-act -s pilot-dev`
9. Make sure you are in the `app/` folder of the data-act repo
10. To build the site `cf push`

This application is password protected. To update authorization credentials: 

1. Log in
2. Set username: `cf set-env data-act-pilot-v2  WEB_USERNAME '<username>'`
3. Set password:  `cf set-env data-act-pilot-v2  WEB_PASSWORD '<password>'` 
4. To check if those credentials saved: `cf restage data-act-pilot` 



