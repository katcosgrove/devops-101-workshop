# Workshop: DevOps 101

[NOTE: This is a draft. Outline subject to change somewhat as content is built.]

## Course Description


When you’re new to an industry, you encounter a lot of new concepts. This can make it really difficult to get your feet underneath you on an unfamiliar landscape, especially for junior engineers. What does DevOps really mean? What’s all this software? What’s all this jargon? Is DevOps a methodology, or a toolset? Is any of this actually going to make my life easier, or is it just a bunch of industry buzzwords? I’ll answer all of these questions (and more) during this hands-on workshop, and get you set up with an end-to-end DevOps solution to automate your build artifact storage, vulnerability detection, testing, and deployment. For profit and glory!


## Prerequisites

1. [JFrog SaaS account](https://jfrog.com/artifactory/start-free/#saas)
    This is free, no credit card required. It includes access to Artifactory, Pipelines, and Xray, with a limited amount of storage, transfer, and build minutes. 

2. Docker
    The Docker client should be installed and configured on your machine.

3. Python3
    We will need to run a hello world Python application. Python 3.6 or higher is required.

4. Code editor
    Whatever you are most comfortable with. I will be using SublimeText. 


## Course Outline


### Intro to DevOps
- What is the definition of DevOps?
- What does DevOps mean for developers?
- What is all of this jargon?


### Artifactory Module
- What does "artifact" mean?
- Why do you need to manage your build artifacts?
- Binary repository setup in Artifactory
    - PyPi
    - Docker
- JFrog CLI


### Pipelines Module
- What is CI/CD?
- Pipelines Integrations
- Writing a “Hello World” pipeline
- Deploying an application


### Xray Module
- Why do devs need to worry about vulnerability detection and license compliance?
- Security and License policies
- Scan a Build
- Reading the Results


### Wrapping Up
- Next Steps
- Thanks