# DevOps 101: Intro to DevOps

Welcome to DevOps 101. This is intended to be a high-level but hands-on overview of DevOps concepts and tools, geared towards beginners. That means students, junior developers, more experienced developers who have never been exposed to DevOps before, or even non-technical folks who are curious. This is not a technical deep-dive -- it's a jumping off point for you.


### What does DevOps mean?

DevOps is the term for the union of the development team and the IT operations team, through the use of a specific set of practices and toolchains. Rather than having the development and operations team handle their own specific responsibilities independently of one another, the two teams should work together. This is both a cultural change and a technology change, with the ultimate goal of drastically shortening the amount of time it takes the team to deliver software. The result is more frequent software deployments, deploying bad updates less frequently, and being able to recover from bad updates faster.


### What does DevOps mean for Developers?

For developers, DevOps may mean changing the way you write software. Your code should be written in a way that's modular, so it's easier for other people to maintain. Microservices rather than monoliths is an example of this. You need a basic understanding of container technologies (Docker, Kubernetes), but don't necessarily need to be an expert in those things. You should be merging with your source repository and pulling from main often, sometimes multiple times a day, and making much smaller changes. Build and unit tests should run with every single commit, and that process should be automated. If the entire team does this, conflicts will happen less often and failures will be discovered much, much earlier in the software development lifecycle, allowing you to fix them immediately. The cultural shift can take some getting used to, but you will be much more efficient and much less stressed out, because a lot of the things you were doing manually before are automated by your tools.


## What's all of this jargon?

Yeah, there's a lot of it. We're absolutely swimming in abbreviations and abstractions, and sometimes it's difficult to define a term satisfactorily without needing to define three more for context. To make this easier (on me AND you), I've included a [glossary](https://github.com/katcosgrove/devops-101-workshop/blob/master/docs/glossary.md). Please note that this is a work in progress. At first, it will only cover terms mentioned in this workshop. If you come across a term that's unfamiliar in the course of going through this workshop, search the glossary! If it's not there, get in touch with me and I'll add it. You can also just open a GitHub issue.