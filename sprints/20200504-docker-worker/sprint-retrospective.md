# docker-worker sprint retrospective

While our process was far from perfect, the team enjoyed our first foray into scrum. They called out the increased focus as a win, and liked not being pulled away from other projects constantly. Those who chose to pair-program during this sprint also cited that process as beneficial.

However, we also found many ways to improve our scrum process for next time. Here's a list of improvements we're implementing for our next sprint:
* Use proper scrum roles, specifically assign a scrum master and product owner. While it makes sense for me to act as scrum master, trying to also act as product owner didn't really work out. These are separate roles and should be held by separate people.
* Define our goals better upfront. This will help us know better what's in scope and what isn't.
* Project tracking
  * The github project board was a good start, but it was sometimes hard to find the next issue to work on. This was largely due to cards not having sufficient information, or simply linking out to bugzilla. For the next sprint, only github issues can be added to the Backlog. If we need to link to bugzilla, we'll do it from the issue. This has lots of other ancilliary benefits around work tracking in github as well.
  * We'll add two new columns to the project board:
    1. Deep Freeze: this is for good ideas that realistically we will never get to
    2. Ideas: These are ideas that we want to not lose track of, but haven't had time to flesh out to into an issue yet.
* Stand-up notes: Don't bother collating them. I was the only one reading them anyway, and I can do that in Slack as required.
* Sprint duration: Looking ahead on the calendar, there is a company-wide virtual all-hands happening in 3 weeks, so we chose a 3-week sprint for our next cycle. We'll use some time during that virtual event to perform our review and retrospective for that cycle.

In aggregate, the above list can be summarized as "Do scrum properly." As Dustin rightly pointed out, we have a history at Mozilla of implementing 10% of a new process framework and then abandoning it when it doesn't work out. Much better to jump in with both feet and see whether the new process is better than what you were doing before. Abandoning is always still an option.

There were also some things we discussed but didn't come to a conclusion on:
* Reporting: We need some way to surface our progress and accomplishments. You're reading this here, but this may not be the final form or location for these reports.
* Syncing releases to sprints: CloudOps would prefer fewer, more regular Taskcluster deployments. We haven't ruled this out, but are still in a mode where bustage fixes sometimes need to be deployed ASAP. This is still TBD.
* Volume of incoming requests: We still receive a fair volume of operational requests from other teams. This is going to reduce our ability to effectively focus during sprints if we can't bring that request volume down.

Based on that volume of incoming requests, we also decided on the initiative for our next sprint: Worker Lifecycle Management.
