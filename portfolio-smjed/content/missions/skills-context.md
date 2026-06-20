# Skills Context — Sabri's Real Experience

> Working doc for posts, missions, and narrative refinement.
> NOT part of the Hugo build. Reference-only.

---

## 1. Observability

### Grafana
- **Scale**: 2000 users across 10 instances
- **Deployment**: Both on-prem (deb packages + DBs) and full Docker via Helm
- **Datasources**: Elasticsearch, VictoriaLogs, Splunk, Loki, Prometheus metrics
- **Dashboarding**: Heavy transformation work across multiple datasources
- **Tooling built**: "Grafana Housekeeping" — gathers all resources (users, dashboards, alerts, contact points, datasources), checks for stale/broken/unused, sends reporting to Jira for manager-driven cleanups
- **MCP**: Used Grafana MCP

### Prometheus / Thanos
- **Scale**: Thanos cluster with global querier (to avoid having scattered Thanos instances in Grafana)
- **Topology**: Storage gateway cache + read gateway cache across 4 different clusters
- **Storage**: ~50TB managed, long-term (12-month) bucket
- **Nodes**: ~200 replica nodes (8GB RAM, 3 CPU each)
- **Project focus**: Maintaining and adding long-term storage for ML toolbox forecasting

### Loki
- **Scale**: 4 clusters, ~400 pods total, ~3TB RAM + significant CPU
- **Cache**: 2TB memcache cluster for 24h hot storage
- **Work**: Fine-tuning, installing cluster cache, experimenting with metric-splitting configurations
- **Recording rules**: Converted TB/day load-balancer logs into metrics

### Vector
- **Migration**: Migrated from Fluentd to Vector due to Fluentd performance issues
- **Scope**: Full pipeline migration + log transformations

### ELK
- **Full stack**: Beats, Kafka, Logstash (heavy transformations, also shipped to Splunk HEC), Elasticsearch, APM + RUM
- **Scale**: 200TB across 3 datacenters, high-availability setup
- **Users**: Team of 20 developers
- **Compliance**: Different retention policies for gambling regulator purposes

---

## 2. Kubernetes & Platform

### Kubernetes
- **Level**: Primarily user-level (not cluster administrator), operates apps via CI/CD
- **Workflow**: Jenkins + Makefile → build → push to JFrog → merged and deployed via ArgoCD
- **Helm**: Created Helm charts for own apps (Graphia, search query exporter, Grafana Housekeeping)
- **Apps deployed**: Graphia (SRE agent), search query exporter, Grafana Housekeeping tool

### Search Query Exporter (app built at FDJ)
- **Purpose**: Measure real user-experience search performance latency for SLO/SLIs
- **How it works**: Queries Splunk, Thanos, and Loki across multiple time ranges (10m, 1h, 6h, 24h, 7d, 30d)
- **Output**: Checks how the platform responds over time, compares against SLO budgets, flags when too slow
- **Design**: Easily configurable, multi-backend querying

---

## 3. CI/CD
- TODO: Still need detail on Jenkins, GitLab CI, GitHub Actions specifically

---

## 4. Automation & IaC

### PXE / Proxmox
- Automated PXE installation for Proxmox nodes using Ansible

### Full VM Delivery Pipeline ("Kubernetes without Kubernetes")
The complete flow, end to end:

**Phase 1 — Request (Git PR)**
- Create a tfvars with VM config. ~80% of variables are shared across providers, ~20% provider-specific (e.g. network on OpenStack, flavors)
- Push to git branch, open PR

**Phase 2 — Plan (Jenkins)**
- Jenkins detects the directory, picks the correct Terraform workspace (env-scoped to avoid massive plan/apply times)
- Runs `terraform plan` on the PR for review

**Phase 3 — Apply (on merge)**
- On merge, Jenkins runs `terraform apply`
- State backend: Consul (for state locking)
- VM is created → automatically registers in Consul and NetBox

