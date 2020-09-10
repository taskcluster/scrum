# Sprint retrospective - Provisioning is efficient, August 4 - August 11, 2020

## What worked
* Different buckets of work that people could move between
  * The sprint was more open-ended and allowed for more creativity.
  * Team members appreciated this after the more mechanical effort in the [previous sprint](../20200622-postgres-phase2/)
* Issues were at the correct level of decomposition
* Similar issues for people who were just learning the subject area
  * Having different team members working on separate cloud providers made it easy to collaborate and come up with a holistic approach quickly.
* Scaling ratios are a useful lever to have again
  * [Miles'](https://github.com/milescrabill) work on scaling ratios was called out as a particularly big win for provisioning.
* Ending the sprint early
  * Brian made the decision as Product Owner to cancel the sprint after the layoffs were announced. This was absolutely the correct thing to do. No one could focus anyway.

## What didn't
* Still ended up with one major thrust of the sprint being blocked on one big chunk of work from one person
  * Specifically the work to refactor worker-manager to support the new mode of work was not completed
* Working with Zenhub is mind-numbing
  * Despite still being considered a net win, the process of managing and running a sprint still involves a lot of mechanical actions -- moving issues, labeling tasks -- that are not preferred activities.

## Process changes for next sprint
* Be explicit about actions that are required to enact process changes.
  * **ACTION**: Coop to update the main process docs to ensure that all process changes have an associated **ACTION**.
* Try hard to actually have independent chunks of work
  * If there is one "big chunk" of work, it should be an epic in its own right. If a piece of work is foundational, it should be the focus of the sprint rather than a piece.
  * **ACTION**: Promote large work items to epics and decompose further.
* Identify issues that are likely to require decomposition and assign them more story points at the outset
  * The burndown chart hasn’t been very realistic. We continue adding story points after start of sprint
  * **ACTION**: Be conservative when assigning story points, i.e. if in doubt, round up to the next Fibonacci number.
* Perform sprint planning out-of-band and *then* transfer data to Zenhub
  * We should be planning sprints around existing epics, rather that creating epics on-the-fly to encompass a batch of existing issues. This implies more forethought has gone into the planning and organization of the sprint, and should lead to better outcomes.
  * **ACTION**: Future Sprint Owners should loop in the Scrum Master and any other domain experts when planning the sprint. A 30 minute meeting may result in a much better-planned sprint.
* Move from Zenhub to Jira?
  * Now that the team is under the IT umbrella at Mozilla, there may be a need to align on Jira for agile process tracking because that's the tool of choice in the new org. There hasn't been a request yet, but we are aware this might happen.
  * **ACTION**: Coop to follow-up with IT leadership to determine the expectation here.
