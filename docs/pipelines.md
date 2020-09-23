# Pipelines Module

In this module, you will learn about CI/CD as a concept. You will also learn how to use JFrog Pipelines to automate a few things you're probably doing manually right now.


## Overview

First, what does CI/CD stand for? The CI stands for Continuous Integration, and the CD can stand for either Continuous Delivery or Continuous Deployment. Practicing Continuous Integration means merging all developers’ working codebase with the source, multiple times a day. Doing this requires a series of automated build and unit tests to ensure none of the proposed changes cause problems, but the result is that bugs and integration issues are discovered much earlier in the development process. Ideally, a build is triggered with every single commit, so that failures are caught by the developer immediately and corrected. It also forces engineers to write code that’s more modular, making it easier to support later on. The interpreter or compiler might actually be executing your code, but other humans have to maintain and extend it, so readability is important.

Continuous Delivery means what it says on the box: your software updates are continuously delivered. In concert with Continuous Integration, this means you should have the ability to deploy a new build very rapidly because you’ve automated some quality gates that would otherwise need to be performed manually, like building and testing. That reduction in manual labor means you get to release a bunch of small changes, rather than one huge update every couple of months. Since you’re now making smaller, incremental changes, you can also be more confident that your release isn’t going to break when you deploy to your users. 

Continuous Deployment is similar, but it goes one step further -- deployment is automated, too. In Continuous Delivery, there is still a manual quality gate involved before an update is out in the wild. This is a controversial step for some, and requires a lot of trust in your system, but I’m personally a huge fan of it. For a modern DevOps pipeline (and thus, you) to be as efficient as possible, human involvement has to be removed wherever possible. I say this a lot, but we are really, really bad at repetitive tasks -- we get bored, we get distracted, and we’re SLOW. Write good, comprehensive tests and automate everything you can, then accept that you absolutely are going to deploy a bad update eventually, whether a human is involved in clicking the Big Green Button or not. What matters is how quickly you can respond to and correct a bad update. Both Continuous Delivery and Continuous Deployment help with that. 




