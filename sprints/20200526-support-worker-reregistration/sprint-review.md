# Sprint Review - Support worker re-registration

For our second sprint, we started with what sounded like a good goal, "Worker Lifecycle Management." We described this as,

> Improvements to management of workers' lifecycle, and users' ability to understand and debug that lifecycle.

We broke that down further into two epics that seemed relevant:

1. Managing resources more effectively and recovering from worker failures better.
2. Revealing useful status and debugging information to users

We set up our [project board](https://github.com/taskcluster/taskcluster/projects/7) and went to work.

About a week into our three-week sprint, we had a few realizations:

* our initial goal and associated epics were too broad to adequately scope the work we *needed* to accomplish in this particular sprint
* migrating the workers table from JSON blobs to a proper relational structure was a big project on its own and couldn't be decomposed/parallelized effectively
* migrating the workers table blocked most other work planned in the sprint

To his credit, Brian recognized this and, as product owner for this sprint, scoped down our sprint goal to "Support worker re-registration." We didn't change the Epics, but they ceased to have much relevance at that point. We didn't delete them though because they could still form the basis of future sprints.

We closed 37 issues during the sprint, with 3 more in progress but wrapping up soon. Strictly speaking, we did not hit our sprint target. The patches required to support worker re-registration still required review and deployment in the week following the sprint. This was mainly due to the aforementioned workers table migration. However, progress was delayed further by the need for [encrypted column support](https://github.com/taskcluster/taskcluster/issues/2962). We didn't recognize this dependency until the middle of the sprint. This piece required external security review, so we were gated on someone outside the context of the sprint.

Aside from worker re-registration support, we also managed to accomplish the following:

* debugged issues with worker overhead so that we can rely on those numbers going forward
* a suite of CI testing fixes for workers to make development and integration testing more reliable
* displaying current capacity for worker pools in a more convenient way

To validate the sprint output, we will start by adapting our own hardware pools in the [community cluster](https://community-tc.services.mozilla.com/worker-manager) to re-register workers. Most of the other projects in the community cluster have little incentive to migrate without a carrot and/or stick, so we plan to set a sunset date far in the future (i.e. a year from now) for worker pools that aren't configured to re-register, and help migrate the community pools when we can. We are uncertain of the timeline for updating the [Firefox CI cluster](https://firefox-ci-tc.services.mozilla.com/).