**Phase 4 — Configuration (Ansible auto-discovery)**
- The tfvars includes an `ansible_playbook` parameter (e.g. "elasticsearch")
- On VM creation, Jenkins sets a NetBox custom field: `ansible_playbook: elasticsearch`
- Another custom field: `configured: false` (default)
- Jenkins launches a **meta-playbook** that uses dynamic inventory to find all VMs where `configured: false`
- Reads the `ansible_playbook` field, runs that specific playbook on the VM
- On success, flips `configured: true` in NetBox

**Phase 5 — Service Registration (Consul → HAProxy)**
- Consul service list feeds HAProxy for automatic backend host registration
- New VM is live and receiving traffic with zero manual intervention

**Phase 6 — Monitoring (Centreon auto-registration)**
- Built a custom Terraform provider for Centreon (`terraform-provider-centreon`, open-sourced on GitHub)
- VMs are automatically registered in Centreon monitoring as part of the pipeline
- Built because no Centreon Terraform provider existed at the time

**Context**: No Kubernetes available, so they built orchestration primitives from existing tooling to handle hundreds of VMs across datacenters during migrations.

### Jenkins + Terraform (Atlantis-like)
- Part of the pipeline above: Jenkins auto-runs terraform apply on merge with diff review

### Terraform Multi-Provider Module System
- Created a module template system using the **same variable files across providers**
- Supported providers: vSphere, Proxmox, OpenStack, NetBox
- ~80% shared variables, ~20% provider-specific

### Cloud & Infrastructure

### AWS
- **Usage**: Deployed ECS EC2, CloudWatch
- **Cost optimization**: Used CUR (Cost and Usage Report) to find and solve budget issues, helped teams build dashboards
- **Self-assessment**: Not very strong, needs more depth. Being honest about this.

### OpenStack
- **Admin**: Deployed a small 8-node cluster with Ceph, then migrated to Proxmox for ease of use ("it was a bit of a machine")
- **User**: Heavy Terraform user on OpenStack — deployed across multiple DCs (volumes, images, etc.)
- **Positioning**: Knows the platform well as a consumer, less as an admin

### OVH Cloud
- **Usage**: Used like Hetzner — VMs and dedicated servers for client deployments

### Proxmox
- **Scale**: Deployed 100+ Proxmox nodes
- **Automation**: Automated installation via PXE + Ansible
- **Storage backends**: NFS, ZFS, SAN, NVMe-oF (NVMe over Fabric), Ceph (managed by Proxmox)
- **Core infrastructure skill** — deep operational experience

### Ceph
- **Deployment**: Big Ceph RBD and Ceph S3 for Loki/OpenStack, deployed in VMs with cephadm
- **Scope**: Helped deploy and operate

### Linux
- Standard sysadmin-level, "nothing too fancy"

---

## 6. Data & Messaging

### PostgreSQL
- **Clustering**: Installed Patroni + ETCD for HA clustering
- **Backup**: PGBackrest
- **Frontend**: Dedicated HAProxy frontend for the DBs
- **Level**: Solid operational experience

### MySQL
- Installed and managed several times, no clustering experience

### SQL Server
- Same level as MySQL — install and manage

### Kafka
- **Scale**: 5 Kafka nodes
- **Use case**: Buffer for Logstash → Elasticsearch pipelines
- **Topics**: Different topics per pipeline, fine-tuned for the workload
- **Coordination**: Zookeeper (maintained it — "was a pain but it's powerful/complicated")

### Redis
- Tried OSS clustering, wasn't good enough for the requirements
- Switched to Couchbase (paid) instead

### RabbitMQ
- Messaging and message routing, standard cluster usage, nothing fancy

### Couchbase
- **Impact**: Big part of unibet.fr performance gains
- **Scale**: 10 servers x 64GB RAM
- **Design**: Multiple indexes, split and sharded
- **Role**: Managed everything AND advised developers on how to use it for performance gains
- **Note**: Replaced Redis because Redis OSS clustering wasn't cutting it

---

## 7. Networking & Delivery

### Load Balancers
- **Breadth**: F5, F5 Cloud, Nginx, HAProxy (with BGP), Envoy, Traefik
- **DDoS mitigation project**: Big project with F5 Cloud using rate limiting and various tools
- **HAProxy + BGP**: Used for the Consul-fed auto-registration backend system (from VM pipeline)

