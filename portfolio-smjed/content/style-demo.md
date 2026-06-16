---
title: "Style Demo"
date: "2026-06-16"
draft: true
---

## Lead Paragraph

<p class="lead">I operated multi-cluster observability at multi-TB/day ingestion across logs, metrics, and traces, with Kafka pipelines feeding SIEM, logging, EDR, APM, and uptime monitoring.</p>

This is what a big punchy intro looks like. It's larger, heavier, and pulls the eye immediately. Use it once at the top of a section or blog post.

## Key Terms Inline

The stack I operated daily: <span class="key">Loki</span> for logs, <span class="key">Thanos</span> for long-term metrics, <span class="key">Grafana</span> for visualization, and <span class="key">Kafka</span> as the ingestion backbone.

You can use this to highlight technologies or concepts that matter in a sentence without bolding everything.

## Big Stat Number

<span class="stat-big">8 TB/day</span>

<p class="lead">Ingestion across 3 clusters, 10 datacenters.</p>

This is useful in blog posts when you want a metric to hit hard. Pair it with a .lead line below for context.

## Callout (Warning)

<div class="callout">
<strong>War story.</strong> We inherited a Loki stack that was silently dropping 15% of log lines due to misconfigured chunk limits. Fixing it recovered 6 months of "lost" observability data.
</div>

Use <code>.callout</code> for war stories, lessons learned, or things that went wrong and how you fixed them. Amber left border, soft tint.

## Note (Info)

<div class="note">
<strong>Architecture.</strong> The Proxmox cluster used Ceph with 3 replicas across 4 racks. Network was 25Gb/host with jumbo frames. PXE boot automated all node provisioning.
</div>

Use <code>.note</code> for technical context or architecture details. Blue left border, soft tint.

## Combined Example (Blog Post Snippet)

<p class="lead">When I joined, the platform was ingesting <strong>2 TB/day</strong> across a single Elastic cluster with no retention strategy. Dashboards took 30+ seconds to load. SLOs didn't exist.</p>

The target: <span class="key">3x ingestion capacity</span>, sub-second query performance, and SLO coverage for 40+ services.

The stack I built:

- <span class="key">Loki</span> replaced Elasticsearch for log storage (10x cheaper at this scale)
- <span class="key">Thanos</span> for long-term Prometheus metrics with S3-backed storage
- <span class="key">Vector</span> as the ingestion layer, replacing Logstash
- <span class="key">Grafana</span> as the unified query layer with RBAC and SSO

<div class="callout">
<strong>Result.</strong> The migration cut infrastructure costs by 60% while tripling ingestion capacity. Query p99 dropped from 12 seconds to under 1 second.
</div>

<span class="stat-big">3x capacity · 60% cheaper · 12x faster</span>

## Inline Code

The config used `replication_factor: 3` with `min_size: 2` for quorum. Each OSD ran on a dedicated NVMe with `osd_op_threads: 32`.

## Standard Bold vs Key Term

This is **bold text** in a sentence.

This is <span class="key">key term</span> in a sentence.

Bold is for emphasis within your own voice. Key term is for technologies, metrics, or concepts you want the reader to scan for quickly.
