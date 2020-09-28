# Artifactory Module


This module will walk you through Artifactory. What it is, what it does, why you should use a binary repository manager, and how to get started. We will cover usage for two repository types: Docker, and Python.


## Overview


Artifactory is a universal binary repository manager. This means that it can be used to manage your build artifacts (compiled binaries, information about your builds, docker images, helm charts, etc) regardless of the technologies you're using -- Python, JavaScript, C#, Ruby, whatever. It supports 27 different package types explicitly, as well as a generic repository type for everything else. This isn't a replacement for source control tools, like GitHub or Bitbucket. Think of it as the place your code goes after it's been wrtitten and built or packaged, but before it's deployed. Repositories are broken up into three categories: local, remote, and virtual. 

**Local** repositories are what they sound like: repositories for your code, that exists locally on your machine. **Remote** repositories are also fairly self-explanatory; they contain remote code, like your project's dependencies. This functions sort of like a cache, so that after the first download, your project pulls its dependencies from the associated remote repository rather than from NPM or PyPi or whatever. **Virtual** repositories create a kind of envelope around the local and remote repositories for your project, and this is what you'll be interacting with most frequently.

A tool like this is used for many reasons, but the biggest benefits are to companies with a lot of different technologies in their stack, and companies that have security concerns requiring them to tightly control both their own code and their dependencies.


## Examples


### Docker

This step will walk you through creating a Docker repository type and uploading your container images, allowing you to use Artifactory as your Docker Registry.

1. Set Up the Repositories
    - In the upper right-hand corner, click the dropdown that displays your username and select "Quick Setup." From that screen, select Docker, click Create, and follow on-screen instructions. Default names and settings are fine for this.

    - From the main UI, clicking Artifactory -> Artifacts should now show you three new repositories: docker, docker-local, and docker-remote.

2. Get a Container
    - Let's get a small container in there. Fork and clone this repository. In sample-projects/docker-example, you will find a Dockerfile. Update it to reference your server and virtual Docker repository, like so:

        `FROM ${SERVER_NAME}.jfrog.io/${VIRTUAL_REPO_NAME}/ubuntu:16.04`

        becomes

        `FROM katc.jfrog.io/docker/ubuntu:16.04`


The SERVER NAME is the first part of the URL for your environment.

The VIRTUAL_REPO_NAME is the `docker` repository created by the quick setup wizard.

2. Build and Tag
    - In your terminal, log into the Docker client:

        `docker login ${SERVER_NAME}.jfrog.io`

    - From the same directory as your Dockerfile, build and tag your image:
         
        `docker build --tag ${SERVER_NAME}.jfrog.io/${VIRTUAL_REPO_NAME}/my-docker-image:latest .`

        Note the trailing dot.

3. Push to Artifactory
    - Now you're ready to push it to your repository:
 
        `docker push ${SERVER_NAME}.jfrog.io/${VIRTUAL_REPO_NAME}/my-docker-image:latest`

    - Back in the platform UI, in your Artifactory repository tree, you will now see your docker image!


### Python

To get started with Python in Artifactory, click the dropdown in the upper right-hand corner and select Quick Setup. From that screen, select PyPi. Click Create, and if you navigate back to Artifactory -> Artifacts in the platform UI, you'll see your new Python repositories!


1. Set Up the Repo
    - Click the PyPi virtual repository in the file tree. The name is just "PyPi." Click "Set Me Up" in the right-hand corner.
    - Enter your platform password in the screen that pops up to automatically populate the various setup commands with your instance information and keys.
    - Add the following to your .pypirc file. Typically, it is found in your home directory.
        `[distutils]
         index-servers = local
         [local]
         repository: https://${SERVER_NAME}.jfrog.io/artifactory/api/pypi/pypi
         username: <USERNAME>
         password: <PASSWORD>`

2. Deploy a Wheel
    - In the terminal, navigate to your forked copy of this repository and /sample-projects/python-example. Run this command to deploy your package as a Python wheel:
        `python3 setup.py bdist_wheel upload -r local`
    - If you want to deploye a Python egg instead, the command is this:
        `python3 setup.py sdist upload -r local`
    - Note that you may need to either update or install Setuptools and wheel for this to work. If Python throws an error when you attempt to deploy your wheel, run this command to make sure Setuptools and wheel are installed and updated:
        `python3 -m pip install --user --upgrade setuptools wheel`

At this point, you'll be able to see your package in the Artifactory repository tree, under PyPi!

3. Resolving from Artifactory
    - If you want to resolve your package from Artifactory, you need to tell pip where to look by adding the following to your .pip.conf file. It's usually found in your home directory, at .pip/pip.conf
        `[global]
        index-url = https://<USERNAME>:<PASSWORD>@${SERVER_NAME}.jfrog.io/artifactory/api/pypi/pypi/simple`
    - From then on, if you run `pip install <package name>`, it will install from your Artifactory repository rather than from PyPi.
