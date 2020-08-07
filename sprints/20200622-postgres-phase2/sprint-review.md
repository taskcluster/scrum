# Sprint Review - Postgres phase 2, June 22 - July 24, 2020

## Goal
This was a more mechanical sprint than previous sprints, but we knew that going in. Our goal was to migrate the existing entities-based database storage system that mimicked the Azure JSON blob datastore to a proper relational schema where data was stored in a well-defined column structure. This was reflected in our choice of Epics for this sprint.

### Epics
1. [Create and update tools to facilitate work with new db format](https://app.zenhub.com/workspaces/taskcluster-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/3)
2. [All DB data is stored as relational tables with columns instead of entities](https://app.zenhub.com/workspaces/taskcluster-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/3)

## Outcomes
All told, there were 28 tables to migrate to the new format. @helfi92 and @djmitche had come up with a well-documented, 2-step migration plan that made most table migrations easy. In some cases, we tried to address table structure issues that were relics of the Azure storage, e.g. extra queue tables that existed solely to provide another index, but this was the exception rather than the rule.

By the official end of the sprint (July 24), 26 of the 28 tables had been migrated in code, and the remaining two tables had code owners who were continuing to work on their migration. I say "in code" because, as of the time of writing, all of the database changes have not yet been pushed to the live clusters -- community & firefox-ci -- due to delays caused by the TCW (see below) and ongoing Firefox releases that made it preferable to *not* change the underlying infrastructure unduly.

We knew going into this sprint that it was going to be a lot of work and we scheduled 5 weeks deliberately. If the work planned TCW (see below) had proven successful, we would have been on track to finish on schedule.

As a result of the delay introduced by the TCW, @helfi92 opted as _Product owner_ to constrain the critical path to [Epic 2](https://app.zenhub.com/workspaces/taskcluster-5ed15d37c2d9744af28567dc/issues/taskcluster/scrum/3) to ensure all the tables were migrated to the new format.

At the end of the sprint, the team moved any non-table migration issues labelled “db” from the Current Sprint Backlog to the Product Backlog. We also did an explicit scan of the New Issues and Product Backlog pipelines and labelled any database-related issues with "db" as well.

### Tree-closing Window (TCW)
During the TCW, the migration of one of the larger queue tables for the firefox-ci cluster proceeded much more slowly than anticipated by previous experiments. The same query that had taken ~5 hours in the development environment was still running after 10 hours on the production cluster, and was predicted to take at least another 6 hours. Rather than hold the trees closed beyond the planned 12-hour window, we canceled the running query and performed a rollback.

Luckily, the Taskcluster release structure for this sprint meant that we didn't lose *all* the work that was planned for the TCW. Starting at db version 18 and Taskcluster version 32 before the sprint and aiming for db version 20 and Taskcluster version 34 after, we were able to rollback to db version 19 and Taskcluster version 33 for the firefox-ci cluster that included most of the small- and medium-sized tables that had been migrated.

Of course, this left us with a major queue table not migrated. It also left us with a bunch of uncertainty around the comparability of our dev and production environments, and also the unappealing prospect of needing to schedule yet another TCW.

We convened a quick post-mortem on Monday morning to examine our options:
1. **Re-run the table upgrade during the next scheduled TCW**: This was not ideal for a number of reasons. It meant waiting (most likely) another 3 weeks until the TCW. Because the changes to the database underpin so much else, this would have meant the Taskcluster code running on the firefox-ci cluster would stagnate for 3 weeks. If we did need to deploy an emergency fix, it would require a bunch of manual work.
2. **Take an emergency downtime to run the table upgrade ASAP**: Because we didn't know *why* the performance had been so bad, this would have been a major gamble. To get more data here, we did ask the CloudOps team to restore a recent db backup to a separate environment so we could try re-running the migration under various scenarios to try to figure out the performance profile.
3. **Modify the db functions to migrate the table data in the background while the cluster was still running**: Because the table was so large and the timing of TCWs can be uncertain, we had actually discussed this idea while planning the sprint, but had dismissed it due to the favorable timing of the current TCW. This was deemed to be the best option of the bunch, but would require very careful review to prevent data loss in the production cluster.

@djmitche set to work on the background processing and after a week of testing, testing, and more testing, had a new version ready for deployment. It would take longer, but the production database would be available for the duration.

CloudOps kicked off the update process the following Monday, and 47.5 hours later, the offending queue table had been migrated with 0 downtime (if you don't count the TCW, naturally).

## Feedback
The team felt the sprint was well-structured and understood the importance of tackling this work in one cohesive chunk, like ripping a band-aid off as mentioned in the [retrospective notes](./sprint-retrospective.md). That said, they aren't keen on jumping into another sprint of this type any time soon.

The real danger here was that the work was monotonous and repetitive. One team member referred to it as "dangerous, but boring" meaning that it wasn't particularly fun, but there was always the potential to destroy or corrupt production data if you got it wrong.

Of the two steps in the migration process, the mechanical first step was the most prone to issues. Step 2 involved updating database function and left a little more room for thought and design. Despite the very regimented nature of the sprint, team members appreciated that there was was some latitude for judgment and even design on some issues. For example, we didn't completely understand how we were going to tackle crypto and signing before the sprint began, but scheduled work to figure them out along the way.

Overall, the previous lack of team experience with postgres caused a few issues, but these were largely mitigated by the docs and tooling put together by @helfi92 and @djmitche. One particular example of a tooling improvement that could have been beneficial if we'd had it sooner is the [support for named arguments in db functions](https://github.com/taskcluster/taskcluster/issues/2928). As we closed out the sprint, the team felt confident that we had enough collective knowledge with postgres now to accomplish the things we want to do with Taskcluster in the future. At the same time, we felt it prudent to try to collect a list of postgres resources/contractors that we could turn to if we did need help with design or performance. @coop is reaching out to @selenamarie to start compiling that list.

Our experience with the recent TCW has made us rethink our approach to tree closures going forward. Can we afford to take long downtimes in the future? Our general feeling is "No." With the volume of data being manipulated in the firefox-ci cluster, future downtimes for work touching large tables would need to be lengthy. Witness that we budgeted 12 hours for the most recent downtime and still ran out of time. Certainly if we have any hope of ever seeing Taskcluster used outside of Mozilla, asking external users to take multiple hours of downtime for upgrades is a hard sell, and possibly even a non-starter.

We now have a useful model for online migrations based on [the recovery work after the TCW](https://github.com/taskcluster/taskcluster/issues/3235). @djmitche is going to make notes about his process and we are considering creating a framework that we can choose to apply to future migrations. Online migrations do take longer; this one took over two days. For large tables, online migrations can avoid upgrade-related downtime altogether. However, for most smaller table migrations, this approach is overkill. For small tables we will be focusing on shorter downtimes measured in minutes to migrate tables during natural lulls in the workday, and will be working with sheriffs to schedule those.

There was some concern about exceeding our error budget with the recent TCW. All told, development trees were closed for 14 hours instead of 12. While not the most egregious delay we've ever experienced/caused, it is still prudent to be judicious in the coming months with our downtime requests.

It seems unlikely at this point that we would have another sprint focused entirely on the database, i.e. a Postgres phase 3. Now that the Taskcluster database is in a state more conducive to hacking and experimentation, small bits of database work will happen naturally as part of future sprints focused on other areas.
