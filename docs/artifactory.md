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
