---
title: "My Resume"
type: "resume"
description: "Senior freelance SRE with 10 years of experience across observability, Kubernetes, Proxmox/Ceph, automation, and AI-assisted SRE tooling."
---

## Summary

> Senior freelance <span class="key">SRE</span> with <span class="key">10 years</span> of experience operating infrastructure that can't quietly fail. I work across high-volume observability, <span class="key">Kubernetes</span> platform engineering, on-prem <span class="key">Proxmox/Ceph</span> clusters, and AI-assisted SRE tooling.

<div class="cv-downloads">
  <a href="/files/sabri-mjahed-cv-en.pdf" download>Download CV PDF - English</a>
  <a href="/files/sabri-mjahed-cv-fr.pdf" download>Download CV PDF - French</a>
</div>

## Open Source Contributions

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

*   Progressed from System Engineer to Site Reliability Engineer, shifting focus from infrastructure automation toward platform reliability, observability, diagnostics and performance.
*   Operate observability workflows around Kubernetes with Thanos, Loki, Grafana, and Vector as core technologies.
*   Built a HouseKeeping tool to diagnose stale and broken Grafana resources, reducing dashboard/config drift and improving platform hygiene.
*   Built a Search Query Exporter to diagnose query slowness and establish SLOs across Thanos and Loki.
*   Designed an SLO Dashboard Framework to standardize service-level visibility and make reliability reporting easier to adopt across teams.
*   Building Graphia, a domain-specific SRE agent for Grafana diagnosis - RBAC-aware behavior, MCP-based diagnosis flows, and safeguards for enterprise operations.
*   Daily hands-on work with Helm charts, Argo CD, container image lifecycle, Jenkins, GitLab, AWS CloudWatch, and CUR2 cost analysis.

#### Current stack and ownership

| Area | Components/Tools |
|------|------------------|
| Observability | Grafana, Loki, Thanos, Vector, AWS CloudWatch |
| Platform Engineering | Kubernetes, Helm, Argo CD, Container Images |
| CI/CD & Automation | Jenkins, GitLab CI, Terraform, Ansible |
| Data & Storage | Kafka, Redis, PostgreSQL, Microsoft SQL, Couchbase |
| Programming & AI | Go, Python, Bash, AI, MCP |

#### Previous impact within the same company

*   Led the automated deployment of VMs and applications through CI/CD, enabling multiple deployments per day.
*   Used Terraform to deploy across 10 datacenters and 4 providers (OpenStack, Proxmox, vSphere, NetBox) from shared templates.
*   Used Ansible for VM initialization and application deployment, with Consul feeding service pools for HAProxy and Prometheus.
*   Operated multi-cluster observability at <span class="key">multi-TB/day</span> ingestion across logs, metrics, and traces, with <span class="key">Kafka</span> pipelines feeding SIEM, logging, EDR, APM, and uptime monitoring.
*   Integrated a highly available Proxmox cluster across 4 racks and 2 datacenters with Ceph, including PXE-based automation and 25 Gb networking per host.
*   Accountable for the French security scope, driving remediation work for vulnerabilities and production hardening.

### <a href="https://www.vinc.fr/"><img src="/img/Vinc.png" alt="VINC" style="height: 30px; padding-right: 10px; vertical-align: middle;"></a> VINC | System engineer | 2019 - 2021

<div class="skills-container">
    <a href="/tags/proxmox" class="skill-badge">Proxmox</a>
    <a href="/tags/dns" class="skill-badge">DNS</a>
    <a href="/tags/ha" class="skill-badge">High Availability</a>
</div>

*   Architected the new platform with new BGP routers and firewalls.
*   Managed Proxmox cluster across 2 datacenters.
*   Responsible for SLA and client communication during production incidents.
*   Implemented websites around client needs.
*   Implemented a new DNS stack with high availability in mind.

### Multi-Visp / Azuria | System administrator | 2017 - 2019

<div class="skills-container">
    <a href="/tags/network" class="skill-badge">Network Infrastructure</a>
    <a href="/tags/vpn" class="skill-badge">VPN</a>
    <a href="/tags/datacenter" class="skill-badge">Datacenter Management</a>
    <a href="/tags/wifi" class="skill-badge">WiFi</a>
</div>

*   Installed complete new racks in Telehouse2.
*   Cable management between two rooms.
*   Installed managed Wi-Fi equipment.
*   Implemented high-availability multi-datacenter VPN services.

## Contact Information

*   Email: contact@smjed.net
