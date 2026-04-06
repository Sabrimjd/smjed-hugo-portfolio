---
title: "My Resume"
type: "resume"
---

## Summary

> I'm a Site Reliability Engineer with a DevOps background, focused on Kubernetes platforms, observability, automation, and building reliable systems that help teams move fast without losing operational confidence.

## Open Source Contributions

🌟 **Terraform Provider for Centreon V2 API**
> Developed and maintained a custom Terraform provider for Centreon's V2 API, enabling infrastructure as code capabilities for Centreon monitoring platform.
- GitHub Repository: [terraform-provider-centreon](https://github.com/Sabrimjd/terraform-provider-centreon/)
- Key achievement in bridging the gap between infrastructure automation and monitoring
- Demonstrates expertise in Go programming and HashiCorp's Terraform ecosystem

🌟 **SSHplex**
> Built and maintained an open source terminal UI for SSH connection multiplexing, designed for infrastructure teams that need fast host discovery, bulk operations, and persistent sessions.
- GitHub Repository: [SSHPlex](https://github.com/Sabrimjd/SSHPlex)
- Blog Post: [Building SSHplex](/posts/building_sshplex/)
- Combines NetBox, Ansible, Consul, and static lists as sources of truth for hosts and devices
- Supports three mux backends: tmux standalone, tmux + iTerm2, and native iTerm2 on macOS
- Provides broadcast commands and persistent sessions to replace expensive legacy tooling

## Experience

### <a href="https://www.kindredgroup.com/"><img src="/img/Kindred.webp" alt="Kindred France" style="height: 30px; padding-right: 10px; vertical-align: middle;"></a> Kindred France | Site Reliability Engineer | 2021 - Present

<div class="skills-container">
    <a href="/tags/kubernetes" class="skill-badge">Kubernetes</a>
    <a href="/tags/grafana" class="skill-badge">Grafana</a>
    <a href="/tags/loki" class="skill-badge">Loki</a>
    <a href="/tags/thanos" class="skill-badge">Thanos</a>
    <a href="/tags/vector" class="skill-badge">Vector</a>
    <a href="/tags/jenkins" class="skill-badge">Jenkins</a>
    <a href="/tags/gitlab-ci" class="skill-badge">GitLab CI</a>
    <a href="/tags/terraform" class="skill-badge">Terraform</a>
</div>

*   Progressed internally from System Engineer to Site Reliability Engineer, shifting my focus from infrastructure automation toward platform reliability, observability, and diagnostics.
*   Manage and improve observability workflows around Kubernetes, with Thanos, Loki, Grafana, and Vector as core technologies.
*   Built a HouseKeeping tool to diagnose stale and broken Grafana resources and improve day-to-day platform hygiene.
*   Built a Search Query Exporter to diagnose query slowness and establish SLOs across Thanos, Loki, and Splunk.
*   Built a Grafana AI Agent with enterprise-ready safeguards, including RBAC-aware behavior and MCP-based diagnosis flows.
*   Expanded recent hands-on expertise with Helm charts, Argo CD, container images, Jenkins, GitLab, Splunk, AWS CloudWatch, and CUR2.

#### Current stack and ownership

| Area | Components/Tools |
|------|------------------|
| Observability | Grafana, Loki, Thanos, Vector, Splunk, AWS CloudWatch |
| Platform Engineering | Kubernetes, Helm, Argo CD, Container Images |
| CI/CD & Automation | Jenkins, GitLab CI, Terraform, Ansible |
| Data & Storage | Kafka, Redis, PostgreSQL, Microsoft SQL, Couchbase |
| Programming & AI | Go, Python, Bash, AI, MCP |

#### Previous impact within the same company

*   Led the automated deployment of VMs and applications through CI/CD, enabling multiple deployments per day.
*   Used Terraform to deploy across 10 datacenters and 4 providers (OpenStack, Proxmox, vSphere, NetBox) from shared templates.
*   Used Ansible for VM initialization and application deployment, with Consul feeding service pools for HAProxy and Prometheus.
*   Implemented and operated a large Elastic Stack platform handling 200 TB of logs across 10 nodes with Kafka for SIEM, logging, EDR, APM, and uptime monitoring.
*   Integrated a highly available Proxmox cluster across 4 racks and 2 datacenters with Ceph, including PXE-based automation and 25 Gb networking per host.
*   Accountable for the French security scope, driving remediation work for vulnerabilities and production hardening.

### <a href="https://www.vinc.fr/"><img src="/img/Vinc.png" alt="VINC" style="height: 30px; padding-right: 10px; vertical-align: middle;"></a> VINC | System engineer | 2019 - 2021

<div class="skills-container">
    <a href="/tags/proxmox" class="skill-badge">Proxmox</a>
    <a href="/tags/dns" class="skill-badge">DNS</a>
    <a href="/tags/ha" class="skill-badge">High Availability</a>
</div>

*   Archictured the new plateform with new BGP routers and Firewalls
*   Managed Proxmox cluster arround 2 datacenters
*   Responsible for SLA and communication with clients for production accident
*   Implementation of websites arround client needs
*   Implemented a new DNS stack with high availability in mind

### Multi-Visp / Azuria | System administrator | 2017 - 2019

<div class="skills-container">
    <a href="/tags/network" class="skill-badge">Network Infrastructure</a>
    <a href="/tags/vpn" class="skill-badge">VPN</a>
    <a href="/tags/datacenter" class="skill-badge">Datacenter Management</a>
    <a href="/tags/wifi" class="skill-badge">WiFi</a>
</div>

*   Installed complete new racks in Telehouse2
*   Cable management between two rooms
*   Installed managed wifi equipmenents
*   Implemented high availability multi datacenter VPN services

### Education

**Louis Armand | BAC**

*   Learned the basics of
    *   Networking
    *   Firewalling
    *   Electricity


**Louis Armand | BTS**

*   Learned basics of
    *   Algorithm with Python
    *   Web development with PHP
    *   Distributed Storage
    *   Routing with OSPF

**ESGI | Master degree**

*   As my degree project
    *  Deployed an Elastic Stack with ML
    *  Auto detect anomaly with JA3 Signature
    *  Import JA3er database to automaticaly ban from JunOS Router L3
    *  Dynamicaly rate limit / block traffic at L7

### Personal Website | Developed a personal website to showcase my skills and experience | Hugo, HTML, CSS, JavaScript

*   Designed and developed a responsive website using Hugo, HTML, CSS, and JavaScript.
*   Implemented a blog to share my thoughts on software development and technology.

## Contact Information

*   Email: contact@smjed.net
