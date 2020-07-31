# Sprint Review - Postgres phase 2, June 22 - July 24, 2020

## Goal
This was a more mechanical sprint than previous sprints, but we knbew that going in. Our goal was to migrate the existing entities-based database storage system that mimiced the initial Azure JSON blob storage schema to a proper relational view where data was stored in a well-defined column structure. This was reflected in our choice of Epics for this sprint.

### Epics
1. All DB data is stored as relational tables with columns instead of entities
2. Create and update tools to facilitate work with new db format

## Outcomes
All told, here were 28 tables to migrate to the new format. By the official end of the sprint, 26 of the 28 tables had been migrated in code, and the remaining 2 tables had code owners who were continuing to work on migration.  We knew going into this sprint that is was going to be a lot of work and we scheduled 5 weeks deliberately. If the work planned TCW (see below) had proven successful, we would have been on track to finish on schedule.

Product owner (hassan) removed cards not on critical path towards end of sprint

At the end of the sprint, the team moved any non-table migration issues labelled “db” from the Current Sprint Backlog to the Product Backlog. We also did an explicit scan of the New Issues and Product Backlog pipelines and labelled

### Tree-closing Window (TCW)
Current state
  Firefox CI: Taskcluster v33 & DB 19
  Didn’t plan to be in this state, are we OK?
Issues
  Queue table not migrated
  Timing: would take ~17hr if rate is constant
Implications for next sprint?
  End up with different versions in community and firefox-ci (or same “version” with different content, i.e. v20 might mean different things)
  Concurrency issues
      One task per transaction
  Potential Solutions
    [dustin] Process table in background over course of coming week
    New data goes into new table;
    services checks new table first
      If not found, clones data from old table into new table
    Re-run table upgrade during next TCW
    [miles] Clone db in CloudSQL, run upgrade, change URL, and observe timing
    [coop] talk to selena re: postgres contractors
Does the future of TC include long downtimes?
Not if we want TC to ever be used outside Mozilla
Short downtimes, or online migrations
Need to budget more time (online migrations take longer)
Online migration of queue took 49 hours, but involved no downtime
Judicious use of downtime
Downtime budget exceeded (but not by much)

## Feedback
  Well-structured
    Team level of confidence with postgres?
        We know enough now for what we’ll need to do for TC
    Monotonous
        Repetitive work for 1 long sprint
        Dangerous but boring
        Replicating azure entities (part 1) was the annoying part
    A little bit open-ended
        Some problems weren’t solved at the outset
            E.g. signing, crypto
    Lack of previous exposure to postgres led to some problems
        Hit a bunch of unknowns (that might have been known to others)
    Focus on tooling at the outset?
    A few things were missed (named args functions)
Burndown chart reveals early lag
Table changes (esp. Large ones) require more review, up to a week
Deployment adds another lag
    Postgres phase 3?
        Type of work would be different


