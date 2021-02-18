# Themes

Themes are large focus areas than span the Mozilla organization and are pertinent and addressable by the Taskcluster team.

The following are the current themes:

* [Make data actionable](#actionable-data)
* [Support cost reduction](#cost-reduction)
* [Project Maintenance](#maintenance)
* [Team Operations](#operations)
* [Promote Taskcluster's external adoption](#tc-adoption)
* [Improve Taskcluster usability](#usability)

To update this information, edit `data/themes.yml` and run `generate.py`.

## actionable-data
*Make data actionable*

Provide data to project stakeholders that can be used to make decisions about the project.

*Associated Initiatives:*

* [Implement the Object Service](./initiatives.md#object-service)
* [Implement projectId](./initiatives.md#project-id)
* [Structured Logging for Workers](./initiatives.md#worker-structured-logging)


## cost-reduction
*Support cost reduction*

Build functionality that can be used to reduce costs for the projects we develop and operate.

*Associated Initiatives:*

* [Implement the Object Service](./initiatives.md#object-service)
* [Better worker capacity estimates](./initiatives.md#worker-capacity-estimates)
* [Automatic rebuilding of worker machine images](./initiatives.md#automated-worker-image-builds)


## maintenance
*Project Maintenance*

Ongoing maintenance of Mozilla software projects, with specific goals in mind for each project, such as continued operation, retirement, or handoff to another team (internal or external).

*Associated Initiatives:*



## operations
*Team Operations*

Improve our operational efficiency, including
 * Management of Community-TC
 * General team operations (secret handling, access control, etc.)

*Associated Initiatives:*

* [Use SOPS instead of password-store](./initiatives.md#use-sops)
* [Automatically deploy config changes to community-tc](./initiatives.md#community-tc-deployment)
* [Automatic rebuilding of worker machine images](./initiatives.md#automated-worker-image-builds)


## tc-adoption
*Promote Taskcluster's external adoption*

Promote adoption and use of Taskcluster more broadly than Firefox CI

*Associated Initiatives:*

* [Streamline service deployment configuration](./initiatives.md#service-deployment-streamlined)
* [Implement the Object Service](./initiatives.md#object-service)
* [Implement the Github Checks API](./initiatives.md#checks-api)
* [Help users construct taskcluster.yml](./initiatives.md#taskcluster-yml-helper)
* [Support private taskcluster deployments](./initiatives.md#private-deployments)


## usability
*Improve Taskcluster usability*

Improve Taskcluster's usability and suitability for common uses.  This includes both quality-of-life improvements and substantial features to support users' needs.  This includes support for deployment and operation of Taskcluster (configuration, logging, monitoring, etc.)

*Associated Initiatives:*

* [Use worker-runner everywhere](./initiatives.md#worker-runner-everywhere)
* [Streamline service deployment configuration](./initiatives.md#service-deployment-streamlined)
* [Implement projectId](./initiatives.md#project-id)
* [Implement the Github Checks API](./initiatives.md#checks-api)
* [Artifact Integrity](./initiatives.md#artifact-integrity)
* [More secure, well-documented process for interactive tasks](./initiatives.md#secure-interactive-tasks)
* [Decommission docker-worker](./initiatives.md#decom-docker-worker)
* [Move frequently-updated complex configuration out of the deployment config and into the API](./initiatives.md#config-in-api)
* [Help users construct taskcluster.yml](./initiatives.md#taskcluster-yml-helper)

