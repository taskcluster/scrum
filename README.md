# Taskcluster Agile Process Tracking

## Definitions

In order to avoid confusion when discussing our process, it's helpful to define the various terms we use to categorize our work at different levels of granularity and how they roll up into each other.

We generally follow [the Atlassian model](https://www.atlassian.com/agile/project-management/epics-stories-themes), with some naming changes to avoid confusion in [our tooling](#Tools).

Theme -> Initiative -> Milestone -> Epic -> Issue

### Theme
Themes are large focus areas than span the Mozilla organization and are pertinent and addressable by the Taskcluster team.

For Taskcluster @ Mozilla, we are currently tracking the following themes:
* Making Data Actionable
* Ease of use
* Promote external adoption
* Cost Reduction

### Initiative
An initiative is a collection of one or more milestones that, taken together, address one or more themes. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.

### Milestone
The *milestone* is the goal for a sprint, and as such should be able to be completed during the sprint duration made up of a small collection of epics. This can be a thin wrapper around a single epic if the user story is large and/or important enough. Milestones can address one or more themes.

### Epic
An *epic* a large user story that describes plainly a feature of the taskcluster system. Epics can address multiple themes. User stories are an important aspect of agile development, but we've chosen to map them to Epics in our usage to make them trackable at the correct level using [our tooling](#Tools).

### Issue
An *issue* is a single, cohesive task as represented by a Guthub issue. Larger issues should be decomposed into smaller issues. No single issue should taken more than 1 engineer week to accomplish, modulo time to review and deploy. Issues should address a single theme.

## Tools
All Taskcluster work for sprints is tracked via issues in Github.

Sometimes bugs from [Bugzilla](https://bugzilla.mozilla.org) will be part of our sprint. When this happens we will create a corresponding issue or Epic in Github and reference the original bug.

We are using [Zenhub](https://www.zenhub.com/) to manage our agile process. Zenhub layers much-needed functionality on top of Github, namely:
* dependency tracking
* estimate tracking
* milestones for tracking sprint objectives
* burndown charts

## Roles
We have three defined roles in our agile process:
### 1. Product owner
The _Product owner_ manages the product backlog and keeps the rest of the team working on the most important thing. They have the final decision on matters of scope.At their discretion, they can also change the scope of the current milestone or end the sprint early.

### 2. Scrum master
The _Scrum master_ deals with the scrum process itself. They run the kick-off meetings, the daily stand-ups, and the wrap-up meetings (review & retrospective) for every sprint. They prompt developers for status and follow-up when developers are blocked. They support the Product owner in whatever way the Product owner deems necessary. The _Scrum master_ also works with Future sprint champions to ensure high quality, well-scoped milestones for future sprints.

### 3. Future sprint champion
The _Future sprint champion_ is responsible for organizing issues in the Product Backlog into a cohesive milestone that the team can work towards in a future sprint. They are expected to devote a few hours every week triaging issues in the back to refine the scope for the future sprint. Note: there can be multiple _Future sprint champions_ active at one time.

## Sprint process

### Choosing the next sprint

### Starting the sprint

### During the sprint

### Ending the sprint
