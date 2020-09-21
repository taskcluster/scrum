# Initiatives

An _initiative_ is a collection of one or more milestones that, taken together, address one or more themes. Initiatives map to major projects that the Taskcluster team would like to accomplish, and can be either new functionality or substantial reworks of existing functionality. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.

The following are the current initiatives:

* [Artifact Integrity](#artifact-integrity)
* [Implement the Github Checks API](#checks-api)
* [Automatically deploy config changes to community-tc](#community-tc-deployment)
* [Move frequently-updated complex configuration out of the deployment config and into the API](#config-in-api)
* [Decommission docker-worker](#decom-docker-worker)
* [Implement the Object Service](#object-service)
* [Implement projectId](#project-id)
* [More secure, well-documented process for interactive tasks](#secure-interactive-tasks)
* [Streamline service deployment configuration](#service-deployment-streamlined)
* [Implement taskQueueId](#task-queue-id)
* [Help users construct taskcluster.yml](#taskcluster-yml-helper)
* [Use SOPS instead of password-store](#use-sops)
* [Better worker capacity estimates](#worker-capacity-estimates)
* [Use worker-runner everywhere](#worker-runner-everywhere)
* [Structured Logging for Workers](#worker-structured-logging)

To update this information, edit `data/initiatives.yml` and run `generate.py`.

## artifact-integrity
*Artifact Integrity*

[more information](https://docs.google.com/document/d/14miyPpGnpiyvFb93-doV7ENcKjwSdZYUV1VplPEcRqU/edit#heading=h.jgvxmoleismy)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aartifact-integrity)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## checks-api
*Implement the Github Checks API*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1459645)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Achecks-api)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [Promote external adoption](./themes.md#tc-adoption)


## community-tc-deployment
*Automatically deploy config changes to community-tc*

TBD

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Acommunity-tc-deployment)

*Addresses Theme:*

* [More efficient, reliable operations](./themes.md#operations)


## config-in-api
*Move frequently-updated complex configuration out of the deployment config and into the API*

TBD

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aconfig-in-api)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## decom-docker-worker
*Decommission docker-worker*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1499055)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Adecom-docker-worker)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## object-service
*Implement the Object Service*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1471582)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aobject-service)

*Addresses Themes:*

* [Support cost reduction](./themes.md#cost-reduction)
* [Promote external adoption](./themes.md#tc-adoption)
* [Make data actionable](./themes.md#actionable-data)


## project-id
*Implement projectId*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1607487)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aproject-id)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [Make data actionable](./themes.md#actionable-data)


## secure-interactive-tasks
*More secure, well-documented process for interactive tasks*

[more information](https://github.com/taskcluster/taskcluster-rfcs/issues/41)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Asecure-interactive-tasks)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## service-deployment-streamlined
*Streamline service deployment configuration*

[more information](https://github.com/taskcluster/taskcluster/projects/8)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aservice-deployment-streamlined)

*Addresses Themes:*

* [More efficient, reliable operations](./themes.md#operations)
* [Promote external adoption](./themes.md#tc-adoption)


## task-queue-id
*Implement taskQueueId*

[more information](https://github.com/taskcluster/taskcluster-rfcs/pull/145)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Atask-queue-id)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## taskcluster-yml-helper
*Help users construct taskcluster.yml*

TBD

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Ataskcluster-yml-helper)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [Promote external adoption](./themes.md#tc-adoption)


## use-sops
*Use SOPS instead of password-store*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1483320)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Ause-sops)

*Addresses Theme:*

* [More efficient, reliable operations](./themes.md#operations)


## worker-capacity-estimates
*Better worker capacity estimates*

TBD

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aworker-capacity-estimates)

*Addresses Theme:*

* [Support cost reduction](./themes.md#cost-reduction)


## worker-runner-everywhere
*Use worker-runner everywhere*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1602946)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aworker-runner-everywhere)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [More efficient, reliable operations](./themes.md#operations)


## worker-structured-logging
*Structured Logging for Workers*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1529660)

[*Associated Epics*](https://github.com/taskcluster/scrum/issues?q=is%3Aissue+is%3Aopen+label%3Ainitiative%3Aworker-structured-logging)

*Addresses Theme:*

* [Make data actionable](./themes.md#actionable-data)

