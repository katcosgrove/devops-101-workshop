# Xray Module


This module will walk you through Xray. We will cover software vulnerabilities and license compliance, go through setup, manually trigger a scan, and learn to read the results.

## Overview


Xray is a tool that protects you from security problems in your software. It looks at your dependencies and compares them against known issues in the NVD (National Vulnerability Database), and optionally against Risk Based Security's VulnDB if you have the Xray Premium plan. Not all vulnerabilities are critical and require immediate attention though, so Xray presents you with the CVSS score (on a scale from 1 to 10) for each vulnerability, as well as the severity (Low, Medium, High). If a version of that particular dependency exists with a fix for the vulnerability Xray found, it will tell you that as well, so you can go update your dependency immediately.

With the Xray Premium, if you're working with a lot of open source tools at work, or you're working in a particularly large open source project in your spare time, you also need to care about license compliance. Xray can keep track of that for you, too, so you don't accidentally add a dependency licensed in a way that conflicts with the rest of your project, thereby avoiding legal problems. This is not included in the free tier.

Xray functions on a system of Policies and Watches. Policies allow us to define security and license compliance behaviors. Once they are defined, they are enforced by applying them to Watches. A Watch is a collection of repositories, builds, and release bundles that Xray should look at. Based on the results of the scan, you can automate certain actions. It can automatically fail a build if a vulnerability that exceeds your comfort level is found, or it can call an external API, or it can just email someone for you. This is something that's really important for businesses or open sources tools that are heavily relied-on to have. It's less important for your personal projects, but still useful (and kinda fun). Anyway, it's included in the free tier of JFrog products, so you may as well use it.


## Setup and Usage


1. Index Resources
    - Navigate to the Administration Module by clicking the gear icon in the left-hand navigation panel. Click on the Xray Security & Compliance menu, and then Indexed Resources.

    - Click Add a Repository, select all of the repositories you want Xray to be able to scan (in this case, docker-local and docker-remote), then save. 

Xray only scans what you explicitly tell it to, so remember that if you add more repositories, you need to come back here to tell Xray to scan them. The scan is labor-intensive, so it's best to index only the repositories you actually need to watch, rather than indexing absolutely everything.

2. Define a Security Policy
    - Navigate to the Application module, expand the Security & Compliance menu and click the Policies menu item.
    - Create a new policy called “docker-security”, of type Security.
    - Add a Rule. Name it "medium-security" and select Medium from the Minimal Severeity dropdown. From here, you can also make some other things happen automatically -- fail the build, block downloads, call an external API, send an email, etc. 

3. Define a Watch
    - Navigate to the Application module, expand the Security & Compliance menu and click the Watches menu item.
    - Create a new watch called “sample-watch”, with your two repositories (“docker-local” and “docker-remote”) and your “docker-security” policy assigned to it by clicking Manage Policies.

4. Run a Scan
    - Hover over your Watch and click "Apply on Existing Content" to manually trigger it. 
    - Note that the scan may take some time to complete; it depends on a few variables, but the size of the repository matters. You can return here later and view your results by clicking on the Watch, but Xray data will also start to show up in a few other places within the platform.

5. Look Around
    - From the Application module, expand the Artifactory menu and click Artifacts. In the file tree, expand your docker-local repository until you see "manifest.json" and click that file. In the pane that opens up, you will be able to see your vulnerability data. Depending on your screen size, you may need to click a menu arrow to see the Xray option. 
    - Click the name of a vulnerability under the Security tab to get more specific information about a particular problem. A pop-up will display with an Impact Analysis Graph to show you exactly which component of your application has a problem, as well as a description of the CVE and the fix version if one is available.

6. Run a Report
    - From the Application module, expand the Security & Compliance menu and click Reports.
    - Create a new report named "sample-report." In the free tier of the JFrog platform, you will only be able to select a report type of Vulnerabilities. Set the scope to Repositories, and select your two Docker repositories.
    - Additional filtering options will become available, like searching for a specific CVE. Filter by a severity of Medium, and click Create Report.
    - Once it's finished, click the report again to view the results.