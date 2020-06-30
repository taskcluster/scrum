# Taskcluster Agile Process Tracking

* [Definitions](#definitions)
* [Tools](#tools)
* [Roles](#roles)
* [Sprint process](#sprint-process)

___

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
An _initiative_ is a collection of one or more milestones that, taken together, address one or more themes. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.

### Milestone
The _milestone_ is the goal for a sprint and, as such, should be able to be completed during the sprint duration made up of a small collection of epics. This can be a thin wrapper around a single epic if the user story is large and/or important enough. Milestones can address one or more themes.

### Epic
An _epic_ a large user story that describes plainly a feature of the Taskcluster system. Epics can address multiple themes. User stories are an important aspect of agile development, but we've chosen to map them to Epics in our usage to make them trackable at the correct level using [our tooling](#Tools).

### Issue
An _issue_ is a single, cohesive task as represented by a Github issue. Larger issues should be decomposed into smaller issues. No single issue should taken more than 1 engineer week to accomplish, modulo time to review and deploy. Issues should address a single theme.

A well-defined developmemt issue is the basis for all of our estimation. It cannot be overstated how important it is to make sure issues are decomposed to the point where they can be estimated accurately. It underpins _everything_ else.

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
The _Product owner_ manages the product backlog and keeps the rest of the team working on the most important thing. They have the final decision on matters of scope. They can also change the scope of the current milestone or, at their discretion,  end the sprint early.

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
As the sprint draws to a close, the _Product owner_ and _Scrum master_ will meet to decide what issues from the _Current Sprint Backlog_ (if anything) still needs to be done. The _Scrum master_ will move all issues that have not been started to the Product Backlog pipeline. The _Product owner_ will engage with developers who still have work in progress to figure out how and when to wrap-up that work during the _Time between sprints_.

### Time between sprints
We allow ourselves *one week* between sprints. This buffer allows us to analyze the previous sprint without the pressure of immediately jumping into something new. Pragmatically speaking, it also gives us the time to finish off sprint items that may still require deployment, to address unanticipated fallout from the previous sprint, and to deal with the backlog of small, timely requests that may have accumulated during the sprint.
