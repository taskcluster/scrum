# Sprint retrospective - Postgres phase 2, June 22 - July 24, 2020

## What worked
* Well-structured
  * Thanks to @helfi92 for organizing the work so well
  * Concerns at the outset about whether we had signed up for too much work, but because the work was so well-defined, we were able to stay on track.
  * It was large, but mostly mechanical, process
    * It could have been tempting to not continue to phase 2 and stick with entities.
    * Boring, but necessary and fruitful work in order to realize the other benefits of postgres down the road.
    * Got it done, like ripping a bandaid off
    * Over 30K lines of code changed, mostly in same area
    * @petemoore touched node code and survived!
      * @petemoore was also on PTO for the final two weeks of the sprint yet we still managed to get stuff done.
        * Rest of the team remained effective, efficient
* Not afraid of creating throwaway, intermediate infra to make the process much easier.
  * The tooling and test frameworks that @helfi92 & @djmitche made it easy for others to plug-in quickly.
  * Look ahead to Object Service which may benefit from a similar pattern.
* Merge conflict resolution skills got a workout
  * Usually this is something teams shy away from, but the skills themselves are super-useful to have.
  * Again, the scripting that was developed to assist with rebasing was great.
* We used the minimum viable tooling to assist with migration
  * We didn't rely on an extra ORM or framework like [Knex](http://knexjs.org/) which meant that there was less for people to learn.
* We established a virtuous help cycle
  * At some point during the sprint, every person on the team helped everyone else
  * Lots of pairing
  * Useful and practical, again because everyone was on same page
* The tree-closing window (TCW)
  * We decided to rollback rather than risk a downtime of unknown duration.
  * Versioning saved us, or at least gave us an acceptable fallback position where we lost less work.
    * Having multiple releases as fallback points for the TCW
  * Flexibility in TCW timing with Release Management
    * We were able to schedule the TCW a week later than it would have normally taken place.
    * Because systems are generally better automated and more resilient than a few years ago. RelMan can be more flexible with timing, provided we engage them early and we have a solid rollback story.
* Zenhub
  * The Zenhub tooling around issues proved better (more full-featured) than the github version.
  * The blocking/blocker labelling was useful
    * e.g. When we decided to cut signing, we immediately knew how many other issues would be effective and could also be cut.
* We managed to maintain a balance between external requests and sprint focus.

## What didn't
* Zenhub
  * Despite generally being a welcome addition to the sprint process, we ran into some issues with Zenhub that weren't great:
    * Occasional blank pages, sometimes associated with switching tabs.
    * Labels that we added to issues sometimes went missing, i.e. our changes didn’t stick and we needed to redo some work.
    * The default layout requires large display.
      * @imbstack found it hard to use on a small laptop screen.
  * Nice-to-have features we wish the tool had:
    * the ability to fullscreen a particular pipeline for triage.
    * clone an issue/card
* The tree-closing window (TCW)
  * We didn't manage to accomplish all the work we planned due to slower performance on the production database than we saw in staging.
    * We still don't understand the reason(s) behind the performance difference.
* We could have had better communication with CloudOps in the run-up to the TCW.
  * If we're planning for people to need to work weekends, we should involve them in the process as early as possible.

## Process changes for next sprint
* Avoid merge conflicts by having a work item to merge other pieces of work
  * When we're all working on the same files (which is likely in the sprint model), designate a "merge master" to resolve conflicts.
* Triage
  * There was some uncertainty around where issues should go when filed: Icebox vs New Issues vs Product Backlog
  * By default, new issues go to the Icebox.
    * This is a good default state because it means some small action is required to acknowledge issues that we will actually work on at some point.
  * The team found Zenhub useful for triaging issues added to the Icebox because the volume is low.
    * ...whereas Github was more useful for larger triage of New Issues/Product Backlog
* Product owner responsibilities
  * Now that we have access to it, the [burndown chart](https://app.zenhub.com/workspaces/taskcluster-5ed15d37c2d9744af28567dc/reports/burndown?milestoneId=5499987) is essential for visualizing progress and delays.
  * Keeping on top of burndown chart is now a primary responsibility for the Product Owner, although the rest of the team show also be looking at it.
    * Be sure to compare the view with "In Progress" issues included alongside the view with only "Closed" issues.
    * To help avoid the initial plateau of productivity, future Product Owners are encouraged to front-load sprints with smaller issues/pieces of work to help people ramp up, especially when they are unfamiliar with the domain.
  * When organizing the sprint, it's important to consider factors that might introduce delays and schedule accordingly. Two such factors we encountered during this sprint were:
    1. Reviews for known large changes - some of the database table changes requires thousands of lines of code and proper reviews take time; and,
    2. Deployments - while most deployments can happen quickly, there are external factors like CloudOps availability and Firefox release schedules that we need to account for.
* Stand-ups
  * We decided that forcing people on the west coast to sacrifice their sleep to attend stand-ups was not kind.
    * Also, east coast people found it strange to reporting status midway through their day.
    * @petemoore was on PTO, so we didn't get his feedback re: CEST timing
  * New model will have localized stand-ups at 09:30 for each timezone
    * We will also try to automate the announcement of the stand-ups in the Slack channel using the gcal integration.
    * It is still incumbent on the Product Owner and Scrum Master to review the daily stand-up notes to look for blockers or other problems.
