# Sprint Review - Sprint 6: Private Taskcluster deployments, September 28 - October 23, 2020

**Product Owner**: [Coop](https://github.com/ccooper)
**Scrum Master**: [Coop](https://github.com/ccooper)

## Goal
The primary focus for this sprint was to take advantage of the recent decision by a non-Mozilla third-party, [Well Played Games](https://wellplayed.games/) to deploy Taskcluster. By analyzing their feedback, we chose a selection of epics that would help both Mozilla and Well Played Games manage their deployments more effectively.

Unlike Mozilla, most Taskcluster adopters will *NOT* want their deployments and artifacts to be accessible to the world. Adding in the necessary default scopes and signing to enable private deployments will encourage adoption while also assisting some Mozilla use cases, e.g. signing. In order to better promote Taskcluster, we took an epic to create a new landing page for Taskcluster. This landing page would be separate from the docs site which is where we historically pointed potential adopters.

Finally, because worker imaging is an ongoing problem, we took an unrelated epics to improve the bootstrapping for kernel images for docker-workers on Linux.

### Epics
1. [Allow signing public S3 artifacts](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/19)
2. [Require scopes for all API calls](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/27)
3. [Create new landing page for taskcluster.net](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/30)
4. [Automate building of kernel packages for docker-worker images](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/21)

## Outcomes
We had mixed results with this sprint.

We achieved two of the epics rather quickly. [@djmitche](https://github.com/djmitche) got the initial [taskcluster.net](https://taskcluster.net/) page setup before the sprint even started, and then [@helfi92](https://github.com/helfi92) was quickly able to perform some tweaks and incorporate the feedback from Well Played Games. Of course, the biggest and most pleasant surprise was that [@ricky26](https://github.com/ricky26) did the lion's share of the work for implementing signed public artifacts. The team is very appreciative of the help.

Both anonymous scopes and the kernel packages work dragged into the original slush week and needed to be handed off to others due to vacation and external requests. [@ccooper](https://github.com/ccooper) as scrum master made the decision to extend the sprint by a week to provide extra time to finish the outstanding epics.

However, because the people who picked up the epics had less context, and because the original epics owners were required for satisfactory review, both epics dragged past the extra week into the new slush week before being wrapped up.

## Feedback
The majority of the feedback we received for this sprint centered around the two epics that went off the rails. Before we dig into those problems, it's worth noting that there has been lots of good buzz already about the new [taskcluster.net landing page](https://taskcluster.net/) from upper management at Mozilla. It will be interesting to see if we can parlay this into more external interest in the coming months.

### Require scopes for all API calls
The key sticking point for this epics was that we needed to come to agreement on the implementation of [RFC#165](https://github.com/taskcluster/taskcluster-rfcs/blob/main/rfcs/0165-Anonymous-scopes.md). This always takes time, and the amount of time varies widely. This is why we generally try to keep all but decided RFCs out of the scope for sprints.

The other factor that slowed us down here was that neither [@petemoore](https://github.com/petemoore) nor [@helfi92](https://github.com/helfi92) had much experience with the the code being changed. This resulted in a pattern of experimenting with changes, fixing tests, and then sometimes backtracking based on new understanding. The team agreed that both the auth and lib-api code is old -- some of the oldest in Taskcluster -- and has been left intentionally untouched to avoid breaking it. The team agreed that we would need to address the lack of shared understanding about these two areas of code in the near future.

### Kernel packages for docker-worker images 
This particular epic languished for different reasons.

First, [@djmitche](https://github.com/djmitche) handed this epic off to [@imbstack](https://github.com/imbstack) when he needed to deliver on a timely external request from our director.

Worker imaging is also hard to test, and few (if any) automated tests exist yet. In fact, this kernel package work is a prerequisite for a future worker imaging pipeline sprint where we hope to create some of those automated checks and tests.

We also weren't sure what exactly we were solving for at the outset, which made it hard to chart the correct path. Initially we thought we needed to create solutions for both AWS and GCP, and that historical kernel modifications would need to be perpetuated in both. Through discussion, and also through a little trial-and-error, we determined that rebuilding the kernels was not actually required. We also decided *not* to build images for AWS, focusing instead on the community- and third-party deployment cases instead which are centered around GCP. The team felt that trying to bootstrap a process for AWS where we have a known horizon was a waste of effort. When the existing Firefox workloads move from AWS to GCP, we can present Release Operations with our existing process in GCP and assist them as necessary in modifying it to support Firefox imaging.

For now, we will document the imaging process as it exists in AWS. If re-imaging *is* required in AWS, we will take the pragmatic approach of updating an existing AMI in place and snapshotting it. 