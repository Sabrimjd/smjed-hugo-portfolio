---
title: "Proxmox / Ceph HA Platform"
subtitle: "Enterprise-grade virtualization and distributed storage on bare metal, without the VMware tax."
description: "Design and deployment of Proxmox clusters with Ceph storage, HA, and PXE automation."
accent: "amber"
weight: 3
duration: "3-6 weeks"
format: "On-site preferred"
pricing: "650 EUR/day"
stack: ["Proxmox", "Ceph", "PXE", "HAProxy", "Keepalived", "ZFS", "Corosync"]
ideal_for: "Teams migrating away from VMware/vSphere, or organizations building new on-prem virtualization that needs real HA without licensing a commercial hypervisor."
scope:
  - "**Architecture design**: cluster sizing, Ceph topology (replication/erasure coding), network plane separation"
  - "**Proxmox cluster setup**: Corosync configuration, quorum tuning, live migration, HA groups and fencing"
  - "**Ceph deployment**: OSD layout, pool design, PG sizing, CRUSH map tuning, bluestore configuration"
  - "**Network design**: dedicated storage network, bonding, jumbo frames, MTU verification"
  - "**PXE automation**: bare-metal provisioning pipeline for rapid node deployment and replacement"
  - "**Backup strategy**: Proxmox Backup Server integration, snapshot scheduling, off-site replication"
  - "**Migration execution**: planned VM migration from vSphere/legacy hypervisors with minimal downtime"
deliverables:
  - "Production Proxmox/Ceph HA cluster with verified failover testing"
  - "PXE boot infrastructure for zero-touch node provisioning"
  - "Documented network architecture with VLAN map and switch configuration"
  - "Backup and recovery runbook with tested restore procedures"
  - "Ceph performance baseline report (IOPS, throughput, latency under load)"
  - "Operational runbook covering common maintenance and failure scenarios"
draft: false
---

VMware licensing changes pushed a lot of teams to look for alternatives. Proxmox is the answer, but a Proxmox cluster that survives real failure scenarios needs proper Ceph design, network segmentation, quorum tuning, and automated provisioning. A default install will not cut it.

This mission delivers a production Proxmox/Ceph platform: HA-configured, properly networked, PXE-automated, and documented well enough for your team to operate independently.
