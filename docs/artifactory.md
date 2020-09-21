# Artifactory

This module will walk you through Artifactory. What it is, what it does, why you should use a binary repository manager, and how to get started. We will cover usage for two repository types: Docker, and Python.


### Docker

This step will walk you through creating a Docker repository type and uploading your container images, allowing you to use Artifactory as your Docker Registry.

In the upper right-hand corner, click the dropdown that displays your username and select "Quick Setup." From that screen, select Docker, click Create, and follow on-screen instructions. Default names and settings are fine for this.

From the main UI, clicking Artifactory -> Artifacts should now show you three new repositories: docker, docker-local, and docker-remote. <!-- TODO: Add short explanation of local/remote/virtual repositories here. -->

Let's get a small container in there. Fork and clone this repository. In sample-projects/docker-example, you will find a Dockerfile. Update it to reference your server and virtual Docker repository, like so:

`FROM ${SERVER_NAME}.jfrog.io/${VIRTUAL_REPO_NAME}/ubuntu:16.04`

becomes

`FROM katc.jfrog.io/docker/ubuntu:16.04`


The SERVER NAME is the first part of the URL for your environment.

The VIRTUAL_REPO_NAME is the `docker` repository created by the quick setup wizard.


In your terminal, log into the Docker client:

`docker login ${SERVER_NAME}.jfrog.io`

From the same directory as your Dockerfile, build and tag your image:
 
`docker build --tag ${SERVER_NAME}.jfrog.io/${VIRTUAL_REPO_NAME}/my-docker-image:latest .`

Note the trailing dot.

Now you're ready to push it to your repository:
 
`docker push ${SERVER_NAME}.jfrog.io/${VIRTUAL_REPO_NAME}/my-docker-image:latest`

Back in the platform UI, in your Artifactory repository tree, you will now see your docker image!


### Python

To get started with Python in Artifactory, click the dropdown in the upper right-hand corner and select Quick Setup. From that screen, select PyPi. Click Create, and if you navigate back to Artifactory -> Artifacts in the platform UI, you'll see your new Python repositories!

<!-- TODO: Finish this -->