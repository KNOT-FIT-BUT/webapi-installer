# Webapiner-installer
This is a pack of scripts for building and maintaining webapiner project. 


## How to build
Clone this repository and enter script directory. First you have to modify vars file. Modify GIT_SSH_USER variable for secapi git. Without it wont be possible clone secapi repository. 
After that, enter main projet directory and run `setup install`. 

## How to run
After build, you have to run SharedKB daemon and Webapi server. Both can be controlled via init.d scripts in the main directory.
```webapi start|stop|status```
```sharedkb start|stop|status```
SharedKB must be always launched BEFORE webapi!!! Webapi will bind to IP 0.0.0.0 at port 8090.

##Scripts description
Each part of the project has its own script for install|update|clean.
 - **create-venv** - installs dependencies via apt-get, and create virtual enviroment for python + requred libraries
 - **clone-repos** - clone all repositories into `repos` folder
 - **deploy-server** - copy server code from its repository to `server` folder
 - **deploy-ui** - copy ui code from its repository to `server/static*` folders
 - **deploy-secapi** - copy secapi tools from its repository and build them
 - **deploy-assets** - download kb and fsa assets and create necessary symlinks
If manualy used, scripts should be executed in this oreder.