### DNS
- **Tools**: BIND, PowerDNS, Cloudflare DNS
- **Notable**: Multi-DC BIND public DNS with secured zone transfers (TSIG keys)
- **Scale**: Nothing massive, but solid

### VPN
- **Tech**: WireGuard, IPsec, GRE, OpenVPN
- **Use cases**: Router-to-router and client VPN
- **Level**: Standard usage, no major project

### Firewalls
- **Big project**: Migrated from SPOF FortiGuard perimeter firewall to BGP routers, pushing iptables/nftables rules to 1000+ VMs via Ansible
- **Rationale**: Moved firewalling to the VM level instead of the router (eliminated single point of failure)
- **Hardware experience**: Cisco ASA, Firepower, FortiGuard (clustering, VDOM)

### Networking (Hardware)
- **Switches/Routers managed**:
  - Cisco Nexus 3000 (installation + management)
  - Juniper MX204 (BGP, limited experience)
  - Juniper EX series
- **NDR / Traffic Analysis**: Installed ExtraHop NDR with Prismatic TAP (network traffic mirroring for analysis)
- **Level**: Solid sysadmin-adjacent networking, not a dedicated network engineer

## 8. Programming & AI

### Go
- Limited experience, mainly the Centreon Terraform provider

### Python
- Built multiple apps (SSHPlex, Search Query Exporter, Grafana Housekeeping, Graphia)
- Full CI/CD lifecycle: build, deploy, publish to PyPI
- Strong operational Python, not a software engineer

### Bash
- Heavy scripting for system installs and automation glue

### HCL
- Extensive Terraform + Consul usage

### YAML / JSON
- Ansible, Python configs, standard tooling

### AI / LLM Infrastructure
- **GPU deployment**: Built and installed 6 GPUs in datacenter across 2x 2U servers (4-GPU capability each)
- **Serving**: vLLM, Python client
- **RAG pipeline**: Embedder model + 1000+ PDFs + PostgreSQL vector DB + GPT OSS 20B
- **Agent**: Built a full-loop agent with safeguards and RBAC (team members get limited resource access)
- **Graphia**: SRE agent for Grafana diagnosis — RBAC-aware, MCP-based. Arch diagram incoming from work laptop.

### MCP (Model Context Protocol)
- Installed many MCP servers
- Built a Graphia MCP for devs/infra engineers (same RBAC, usage tracking)

---

## 9. Security

### Unibet.fr Scope Responsibility
- **Vulnerability management**: Followed up on Tenable/Nessus vulns and patches
- **Architecture review**: Checked PoCs and provided security inputs for new implementations (BIND, Packer, etc.)
- **DDoS mitigation**: Installed F5 Cloud as mitigation layer
- **Network monitoring**: Installed ExtraHop + alerts (DB dump detection, network anomalies)

---

## 10. Physical / Datacenter

### Rack Installation
- Installed 4-5 full racks from scratch: network → server → SAN for virtualization
- Knows cabling, on-site intervention

### NetBox + HA Architecture Design
- Managed NetBox as source of truth
- Designed HA Proxmox architectures with LACP/EVPN/VPC

---

## 11. Learning Gaps (self-identified)
- AWS / cloud depth
- BGP routing
- eBPF
- Full rack design best practices (A to Z)
- FinOps
- Formal SRE incident management processes
- Tracing (Grafana Alloy, OpenTelemetry) — did a little bit

---

## 12. Team & Leadership

### Working Style
- **80% solo**: Most projects owned end-to-end
- **20% team/project lead**: For Proxmox and infrastructure projects
  - Splits tasks, does knowledge transfer
  - Uses RAPID framework for validation
  - Runs Spike sessions before starting to scope properly
  - Weekly meetings to check blockers and progress
  - Still does ~50% of the hands-on work even when leading

---

## 13. Scale Numbers (Consolidated)

