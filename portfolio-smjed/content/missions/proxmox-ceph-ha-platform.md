---
title: "Proxmox / Ceph HA Platform"
subtitle: "Enterprise-grade virtualization on bare metal, without the VMware tax."
description: "Design and deployment of Proxmox HA clusters with PXE automation, multi-backend storage, and migration from legacy hypervisors."
accent: "amber"
weight: 3
duration: "3-6 weeks"
format: "On-site preferred"
pricing: "650 EUR/day"
stack: ["Proxmox", "Ceph", "PXE", "ZFS", "NVMe-oF", "HAProxy", "Corosync"]
ideal_for: "Teams migrating away from VMware/vSphere, or organizations building new on-prem virtualization that needs real HA without licensing a commercial hypervisor."
scope:
  - "**Architecture design**: cluster sizing, Ceph topology (replication/erasure coding), network plane separation, LACP/EVPN/VPC"
  - "**Proxmox cluster setup**: Corosync configuration, quorum tuning, live migration, HA groups and fencing"
  - "**Storage backends**: ZFS, NFS, SAN, NVMe over Fabric, Ceph (managed by Proxmox or cephadm)"
  - "**PXE automation**: bare-metal provisioning pipeline for rapid node deployment and replacement"
  - "**Backup strategy**: Proxmox Backup Server integration, snapshot scheduling, off-site replication"
  - "**Migration execution**: planned VM migration from vSphere with minimal downtime, or Proxmox version upgrades"
deliverables:
  - "Production Proxmox HA cluster with verified failover testing"
  - "PXE boot infrastructure for zero-touch node provisioning"
  - "Documented network architecture with VLAN map and switch configuration"
  - "Backup and recovery runbook with tested restore procedures"
  - "Storage performance baseline report per backend (IOPS, throughput, latency)"
  - "Operational runbook covering common maintenance and failure scenarios"
draft: false
---

VMware licensing changes pushed a lot of teams to look for alternatives. Proxmox is the answer, but a Proxmox cluster that survives real failure scenarios needs proper Ceph design, network segmentation, quorum tuning, and automated provisioning.

I deployed 100+ Proxmox nodes with PXE automation across every storage backend: ZFS, NFS, SAN, NVMe over Fabric, and Ceph. I led vSphere-to-Proxmox migrations (Pure Storage SAN, NVMe-oF, MultipathD), Proxmox 4-to-8 upgrades with near-zero downtime using NFS buffer, and designed HA architectures with LACP/EVPN/VPC.

This mission brings that operational depth to your deployment.
