# Sprint retrospective - Support worker re-registration

## What worked
* Having a dedicated product owner
  * @imbstack provided extra guidance on scope and helped us narrow the critical path when that became necessary.
* Encrypted column support
  * This would have been a blocker for a future postgres phase 2 sprint, but we got it done in the context of this sprint.
* Issues
  * Aligning on issues in github as the sole source of truth made it easier to track progress and find the next thing to work on.
  * Kudos to @imbstack for putting in the effort to flesh out all the issues as much as he did and highlighting the dependencies as best he could in github.
* Estimate tracking
  * Our label-based method was a good start.

## What didn't
* Stories vs Epics vs Issues
  * Lack of clarity around terminology and how things break down from one level to the next
  * Very clear technical tasks are the basis for good estimates == Issues
  * User stories should be the basis for "did we finish the thing?" or not
  * Unsure yet how to indicate this effectively in current tooling
* Delivering what we promise
  * aka Following through on what we decide goes into each sprint
  * We are starving requests from other teams while in a particular sprint, so we'd better deliver what we intend.
  * Do we need recurring or interstitial sprints to deal with requests and backlog?
    * Bustage/requests need to be factored into every sprint.
    * We should plan on scheduling a sprint every 4 cycles or so (i.e once a quarter) to address backlogged requests if not covered by other sprints.
* Scope and the critical path
  * Our initial sprint goals were too broad and lacked a well-defined user story that we could use to measure delivery.
    * In fact, it would have been impossible to determine the critical path with the initial goals.
  * By not determining the real sprint goal until halfway through the sprint, we performed more work that wasn't on the critical path or didn't fit in this particular sprint at all.
* Dependency tracking
  * Github doesn't do dependency tracking, but we hacked around it as best we could using labels and comments.

## Other notes/Unresolved issues

* Can we run multiple sprints simultaneously?
  * e.g. 2 people on one sprint, 3 people on another
  * Serial vs parallel
* Should we have themes for future sprints?
  * Papercuts, possibly linked by theme
  * One big epic, plus some other fixes in same area
* We should document current best practices in the scrum repo
  * terminology
  * How to minimize conflicts as we all work in the same areas
  * Rebasing
    * Testing is particularly prone to collisions

## Process changes for next sprint

* [Zenhub](https://www.zenhub.com/) as sprint tracking tool
  * layers many of the features we're missing on top of github, chief among them:
    * dependency tracking
    * estimate tracking with burndown charts
    * milestones that can be scheduled to assist with planning future sprints
  * We will adopt the terminology of Zenhub re: milestones and epics to minimize confusion.
    * We will document this and other process decisions in the scrum repo.
* Critical path analysis
  * Prior to the kickoff of the next sprint, the product owner and the scrum master will meet to determine what *must* get done.
    * Dependency tracking in Zenhub will also help with this.
  * We will reconvene every week to assess the remaining work and prioritize appropriately.
  * More upfront planning will save us some pain later.
