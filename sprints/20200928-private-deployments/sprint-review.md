# Sprint Review - Sprint 6: Private Taskcluster deployments, September 28 - October 23, 2020

**Product Owner**: [Coop](https://github.com/ccooper)
**Scrum Master**: [Coop](https://github.com/ccooper)

## Goal
The primary focus for this sprint was to take advantage of the recent decision by a non-Mozilla third-party, [Well Played Games](https://wellplayed.games/) to deploy Taskcluster. By analyzing their feedback, we chose a selection of epics that would help both Mozilla and Well Played Games work managed their deployments more effectively. Unlike Mozilla, most Taskcluster adopters will *NOT* want their deployments and artifacts to be accessible to the world. Adding in the necessary default scopes and signing to enable private deployments will encourage adoption while assisting some Mozilla use cases, e.g. signing. In order to better promote Taskcluster, we also took an epic to create a new landing page for taskcluster that would be separate from the docs site which is where we historically pointed potential adopters.

Finally, because worker imaging is an ongoing problem, we took an unrelated epics to improve the bootstrapping for kernel images of docker-workers on Linux.

### Epics
1. [Allow signing public S3 artifacts](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/19)
2. [Require scopes for all API calls](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/27)
3. [Create new landing page for taskcluster.net](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/30)
4. [Automate building of kernel packages for docker-worker images](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/21)

## Outcomes

## Feedback
