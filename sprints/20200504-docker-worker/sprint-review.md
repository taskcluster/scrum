# docker-worker sprint review

While the Taskcluster team has attempted to implement some agile methodologies before, this was our first stab at a formal scrum.

We didn't have a lot of time to prepare -- the status of Wander's contract renewal was uncertain until late April -- but we decided that the hand-off of docker-worker maintenance responsibilities from Wander was a significantly high priority need for Mozilla that it warranted pulling the team off of other projects to focus on docker-worker. As their manager, I hoped that this would help breakdown some of the longstanding barriers between the various silos of work and encourage a sense of shared ownership of the *entire* codebase.

For this first sprint, we had a naturally emposed duration. Wander's contract was up on May 22, so that gave us slightly less than 3 weeks with which to work. We chose a set of four goals for the first sprint, some of which were already in progress:
1. Migrate off packet.net onto AWS bare metal instances (in progress)
2. Migrate docker-worker into the monorepo
3. Redeploy all docker-worker workers
4. Migrate docker-worker workloads to generic-worker

We quickly setup a [github project board](https://github.com/taskcluster/taskcluster/projects/9), and added many existing docker-worker bugs. We also created new cards for the obvious missing elements needed to tackle our goals.

As it turned out, we were overly-ambitious with our first sprint. ;)

We managed to accomplish goals #1 and #2, and made some progress towards #3, but decided to drop #4 as out of scope after some initial investigation. We quickly realized that in order to redeploy all docker-worker deployments (#3), we needed a much better story around CI testing docker-worker in staging. This entailed a lot of work to get integration tests running and debugged once docker-worker was migrated into the monorepo. There was also a fair amount of work required on monopacker, the tool we hope to use to generate images going forward.

By the very end of the sprint, we were able to deploy docker-worker successfully to staging using monopacker-generated images, but it's a big step from there to deploying a version of docker-worker to production.
