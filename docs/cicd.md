# Pipelines Module

In this module, you will learn about CI/CD as a concept. You will also learn how to use GitHub Actions and the JFrog CLI to automate a few things you're probably doing manually right now.


## Overview

First, what does CI/CD stand for? The CI stands for Continuous Integration, and the CD can stand for either Continuous Delivery or Continuous Deployment. Practicing Continuous Integration means merging all developers’ working codebase with the source, multiple times a day. Doing this requires a series of automated build and unit tests to ensure none of the proposed changes cause problems, but the result is that bugs and integration issues are discovered much earlier in the development process. Ideally, a build is triggered with every single commit, so that failures are caught by the developer immediately and corrected. It also forces engineers to write code that’s more modular, making it easier to support later on. The interpreter or compiler might actually be executing your code, but other humans have to maintain and extend it, so readability is important.

Continuous Delivery means what it says on the box: your software updates are continuously delivered. In concert with Continuous Integration, this means you should have the ability to deploy a new build very rapidly because you’ve automated some quality gates that would otherwise need to be performed manually, like building and testing. That reduction in manual labor means you get to release a bunch of small changes, rather than one huge update every couple of months. Since you’re now making smaller, incremental changes, you can also be more confident that your release isn’t going to break when you deploy to your users. 

Continuous Deployment is similar, but it goes one step further -- deployment is automated, too. In Continuous Delivery, there is still a manual quality gate involved before an update is out in the wild. This is a controversial step for some, and requires a lot of trust in your system, but I’m personally a huge fan of it. For a modern DevOps pipeline (and thus, you) to be as efficient as possible, human involvement has to be removed wherever possible. I say this a lot, but we are really, really bad at repetitive tasks -- we get bored, we get distracted, and we’re SLOW. Write good, comprehensive tests and automate everything you can, then accept that you absolutely are going to deploy a bad update eventually, whether a human is involved in clicking the Big Green Button or not. What matters is how quickly you can respond to and correct a bad update. Both Continuous Delivery and Continuous Deployment help with that. 

To start, you need a CI/CD tool. For this workshop, we’ll be using JFrog Pipelines, but there are also instructions for GitHub Actions and the JFrog CLI. This is what’s going to automate a bunch of manual processes for you. You set something as a trigger, like telling it to watch your source repository for a commit or a merge. You then configure a series of steps, each with pass/fail conditions, like telling it how to run your unit tests, build the code, scan for vulnerabilities, or deploy your application. With a sufficiently detailed CI/CD pipeline, you don’t have to do anything but write code and push it -- the system handles everything else for you. In most CI tools, these steps are defined with a format called YAML, in a file that lives in your code repository. There is also a web interface that gives you a graphical overview of what your steps look like, with logging output so you know exactly what’s going on and when.


## Setup and Usage


### With JFrog Pipelines

1. Add an Artifactory Integration
    - Your Pipeline will be consuming and producing artifacts and builds, so first, we need to connect your Artifactory instance to it.
    - Generate and copy an API Key from your User Profile by clicking on the admin username on the top right of the JFrog platform and selecting Edit Profile. Enter your password, then click the gear icon to generate an API key. Copy it.
    - Navigate back to the Application Module. Expand the Pipelines menu on the left, and click Integrations.
    - Create a new integration called “art” of the type Artifactory, with the url “${SERVER_NAME}/artifactory” (e.g. “https://katc.jfrog.io/artifactory”), your username, and the API Key you just copied.


2. Add a GitHub Integration
    - Log in to your GitHub account and generate a new personal access token called “pipelines-token” that has all permissions for "repo" and "admin:repo_hook." Click your profile picture in the upper right-hand corner, go to Settings, then Developer Settings and Personal Access Tokens.
    - In the JFrog Platform, navigate back to the Application module, create a new integration called “my_github” of the type GitHub, with the Token you just created in your GitHub account.
    - In your fork of this repository, in the python-example repository, you will find a pre-defined sample pipeline YAML file.
    - Update the pipeline definition by editing the pipelines.yml file, and changing the path from my repository to your fork. For example:

        `path: katcosgrove/devops-101-workshop`

        becomes

        `path: lorilorusso/devops-101-workshop`


4. Add a Pipeline Source
    - Navigate back to the Application module. Expand the Pipelines menu, and the Pipeline Sources menu. Add your forked GitHub repository as a Single Branch pipeline source. The Integration should be named “my_github” and the Repository Full Name should be the path to your forked repo, e.g., “katcosgrove/devops-101-workshop”. You can leave the branch set to Main or Master, and the Pipeline Config File Filter set to “pipelines.yml”.


5. Manually Trigger the Pipeline
    - Navigate back to the Application module, expand the Pipelines menu and click the My Pipelines menu item. Click on the basic_pipeline, click on step_1 to trigger the step.


### With the JFrog CLI and GitHub Actions

1. Install the JFrog CLI
    - Your workflow will be consuming and producing artifacts and builds, so first, we need to connect your Artifactory instance to it. To do that, we need to install the JFrog CLI and get an access token. You can get the CLI from this URL: https://jfrog.com/getcli/
    - Multiple methods of installation are provided. If you’re on a Mac, you want the Homebrew command. Just run that in your terminal. If you’re on Windows, you want the Curl option or you can just download one of the three executables at the bottom of the page.

2. Configure the JFrog CLI
    - Once installed, open your terminal and run the command `jfrog rt c` to begin. Default answers are fine; just remember what you name the Artifactory server. Mine is art-1, but yours is probably Default-Server.
    - You do not need to use an access token. Just use username and password, which will be the login for your JFrog platform instance -- an email address and password. 
    - Once logged in, run the following command to get a token:

        `jfrog rt c export Default-Server`


3. Create a Workflow
    - In your fork of this repository, in the .github/workflows directory,  you will find a pre-defined sample workflow YAML file called blank.yml
    - Update the definition by editing the blank.yml file, and changing the path from my Artifactory instance to yours in both the Docker Build and Push commands. For example:

        `docker build --tag katc101.jfrog.io/docker/my-docker-image:latest ./sample-projects/docker-example`

        becomes

        `docker build --tag batelt.jfrog.io/docker/my-docker-image:latest ./sample-projects/docker-example`


4. Add Secrets
    - Commit and push your changes, then go to your GitHub repository. We need to add some secrets, so that the Workflow can access your Artifactory instance without publicly committing passwords and access tokens to GitHub. Click Settings at the top, then Secrets on the left.
    - Add three new secrets called JF_ARTIFACTORY_USER, JF_ARTIFACTORY_PASSWORD, JF_ARTIFACTORY_SECRET. The value of USER is the email address you use to log into your JFrog platform, PASSWORD is the password you use, and SECRET is the token we generated from the JFrog CLI earlier.
    - At the top of your GitHub repo, you’ll see a button that says Actions. Click that, and you’ll see one called “sample-workflow.” That’s your new CI pipeline!


5. Trigger the Workflow
    - Make a change to something in your fork of this repository, like typing “Hi, JFrog!” somewhere in the README.md file. Add, commit, and push that change, then go look at GitHub!
    - Under the Actions tab in your repository, click sample-workflow and you'll see a build running. Click it to expand and see what each of the steps is doing!