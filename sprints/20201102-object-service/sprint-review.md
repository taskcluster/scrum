# Sprint Review - Object Service / Careers Site, November 2, 2020 - December 4, 2020

**Product Owners**
* Object Service: [@djmitche](https://github.com/djmitche)
* Careers Site: [@ccooper](https://github.com/ccooper)
* High-priority Fixes: [@ccooper](https://github.com/ccooper)

**Scrum Master**: [@ccooper](https://github.com/ccooper)

## Goal
Coming out of the [previous sprint](https://github.com/taskcluster/scrum/blob/main/sprints/20200928-private-deployments/sprint-review.md), we knew we had some high-priority issues that couldn't wait for bundling into their own sprint. Work on the Object service had already been postponed repeatedly, so we elected to pursue a reduced-scope MVP for the Object service while simultaneously addressing the high-priority fixes.

### Milestone
* [Sprint 7: Object Service, Careers Site](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/board?milestones=Sprint%207%3A%20Object%20Service%2C%20Careers%20Site%232020-12-04&filterLogic=any&repos=161867312,207857296,199742618,257988948,269405817,210879143,284731663,9521528,294202511)
* [Burndown report](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/reports/burndown?milestoneId=6013788)

### Epics
1. [Object service: Build a minimum viable object service](https://github.com/taskcluster/scrum/issues/32)
2. [Object service: Add a simple download process to the object service](https://github.com/taskcluster/scrum/issues/34)
3. [Object service: Determine required cost/usage reporting for object service](https://github.com/taskcluster/scrum/issues/40)
4. [Object service: Add real storage backends to the object service](https://github.com/taskcluster/scrum/issues/36)
5. [Sprint 7 high-priority fixes](https://github.com/taskcluster/scrum/issues/45)
6. [Address issue backlog for the Careers website](https://github.com/taskcluster/scrum/issues/41)


## Outcomes
Results were mixed, at least within the planned time bounds of the sprint.

While we did end up with an Object service MVP by the scheduled end of the sprint, the work to support a [GCS backend](https://github.com/taskcluster/taskcluster/issues/3718) was delayed well beyond the end of the sprint. GCS is one of the few upcoming use-cases for the Object service that is currently known, so this was disappointing, but also important to get right.

The high-priority fixes were all resolved. Unfortunately the patch to address the [MLS observation queue issue](https://github.com/mozilla/ichnaea/issues/1398) wasn't ready prior to the US Thanksgiving break, and we needed to deploy it afterwards. This delay meant that we weren't able to push the fix to production until after the sprint was over.

The Careers website epic was finished very quickly in early Novemeber. However the monthly deployment schedule for the Careers website meant that the changes weren't live for until early December. We have since addressed the deployment cadence with the Marketing Operations to ensure more timely deployments in the future.

## Feedback
The team felt like the issue decomposition worked well on this iteration.

For the Object service, we successfully constrained our ambition and hit an achievable goal with the MVP. Big projects are hard, and need to be broken down at some level. It was tempting to try to accomplish more, especially given the previous delays with working on the Object service. 20% of a larger goal still a good thing. We are now all anxious to see it to fruition.

Of the high-priority fixes, the [Azure cert issue](https://github.com/taskcluster/taskcluster/issues/3669) fix proved particularly timely as [Azure changed their certs](https://docs.microsoft.com/en-ca/azure/security/fundamentals/tls-certificate-changes) with very little warning in the middle of our sprint.