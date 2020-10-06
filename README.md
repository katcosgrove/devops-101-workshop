# Workshop: DevOps 101

Maintained by: Kat Cosgrove, kat.cosgrove@gmail.com, @dixie3flatline


## Course Description


When you’re new to an industry, you encounter a lot of new concepts. This can make it really difficult to get your feet underneath you on an unfamiliar landscape, especially for junior engineers. What does DevOps really mean? What’s all this software? What’s all this jargon? Is DevOps a methodology, or a toolset? Is any of this actually going to make my life easier, or is it just a bunch of industry buzzwords? I’ll answer all of these questions (and more) during this hands-on workshop, and get you set up with an end-to-end DevOps solution to automate your build artifact storage, vulnerability detection, testing, and deployment. For profit and glory!


## Prerequisites

1. [JFrog Cloud account](https://jfrog.com/artifactory/start-free/#saas)

    This is free, no credit card required. It includes access to Artifactory, Pipelines, and Xray, with a limited amount of storage, transfer, and build minutes. NOTE: To follow this workshop, you must choose either AWS or Azure as your cloud provider. JFrog Pipelines is not currently available on GCP.

2. Docker

    The Docker client should be installed and configured on your machine.

3. Python3

    We will need to package a simple Python application. Python 3.6 or higher is required.

4. Code editor

    Whatever you are most comfortable with. I will be using SublimeText. 


## Course Outline


### [Intro to DevOps](https://github.com/katcosgrove/devops-101-workshop/blob/master/docs/intro.md)
- What is the definition of DevOps?
- What does DevOps mean for developers?
- What is all of this jargon?


### [Artifactory Module](https://github.com/katcosgrove/devops-101-workshop/blob/master/docs/artifactory.md)
- What is binary repository manager?
- What are build artifacts?
- Why might you need to manage your build artifacts?
- Binary repository setup in Artifactory
    - Docker
    - PyPi


### [Xray Module](https://github.com/katcosgrove/devops-101-workshop/blob/master/docs/xray.md)
- Why do devs need to worry about vulnerability detection and license compliance?
- Security and License policies
- Scan a Build
- Running Reports
- Reading Results


### [Pipelines Module](https://github.com/katcosgrove/devops-101-workshop/blob/master/docs/pipelines.md)
- What is CI/CD?
- Pipelines Integrations
- Writing a “Hello World” pipeline


### Additional Resources

[Glossary of Terms](https://github.com/katcosgrove/devops-101-workshop/blob/master/docs/glossary.md)

[Artifactory Documentation](https://www.jfrog.com/confluence/display/JFROG/Package+Management)

[Xray Documentation](https://www.jfrog.com/confluence/display/JFROG/Xray+Security+and+Compliance)

[Pipelines Documentation](https://www.jfrog.com/confluence/display/JFROG/Pipelines+Developer+Guide)