### VM Fleet
- **Peak**: ~3000 VMs under management
- **Migrations**: Recreated most of them for cross-DC migrations (vSphere → Proxmox, then some → OpenStack, then OpenStack DC → OpenStack DC)

### Datacenters
- **Org scale**: 30-40 DCs total, used 10 for replications (OpenStack, mostly usage not admin)
- **Directly managed**: 2 DCs / 8 racks at one point
- **VINC era**: 4 racks / 30 nodes

### Ingestion (The Real Numbers)
- **Loki**: 8 TB/day
- **Elasticsearch**: 2 TB/day
- **Thanos**: 1 TB/day
- **Combined**: ~11 TB/day

---

## 14. War Stories

### The Champions League Final Incident
- **Context**: Gambling platform — when a match settles (especially Champions League final), 10,000+ users connect within the SAME MINUTE. Business-driven traffic spike, not a DDoS, but hits like one.
- **The change**: Migrated firewall to nftables. Worked fine for 30 days.
- **The incident**: During a Champions League final, massive user spike. nftables conntrack table filled up → some users couldn't connect, others could. TCP window times were extremely long.
- **The fix**: Killed all HAProxy and nftables, bumped nftables conntrack limits, set aggressive TCP windows and TTL values.
- **How they found it**: Grafana dashboard caught the anomaly.
- **Lesson**: Conntrack sizing matters for bursty traffic. Default values don't survive gambling-scale spikes.

---

## 16. Migration Projects (Detail)

### a. vSphere → Proxmox Migration
- **Driver**: vSphere licenses costly + EoL
- **Approach**: Installed Proxmox, converted/rebuilt VMs node by node from vSphere
- **Storage**: Pure Storage SAN with NVMe-oF (MultipathD)
- **Backup**: Found and integrated Proxmox Backup Server as part of the migration

### b. Proxmox 4 → Proxmox 8 Upgrade
- Old cluster: 6 nodes, Proxmox 4
- New cluster: 4 nodes, Proxmox 8
- **Challenge**: OpenVZ containers to convert with zero or low downtime
- **Solution**: Used NFS as a buffer storage during the migration

### c. OpenStack DC → OpenStack DC Migration
- **Driver**: Source DC got decommissioned
- **Approach**: Used Terraform to rebuild VMs, Ansible to install, then switched HAProxy backends to new DC bit by bit

### d. Elasticsearch 200TB Cluster Migration
- **Scope**: 200TB ES cluster, DC to DC
- **Approach**: Rebuilt nodes 1 by 1 in the new DC, waited for shard rebalancing or forced shards to new nodes

---

## 17. Graphia — Pain Points Solved

### The Problem
- Grafana dashboards require deep expertise to build well ("need a PhD")
- Companies have 1000+ datasources — onboarding is slow
- Query languages (LogQL, PromQL, Splunk SPL) are a barrier
- Correlating metrics and logs across backends is manual and slow
- Jumping on an alert incident means starting from scratch every time

### What Graphia Does
- Removes the need to be a dashboard expert
- Abstracts away datasource complexity (fast onboarding)
- Eliminates query language knowledge requirement
- Correlates data across metrics and logs
- Prepares a battle plan when jumping on an alert incident
- RBAC-aware: team members get access only to their permitted resources
- Usage tracking built in

---

## 18. Honesty Notes (from Sabri)
- The 11TB/day observability stack was TEAM work, not solo. Don't oversell as "I built this alone."
- Loki was mostly already there — his contribution was fine-tuning + Fluentd→Vector migration + recording rules
- He didn't deploy 100% of the 3000 VMs himself — he BUILT THE TOOLING that enabled it
- Position as "operated and optimized" or "built the automation for" rather than "single-handedly ran"
- He'd be nervous taking on a solo "build me a new rack that ingests 10TB/day" mission

---

## 15. The "Why Freelance" Story

### Kindred Acquisition
- Before Kindred acquired (specifically France): startup-like culture, 5 people in infra, 10 in dev. Things moved fast.
- After acquisition: all process and drama. Speed died.
- Took a voluntary departure plan ("Plan de départ volontaire") — the financial runway made the exit possible.
