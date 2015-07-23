---
title: Deploying DATA Act Pilot app to Cloud Foundry
---
Deploying the site on Cloud Foundry is best done on the command line. Here are the steps to deploy the DATA Act pilot site: 

1. Set up Cloud Foundry on your computer. Follow the documentation [https://docs.18f.gov/getting-started/setup/](https://docs.18f.gov/getting-started/setup/)
2. Set up your account by [creating an issue in the DevOps issue tracker](https://github.com/18F/DevOps/issues/new). 
3. Log in: 
    ```	
    cf api https://api.18f.gov
    cf login
    ```
4. Enter you username (gsa email) and password
5. Select org 2. data-act
6. Select space - 3. pilot-dev
7. Make sure you are in the app folder of the data-act 
8. To build the site `cf push`




