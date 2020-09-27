# Glossary of Terms

DevOps encompasses a lot of technologies, tools, terms, abbreviations, and abstractions. To make this easier to learn, I'm including this glossary, which will be a constant work in progress and may include terms not explicitly discussed in this workshop. If something is missing, please open a GitHub issue and I'll add it!

In some cases, a term may have multiple meanings. I'll do my best to encompass the breadth of a term's meaning within the comtext of DevOps, but when in doubt, assume that it has a particular meaning specific to this workshop.


**Artifact**

Any new object produced as a result of software development. This could mean a compiled binary, the project's source code, container images, or project dependencies.

**Binary**

The file that results from compiling your code, if written in a language that is compiled rather than interpreted.

**Binary Repository Manager**

A tool that allows you to organize your compiled binaries into repositories the same way you organize your source code into repositories, e.g., JFrog Artifactory

**Build**

As a verb, to compile your source code into an executable binary. As a noun, a version of your application as an executable binary.

**CI/CD**

The combination of Continuous Integration and either Continuous Deployment or Continuous Delivery. Broadly, this is the term for a set of tools and behaviors that allow you to automate everything that occurs between committing code and either delivering or deploying your application, including building, testing, vulnerability scanning, and promotion from development to production.

**Compiler**

A tool that translates an entire application written in one higher-level programming language into another lower-level language so that it can be executed. Examples of compiled languages are C, C++, and Go.

**Container**

A virtualized operating system environment that includes your application and its dependencies, allowing you to have a greater level of confidence that it will run no matter where it's deployed.

**Continuous Delivery**

A philosophy that your software updates should be continuously delivered to the target, although deployment to the user is still triggered manually, allowing you to deploy quickly and often. Quality gates like testing are performed automatically. Continuous Delivery requires Continuous Integration.

**Continuous Deployment**

Like Continuous Delivery, a philosophy that your software updates should be continuously delivered to the target. However, Continuous Deployment goes one step further and says that your updates should be automatically deployed without human interference as well. Also requires Continuous Integration.

**Continuous Integration**

Enabled by a Continuous Integration tool like JFrog Pipelines, merging all developers’ working codebase with the source, multiple times a day. Doing this requires a series of automated build and unit tests to ensure none of the proposed changes cause problems, but the result is that bugs and integration issues are discovered much earlier in the development process. Ideally, a build is triggered with every single commit, so that failures are caught by the developer immediately and corrected.

**CVE**

Common Vulnerabilities and Exposures, a dictionary of publicly-disclosed cybersecurity vulnerabilities. Each vulnerability may also be referred to as a CVE. An example is CVE-2017-5638, the vulnerability in Apache Struts that was exploited to allow the Equifax breach to occur.

**CVSS**

Common Vulnerability Scoring System. A numerical score on a scale from 1 to 10, representing the potential severity of a software vulnerability.

**Dependency**

Code, librarties, or tools that your application relies on to operate. May or may not be writtem by a third party.

**DevOps**

DevOps is the term for the union of the development team and the IT operations team, through the use of a specific set of practices and toolchains. Rather than having the development and operations team handle their own specific responsibilities independently of one another, the two teams should work together. This is both a cultural change and a technology change, with the ultimate goal of drastically shortening the amount of time it takes the team to deliver software. The result is more frequent software deployments, deploying bad updates less frequently, and being able to recover from bad updates faster. CI/CD is a core concept of DevOps.

**DevSecOps**

Like DevOps, but Security is made a concern earlier in the software development lifecycle. Vulnerability scanning tools like JFrog Xray are baked into the CI/CD pipeline, allowing you to automate failing a build if a critical vulnerability is found.

**Docker**

A virtualization tool that allows you to deliver your software in a particular type of package called a container, which includes an operating system.

**Helm**

A package manager for Kubernetes. Written in YAML, a Helm chart allows you to define, install, and upgrade complex Kubernetes applications. 

**Infrastructure As Code**

A tool that allows you to manage and provision infrastructure such as containers and network configuration through your code, in a way that can be versioned just like your code, rather than handling your infrastructure separately through an interactive tool or dashboard. Examples are Pulumi, Ansible, Terraforrm, and AWS Cloudformation.

**Integration Tests**

A type of testing that verifies entire parts of an application work when combined with other parts of an application.

**Interpreter**

A tool that translates source code in a higher-level language into a lower-level language for execution, line-by-line, at runtime. JavaScript, Lisp, and Ruby are examples of interpreted languages. Technically, Python is compiled to bytecode before being interpreted by CPython.

**Kubernetes**

A container orchestration tool designed to make the deployment and management of containerized applications easier. Think of it like the thing that helps you define which shipping containers go where on a barge. 

**License**

A legal document that defines how a piece of software may be used, and what the implications are for using it. Licenses may define rules around contributing code, monetization for projects that rely on it, and more.

**Local Repository**

In the context of JFrog Artifactory, a particular type of repository that contains code originating on your local machine. Does not include code from dependencies or third-party sources.

**Microservice**

A software development architecture that breaks your application up into multiple independent services that interact with one another. Each service performs a specific task, and may have its own resources such as a database.

**Monolith**

A software development architecture wherein your application is built as a single unit -- front-end, back-end, and database. Until fairly recently, this is how all software was written. 

**Remote Repository**

In the context of JFrog Artifactory, a repository type that contains only remote code with an original source outside of your local machine, e.g., your project's dependencies.

**Repository**

A place to organize your source code or artifacts into one cohesive, organized group by application or project. Tools like GitHub are for organizing your source code into repositories, and Artifactory is for organizing your build artifacts into repositories.

**Service Mesh**

A tool that makes it easier to monitor and control the flow of information between the microservices that make up your application. This is part of your infrastructure.

**SDLC**

Often-used shorthand for Software Development Lifecycle, which is the processes and tools involved in writing and delivering software.

**Source Control**

A tool that helps manage your uncompiled source code into repositories. Examples are GitHub or Bitbucket.

**Unit Tests**

A type of test that aims to verify functionality within a very specific, narrow scope, e.g., a specific function or class.

**Virtual Repository**

In the context of JFrog Artifactory, a type of repository that acts as an envelope around the local and remote repositories that make up your complete application.

**YAML**

A data serialization language designed to be human-readable, frequently used for configuration files in DevOps and beyond.