# Taskcluster Agile Process Tracking

This repo contains documentation and issues related to how the Taskcluster team at Mozilla runs its agile development process.

Table of Contents
=================

   * [Taskcluster Agile Process Tracking](#taskcluster-agile-process-tracking)
      * [Definitions](#definitions)
         * [Theme](#theme)
         * [Initiative](#initiative)
            * [Current Initiatives](#current-initiatives)
         * [Milestone](#milestone)
         * [Epic](#epic)
         * [Issue](#issue)
         * [An Example](#an-example)
      * [Tools](#tools)
      * [Roles](#roles)
         * [1. Product owner](#1-product-owner)
         * [2. Scrum master](#2-scrum-master)
         * [3. Future sprint champion](#3-future-sprint-champion)
      * [Sprint process](#sprint-process)
         * [Choosing the next sprint](#choosing-the-next-sprint)
         * [Workspace configuration](#workspace-configuration)
         * [Starting the sprint](#starting-the-sprint)
         * [During the sprint](#during-the-sprint)
         * [Ending the sprint](#ending-the-sprint)
         * [Time between sprints](#time-between-sprints)

______

## Definitions

In order to avoid confusion when discussing our process, it's helpful to define the various terms we use to categorize our work at different levels of granularity and how they roll up into each other.

We generally follow [the Atlassian model](https://www.atlassian.com/agile/project-management/epics-stories-themes), with some naming changes to avoid confusion in [our tooling](#Tools).

Theme -> Initiative -> Milestone -> Epic -> Issue

### Theme
Themes are large focus areas than span the Mozilla organization and are pertinent and addressable by the Taskcluster team.

For Taskcluster @ Mozilla, we are currently tracking the following themes:
* Make data actionable
* Promote external adoption
* Improve ease of use
* Support cost reduction

### Initiative
An _initiative_ is a collection of one or more milestones that, taken together, address one or more themes. Initiatives map to major projects that the Taskcluster team would like to accomplish, and can be either new functionality or substantial reworks of existing functionality. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.

#### Current Initiatives
* [Switch the Taskcluster datastore from Azure to Postgres](https://github.com/orgs/taskcluster/projects/6)
* [Use worker-runner everywhere](https://bugzilla.mozilla.org/show_bug.cgi?id=1602946)
* [Streamline service deployment configuration](https://github.com/taskcluster/taskcluster/projects/8)
* [Implement the Object Service](https://bugzilla.mozilla.org/show_bug.cgi?id=1471582)
* [Implement projectId](https://bugzilla.mozilla.org/show_bug.cgi?id=1607487)
* [Implement taskQueueId](https://github.com/taskcluster/taskcluster-rfcs/pull/145)
* [Implement the Github Checks API](https://bugzilla.mozilla.org/show_bug.cgi?id=1459645)
* [Use SOPS instead of password-store](https://bugzilla.mozilla.org/show_bug.cgi?id=1483320)
* [Artifact Integrity](https://docs.google.com/document/d/14miyPpGnpiyvFb93-doV7ENcKjwSdZYUV1VplPEcRqU/edit#heading=h.jgvxmoleismy)
* [Structured Logging for Workers](https://bugzilla.mozilla.org/show_bug.cgi?id=1529660)
* [More secure, well-documented process for interactive tasks](https://github.com/taskcluster/taskcluster-rfcs/issues/41)
* [Decommission docker-worker](https://bugzilla.mozilla.org/show_bug.cgi?id=1499055)
* Automatically land config changes to community-tc
* Move frequently-updated complex configuration out of the deployment config and into the API
* Help users construct taskcluster.yml
* Better worker capacity estimates

### Milestone
The _milestone_ is the goal for a sprint and, as such, should be able to be completed during the sprint duration. A milestone is made up of a small collection of epics. This can be a thin wrapper around a single epic if the user story is large and/or important enough. Milestones can address one or more themes.

### Epic
An _epic_ a large user story that describes plainly a feature of the Taskcluster system. Epics can address multiple themes. User stories are an important aspect of agile development, but we've chosen to map them to Epics in our usage to make them trackable at the correct level using [our tooling](#Tools).

### Issue
An _issue_ is a single, cohesive task as represented by a Github issue. Larger issues should be decomposed into smaller issues. No single issue should take more than 1 engineer week to accomplish, modulo time to review and deploy. Issues should address a single epic.

A well-defined issue is the basis for all of our estimation. It cannot be overstated how important it is to make sure issues are decomposed to the point where they can be estimated accurately. It underpins _everything_ else.

### An Example

Here is a top-down categorization example from an actual sprint:

* Theme: Make data actionable
* Initiative: Switch the Taskcluster datastore from Azure to Postgres
* Milestone: Migrate database tables from tc-lib-entities format to proper relational tables (aka postgres phase 2)
* Epic: [Create and update tools to facilitate work with new db format](https://github.com/taskcluster/scrum/issues/3)
* Issue: [Add support for data signing](https://github.com/taskcluster/taskcluster/issues/3082)

Note: the above decomposition from theme to issue is represented in its simplest form, but it could certainly be more complex. For example, the _Initiative_ to "Switch the Taskcluster datastore from Azure to Postgres" might also serve the theme of "Cost reduction" depending on how the new data is used, and would "Promote external adoption" as well by simplifying the setup requirements for Taskcluster.

## Tools
All Taskcluster work for sprints is tracked via issues in Github.

Sometimes bugs from [Bugzilla](https://bugzilla.mozilla.org) will be part of our sprint. When this happens we will create a corresponding issue or Epic in Github and reference the original bug.

We are using [Zenhub](https://www.zenhub.com/) to manage our agile process. Zenhub layers much-needed functionality on top of Github, namely:
* dependency tracking
* estimate tracking
* milestones for tracking sprint objectives
* burndown charts

Any issues that are purely process-based (e.g. scrum documentaion) should be filed in [the scrum repo](https://github.com/taskcluster/scrum). Epics are represented in Zenhub as [specially-tagged issues](https://app.zenhub.com/workspaces/taskcluster-5ed15d37c2d9744af28567dc/board?epics:settings=epicsOnly&repos=269405817). Since they are a process abstraction to link issues together, Epic issues should be filed in the scrum repo as well.

## Roles
We have three defined roles in our agile process:
### 1. Product owner
The _Product owner_ manages the product backlog and keeps the rest of the team working on the most important thing. They have the final decision on matters of scope. They can also change the scope of the current milestone or, at their discretion, end the sprint early.

### 2. Scrum master
The _Scrum master_ deals with the scrum process itself. They run the kick-off meetings, the daily stand-ups, and the wrap-up meetings (review & retrospective) for every sprint. They prompt developers for status and follow-up when developers are blocked. They support the Product owner in whatever way the Product owner deems necessary. The _Scrum master_ also works with _Future sprint champions_ to ensure high quality, well-scoped milestones for future sprints.

### 3. Future sprint champion
The _Future sprint champion_ is responsible for organizing issues in the Product Backlog into a cohesive milestone that the team can work towards in a future sprint. They are expected to devote a few hours every week to triaging issues in the backlog to refine the scope for the future sprint. Note: there can be multiple _Future sprint champions_ active at one time.

## Sprint process

### Choosing the next sprint
During the previous sprint, one or more Future sprint champions do the work organize the work around new milestones. User stories are discussed and converted into Epics. New issues are filed or existing issues are tagged against the upcoming milestone. Estimates are made on each issue, often through consultation with other team members. Care should be taken to avoid adding too much work to a given milestone, and the issue estimates are a good tool to gauge how conservative to be.

As we near the end of the current sprint, the milestone for the next sprint is often obvious based on organizational needs or follow-on work that builds on the current sprint. If there are multiple milestones possible, they should all be added to the roadmap. This helps keep customers and external parties informed.

If multiple future sprints are ready and there are no other factors to aid decision, the _Scrum master_ will decide.

### Workspace configuration
We have the following pipelines (columns) configured in Zenhub:
* **Icebox**: issues we will never work on. These may be valid, but are not a priority given finite time and resources.
* **New Issues**: newly-filed issues. They will remain here until triaged and labelled to go into either the Product Backlog, Next Sprint, Current Sprint Backlog, In Progress, or Icebox pipeline.
* **Product Backlog**: triaged issues that are not part of the current sprint or an upcoming sprint.
* **Next Sprint**: issues that have been labelled and are being groomed for an upcoming sprint. Note: all upcoming sprints (there can be several being planned in parallel) share this pipeline.
* **Current Sprint Backlog**: issues that are part of the current sprint that are not being worked on yet.
* **In Progress**: issues that are being worked on.
* **Done**: White shores, and beyond, a far green country under a swift sunrise.

### Starting the sprint
At the start of the sprint, the _Scrum master_ will update the [primary Zenhub workspace](https://app.zenhub.com/workspaces/taskcluster-5ed15d37c2d9744af28567dc/board) to mark the current milestone as active and moved the issues associated with that milestone into the Current Sprint Backlog pipeline. The _Product owner_ and _Scrum master_ will decide how and when they want to meet to review sprint progress, possibly leveraging an existing 1x1 if one exists.

We will hold a kick-off meeting where the _Product owner_ will provide context enough for people to get started and assist developers in choosing their first issue to work on. The _Scrum master_ will remind everyone of any process changes being adopted for the new sprint. Work begins.

### During the sprint
The team will hold daily stand-up meetings for the duration of the sprint. Our daily stand-ups take place in Slack at 8am PT (11am ET/5pm CEST), except on Tuesdays when we present our stand-up status as the first agenda item of our weekly team meeting. Whether delivered in person on via Slack, the format of the update is the same:
* DONE: work that has been completed
* TODO: work that is coming up next
* BLOCKERS: what is preventing you from getting the work done
* INTERRUPTS: what is delaying you from getting the work done

The _Product owner_ is paying attention to these updates to make sure that the most important things are being worked on and are being picked up next.

The _Scrum master_ is paying attention to these updates to make sure that blockers are highlighted and interrupts are kept to a minimum.

Once a week, the _Product owner_ and the _Scrum master_ will meet to assess sprint progress. Using the burndown chart, they figure out whether the sprint is still on track and can be completed within the allotted time. If necessary, the critical path can be refined to allow partial delivery of the original objective. Under extraordinary circumstances, they can opt to end the current sprint.

### Ending the sprint
As the sprint draws to a close the _Scrum master_ with schedule two meetings for a Review and a Retrospective. These meetings are usually scheduled back-to-back for convenience.

In the Review meeting, the _Product owner_ will lead the discussion. The focus will we be on the content of the sprint and the outcomes achieved. Feedback on the sprint content will also be collected. At the end of the Review meeting, the team will triage any outstanding issues from the sprint. The _Product owner_ will engage with developers who still have work marked as **In Progress** to figure out how and when to wrap-up that work during the _Time between sprints_.  All issues that have not been started will be moved back into the **Product Backlog**.

In the Retrospective meeting, the _Scrum master_ will lead the discussion. The focus will be on the sprint process itself in an attempt to uncover grey areas and process improvements. If the team agrees to adopt a particular process change, it should be clearly marked in the meeting notes with an **ACTION** label and the person responsible for that action, if appropriate.

Notes for both meetings should be taken using the templates provided:

* sprints/
  * templates/
    * [sprint-retrospective.md](./sprints/templates/sprint-retrospective.md)
    * [sprint-review.md](./sprints/templates/sprint-review.md)

As process changes are adopted, this document should be updated to reflect the new process.

### Time between sprints
We allow ourselves *one week* between sprints. This buffer allows us to analyze the previous sprint without the pressure of immediately jumping into something new. Pragmatically speaking, it also gives us the time to finish off sprint items that may still require deployment, to address unanticipated fallout from the previous sprint, and to deal with the backlog of small, timely requests that may have accumulated during the sprint.
