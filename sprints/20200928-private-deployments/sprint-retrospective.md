# Sprint retrospective - Sprint 6: Private Taskcluster deployments, September 28 - October 23, 2020

## What worked
* Better appreciation for worker space
  * Like the last sprint, this "extra" epic validated that all epics in a sprint don't need to address the same initiative. Both [@djmitche](https://github.com/djmitche) and [@imbstack](https://github.com/imbstack) commented that the rest of the team is slowly gaining confidence in what was once one of our biggest knowledge silos.
* Most of team now has baseline knowledge about auth & lib-api
* An external contributor, [@ricky26](https://github.com/ricky26), delivered one of our epics(!!!)
  * Getting someone else to do your work for you is highly recommended. :)
* Pairing (or tripling) is useful
  * [@helfi92](https://github.com/helfi92), [@jwhitlock](https://github.com/jwhitlock), and [@petemoore](https://github.com/petemoore) found it useful once again to collaborate on an area of the code where none of them were necessarily experts.
* People jumped in to help when the sprint went long.
  * Both [@imbstack](https://github.com/imbstack) and [@helfi92](https://github.com/helfi92) stepped up to inherit epics from others.
* Assigning product owners per epic
  * This effectively spread the oversight across multiple people which was very helpful when all the epics were not tackling the same initiatives.

## What didn't
* Epic decomposition was not fantastic, especially for anonymous scopes.
  * We’ve always struggled to plan work around workers. It's starting to get better as more people get exposure to worker code and issues, but we're still not great at this.
  * We hope that a few more worker-related sprints will make this better.
* Don’t anticipate needs of Firefox CI.
  * Let them come to us; if they need it they will ask.
    * We should let them know they can ask, of course.
  * If we try to do predictive work, the potential for rework is real.
* Auth and lib-api are a black box
  * Should we take this opportunity to (consider) refactor?
    * No, we have work planned for the rest of 2020. We should delay until next year.
* Reviewing RFCs (i.e. big changes) takes a long time
  * Also review by multiple people is required.
  * Cycle time and number of cycles to decide an RFC is generally unknown at the outset, so it's not something we should be trying to accomplish within the framework of a sprint.
    * *HOWEVER*, if someone *is* responsible for writing an RFC, this should be factored in to sprint planning and fewer available story points should be alotted.

## Process changes for next sprint
* Don’t anticipate needs of Firefox CI
  * **ACTION**: plan for Taskcluster and community needs only
* First implementation doesn’t need to make it to production
  * **ACTION**: gauge experience with code area and budget time to learn and make mistakes
  * **ACTION**: Change one service or API at a time
* Structure epics for better parallelism
  * **ACTION**: leverage existing blocking functionality in zenhub
  * **ACTION**: add extra story points for big changes
  * **ACTION**: RFCs should be written outside the sprint process because the amount of time required to review and iterate is hard to predict
* Different epics can have different product owners
  * **ACTION**: assign product owners per epic
* Factor in review time for code areas that are security-sensitive or less well-known
  * **ACTION**: add extra story points to issues that will require in-depth review