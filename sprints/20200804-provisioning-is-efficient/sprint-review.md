# Sprint Review - Provisioning is efficient, August 4 - August 11, 2020

## Goal
Our goal with this sprint was to find the balance between latency, throughput, and cost in our cloud provisioning system using whatever tools we could bring to bear.

### Epics
1. [Cloud providers are hardened and simplified](https://github.com/taskcluster/scrum/issues/10)
2. [We spend as little as possible to do the most amount of work](https://github.com/taskcluster/scrum/issues/11)

## Outcomes
It's important to note at the outset that the sprint was initially scheduled to last three weeks. The Product Owner stopped the sprint after only a week when [Mozilla announced massive layoffs](https://blog.mozilla.org/blog/2020/08/11/changing-world-changing-mozilla/).

Despite the short duration, we still achieved some worthwhile outcomes:

* **[Added support for a workerpool scaling ratio](https://github.com/taskcluster/taskcluster/issues/3168)**: breaking the conventional mapping that 1 pending task == 1 worker request should lead to less over-provisioning of cloud resources and reduced costs overall. This is functionality that previously existed in [aws-provisioner](https://github.com/taskcluster/aws-provisioner), but was poorly understood. It is a useful knob for tweaking CI efficiency going forward.
* **[We now have a provisioning simulator](https://github.com/taskcluster/taskcluster/issues/3318)**: historical attempts at improving the efficiency of provisioning have been based on educated guesses and involved testing theories directly in production. Now that we have a simulator, anyone with a theory about provisioning can validate their model, and iterate safely. This will be useful if we need to change what we are optimizing for when provisioning, e.g. cost vs end-to-end time.

## Feedback
Overall, the team considered this a successful sprint. We needed to cancel the sprint early, but not because the sprint itself wasn't going well. That we were still able to achieve the two high-value pieces of work noted above despite the shorter duration is a testament to that.

The team also called out how this sprint provided a good introduction to how workers are provisioned in Taskcluster for people who had not previously worked with worker-manager or the providers.

Similar to previous sprints, we struggled with larger, monolithic pieces of work blocking the critical path. The worker-manager refactor was one piece that was not finished and was flagged as something that could have used more decomposition. The simulator was also a big piece of work, but we managed to complete it because work on it began a few days before the scheduled start of the sprint. That's not a model we want to rely on in the future.
