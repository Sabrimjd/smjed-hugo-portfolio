---
title: "VM Migration Factory"
subtitle: "Git push to live traffic, zero manual steps. The orchestration pipeline I built when we didn't have Kubernetes."
description: "Autonomous VM delivery pipeline across vSphere, Proxmox, and OpenStack with Consul, NetBox, Ansible, and Centreon."
accent: "green"
weight: 2
duration: "3-6 weeks"
format: "Remote or on-site"
pricing: "650 EUR/day"
stack: ["Terraform", "Ansible", "Consul", "NetBox", "Jenkins", "HAProxy", "Centreon"]
ideal_for: "Teams operating hundreds of VMs across multiple providers or datacenters who are tired of manual provisioning, inconsistent configuration, and migration projects that never end."
scope:
  - "**Pipeline design**: Git-triggered Terraform plan/apply across multiple providers with shared variable files (~80% common, ~20% provider-specific)"
  - "**Dynamic inventory**: Consul and NetBox as source of truth, new VMs auto-register on creation"
  - "**Automated configuration**: Ansible meta-playbook discovers unconfigured VMs via NetBox custom fields, runs the right playbook, marks as configured"
  - "**Traffic cutover**: HAProxy backends auto-register via Consul service discovery, new VMs receive traffic without manual intervention"
  - "**Monitoring integration**: Automatic registration into your monitoring stack (Centreon, Prometheus, or equivalent)"
  - "**Migration execution**: Planned VM migrations from vSphere, Proxmox upgrades, or cross-DC moves with minimal downtime"
deliverables:
  - "Fully functional Git-to-live-traffic VM delivery pipeline"
  - "Terraform multi-provider module templates (vSphere, Proxmox, OpenStack)"
  - "Ansible dynamic inventory integration with NetBox custom fields"
  - "HAProxy or load balancer auto-registration via Consul"
  - "Operational runbook for adding new VM types and providers"
  - "Migration playbook template for existing fleet"
draft: false
---

Most teams operating hundreds of VMs do it manually: ticket, provision, configure, register, repeat. Every VM is slightly different. Every migration is a project. Every provider has its own quirks that someone has to remember.

This mission replaces that with a pipeline. I built this exact system to manage 3000+ VMs across 4 providers and 10 datacenters, without Kubernetes. You open a PR with a tfvars file, merge it, and the VM goes from nothing to configured, monitored, and receiving traffic.

The key insight: you don't need Kubernetes to have orchestration. You need Git as the control plane, Terraform as the provisioner, Consul/NetBox as the source of truth, and Ansible as the configurator. Wire them together with the right metadata and the pipeline runs itself.
