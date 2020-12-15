# Taskcluster Agile Process Tracking

This repo contains documentation and issues related to how the Taskcluster team at Mozilla runs its agile development process.

Table of Contents
=================

   * [Taskcluster Agile Process Tracking](#taskcluster-agile-process-tracking)
      * [Definitions](#definitions)
         * [Theme](#theme)
         * [Initiative](#initiative)
         * [Milestone](#milestone)
         * [Epic](#epic)
         * [Issue](#issue)
         * [An Example](#an-example)
      * [Tools](#tools)
      * [Roles](#roles)
         * [1. Product owner](#1-product-owner)
             * [1a. Epic owner](#1a-epic-owner)
         * [2. Scrum master](#2-scrum-master)
         * [3. Future sprint champion](#3-future-sprint-champion)
      * [Sprint process](#sprint-process)
         * [Planning a sprint](#planning-a-sprint)
             * [Estimation](#estimation)
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

A _theme_ is a large focus area than spans the Mozilla organization and is pertinent to and addressable by the Taskcluster team.  Themes are gathered [here](https://github.com/taskcluster/scrum/blob/main/gen/themes.md).

### Initiative

An _initiative_ is a collection of one or more milestones that, taken together, address one or more themes. Initiatives map to major projects that the Taskcluster team would like to accomplish, and can be either new functionality or substantial reworks of existing functionality. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.  Initiatives are gathered [here](https://github.com/taskcluster/scrum/blob/main/gen/initiatives.md).

### Milestone
The _milestone_ is the goal for a sprint and, as such, should be able to be completed during the sprint duration. A milestone is made up of a small collection of epics. This can be a thin wrapper around a single epic if the user story is large and/or important enough. Milestones can address one or more initiatives; all the epics in a given Milestone do not need to service the same initiative.  Milestones are tracked [in ZenHub](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/milestones).

### Epic
An _epic_ a large user story that describes plainly a feature of the Taskcluster system. Epics can address multiple milestones. User stories are an important aspect of agile development, but we've chosen to map them to Epics in our usage to make them trackable at the correct level using [our tooling](#Tools).  Epics are tracked [in ZenHub](https://app.zenhub.com/workspaces/services-engineering-5ed15d37c2d9744af28567dc/board?epics:settings=epicsOnly&repos=161867312,207857296,199742618,257988948,269405817,210879143,284731663,9521528&showPRs=false&showClosed=false)

### Issue
An _issue_ is a single, cohesive task as represented by a Github issue. Larger issues should be decomposed into smaller issues. No single issue should take more than 1 engineer week to accomplish, modulo time to review and deploy. Issues should address a single epic.  Issues are tracked in ZenHub/GitHub.

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

#### 1a. Epic owner
For sprints composed of multiple, unrelated epics, a different _Product owner_ can be assigned per epic. 

### 2. Scrum master
The _Scrum master_ deals with the scrum process itself. They run the kick-off meetings, the daily stand-ups, and the wrap-up meetings (review & retrospective) for every sprint. They prompt developers for status and follow-up when developers are blocked. They support the Product owner in whatever way the Product owner deems necessary. The _Scrum master_ also works with _Future sprint champions_ to ensure high quality, well-scoped milestones for future sprints.

### 3. Future sprint champion
The _Future sprint champion_ is responsible for organizing issues in the Product Backlog into cohesive epics that the team can work towards in a future sprint. They are expected to devote a few hours every week to triaging issues in the backlog to refine the scope for the future sprint. Note: there can be multiple _Future sprint champions_ active at one time.

## Sprint process

### Planning a sprint
During the previous sprint, one or more Future sprint champions do the work organize the issues into epics, and epics into new milestones. User stories are discussed and converted into Epics. New issues are filed or existing issues are tagged against the upcoming milestone.

Zenhub allows setting dependencies between issues. While we need to be careful to avoid having _too many_ dependencies within a given sprint to avoid blocking work, we should leverage dependencies to help reveal the critical path for sprints.

When planning for upcoming sprints, we should focus on the needs of Taskcluster and the community deployment. We can act on specific requests or use cases from the Firefox deployment, but we should not assume anything on their behalf. This will help avoid Mozilla-specific solutions and potential re-work later on.

As much as possible, [RFCs](https://github.com/taskcluster/taskcluster-rfcs) should be written *outside* the sprint process, with only implementation happening within the context of sprints. If the amount of work required for implementation is unclear, estimates should be higher.

#### Estimation
The Taskcluster team uses Fibonacci-scale story points for estimation. Each team member is assumed to be able to deliver on 3-4 story points in a given week. This gives individuals time to deal with interrupts and also to pursue some professional development time. Care should also be taken to plan around upcoming holidays and vacation to avoid over-packing the next sprint.

The first step for sprint estimation is adding up the available story points for all team members over the coming weeks to see what the maximum achievable amount of work is. Combined point estimates for milestones need to fit within that limit to be achievable and realistic.

Story point estimates are made on each issue, often through consultation with other team members. Care should be taken to avoid adding too much work to a given milestone, and the issue estimates are a good tool to gauge how conservative to be.

Some areas of the Taskcluster code are easier to deal with than others. If the issues or epics involve modifying code in a service that is less well-known or difficult to test (e.g. auth), story point estimates should be higher by default to recognize the need for closer inspection on review.

Shorter sprints are preferred, i.e. 1 to 3 weeks. Not all team members need to be involved in every sprint. Avoid the temptation to add "filler" work just so everyone can participate.

### Choosing the next sprint
As we near the end of the current sprint, the milestone for the next sprint is often obvious based on organizational needs or follow-on work that builds on the current sprint. If there are multiple milestones possible, they should all be added to the roadmap. This helps keep customers and external parties informed.

If multiple future sprints are ready and there are no other factors to aid decision, the _Scrum master_ will decide which sprint will come next.

### Workspace configuration
We have the following pipelines (columns) configured in Zenhub:
* **Icebox**: issues we will never work on. These may be valid, but are not a priority given finite time and resources.
* **New Issues**: newly-filed issues. They will remain here until triaged and labeled to go into either the Product Backlog, Next Sprint, Current Sprint Backlog, In Progress, or Icebox pipeline.
* **Product Backlog**: triaged issues that are not part of the current sprint or an upcoming sprint.
* **Next Sprint**: issues that have been labeled and are being groomed for an upcoming sprint. Note: all upcoming sprints (there can be several being planned in parallel) share this pipeline.
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

In the Review meeting, the _Product owner_ will lead the discussion. The focus will we be on the content of the sprint and the outcomes achieved. Feedback on the sprint content will also be collected. At the end of the Review meeting, the team will triage any outstanding issues from the sprint. The _Product owner_ will engage with developers who still have work marked as **In Progress** to figure out how and when to wrap-up that work during the _[Time between sprints](#time-between-sprints)_.  All issues that have not been started will be moved back into the **Product Backlog**.

In the Retrospective meeting, the _Scrum master_ will lead the discussion. The focus will be on the sprint process itself in an attempt to uncover grey areas and process improvements. If the team agrees to adopt a particular process change, it should be clearly marked in the meeting notes with an **ACTION** label and the person responsible for that action, if appropriate.

Notes for both meetings should be taken using the templates provided:

* sprints/
  * templates/
    * [sprint-retrospective.md](./sprints/templates/sprint-retrospective.md)
    * [sprint-review.md](./sprints/templates/sprint-review.md)

As process changes are adopted, [this document](./README.md) should be updated to reflect the new process.

### Time between sprints
We allow ourselves *one week* between sprints. This buffer allows us to analyze the previous sprint without the pressure of immediately jumping into something new. Pragmatically speaking, it also gives us the time to finish off sprint items that may still require deployment, to address unanticipated fallout from the previous sprint, and to deal with the backlog of small, timely requests that may have accumulated during the sprint.
