# Initiatives

An _initiative_ is a collection of one or more milestones that, taken together, address one or more themes. Initiatives map to major projects that the Taskcluster team would like to accomplish, and can be either new functionality or substantial reworks of existing functionality. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.

The following are the current initiatives:

* [Artifact Integrity](#artifact-integrity)
* [Switch the Taskcluster datastore from Azure to Postgres](#azure-to-postgres)
* [Implement the Github Checks API](#checks-api)
* [Automatically deploy config changes to community-tc](#community-tc-deployment)
* [Move frequently-updated complex configuration out of the deployment config and into the API](#config-in-api)
* [Decommission docker-worker](#decom-docker-worker)
* [Implement the Object Service](#object-services)
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

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## azure-to-postgres
*Switch the Taskcluster datastore from Azure to Postgres*

[more information](https://github.com/orgs/taskcluster/projects/6)

*Addresses Theme:*

* [Make data actionable](./themes.md#actionable-data)


## checks-api
*Implement the Github Checks API*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1459645)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [Promote external adoption](./themes.md#tc-adoption)


## community-tc-deployment
*Automatically deploy config changes to community-tc*

TBD

*Addresses Theme:*

* [More efficient, reliable operations](./themes.md#operations)


## config-in-api
*Move frequently-updated complex configuration out of the deployment config and into the API*

TBD

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## decom-docker-worker
*Decommission docker-worker*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1499055)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## object-services
*Implement the Object Service*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1471582)

*Addresses Themes:*

* [Support cost reduction](./themes.md#cost-reduction)
* [Promote external adoption](./themes.md#tc-adoption)
* [Make data actionable](./themes.md#actionable-data)


## project-id
*Implement projectId*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1607487)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [Make data actionable](./themes.md#actionable-data)


## secure-interactive-tasks
*More secure, well-documented process for interactive tasks*

[more information](https://github.com/taskcluster/taskcluster-rfcs/issues/41)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## service-deployment-streamlined
*Streamline service deployment configuration*

[more information](https://github.com/taskcluster/taskcluster/projects/8)

*Addresses Theme:*

* [More efficient, reliable operations](./themes.md#operations)


## task-queue-id
*Implement taskQueueId*

[more information](https://github.com/taskcluster/taskcluster-rfcs/pull/145)

*Addresses Theme:*

* [Improve usability](./themes.md#usability)


## taskcluster-yml-helper
*Help users construct taskcluster.yml*

TBD

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [Promote external adoption](./themes.md#tc-adoption)


## use-sops
*Use SOPS instead of password-store*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1483320)

*Addresses Theme:*

* [More efficient, reliable operations](./themes.md#operations)


## worker-capacity-estimates
*Better worker capacity estimates*

TBD

*Addresses Theme:*

* [Support cost reduction](./themes.md#cost-reduction)


## worker-runner-everywhere
*Use worker-runner everywhere*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1602946)

*Addresses Themes:*

* [Improve usability](./themes.md#usability)
* [More efficient, reliable operations](./themes.md#operations)


## worker-structured-logging
*Structured Logging for Workers*

[more information](https://bugzilla.mozilla.org/show_bug.cgi?id=1529660)

*Addresses Theme:*

* [Make data actionable](./themes.md#actionable-data)

