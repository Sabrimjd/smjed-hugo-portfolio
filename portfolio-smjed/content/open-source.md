---
title: "Open Source"
aliases: ["opensource"]
draft: false
---

I treat open source as an extension of my SRE and platform engineering work: build tools around real operational pain points, keep them practical, and make them useful beyond my own environment.

## Featured Projects

### SSHplex

Modern SSH connection multiplexing for infrastructure teams that need to move quickly across large fleets.

- GitHub: [SSHPlex](https://github.com/Sabrimjd/SSHPlex)
- Blog post: [Building SSHplex](/posts/building_sshplex/)
- Problem solved: expensive legacy remote access workflows and too much manual host management
- Key capabilities: multi-source inventory from NetBox, Ansible, Consul, and static lists; broadcast commands; persistent sessions
- Mux backends: tmux standalone, tmux + iTerm2, and native iTerm2 on macOS
- Tech focus: Python, Textual, tmux, iTerm2, CI/CD, packaging

### OpenClaw Audit TUI

Terminal UI for auditing OpenClaw sessions, tool usage, model behavior, and live events.

- GitHub: [openclaw-audit-tui](https://github.com/Sabrimjd/openclaw-audit-tui)
- Problem solved: poor visibility into agent activity, session events, and audit trails
- Key capabilities: global timeline, tree view, rich session inspection, advanced filters, and real-time streaming to channels like Discord, Telegram, or Slack
- Tech focus: OpenTUI React, terminal UX, event auditing, real-time operations visibility

### Hypr CodexBar

Small Waybar module for Hyprland and Omarchy that makes Codex usage windows readable at a glance.

- GitHub: [hypr-codexbar](https://github.com/Sabrimjd/hypr-codexbar)
- Problem solved: hard-to-track usage windows and pacing during day-to-day development
- Key capabilities: 5-hour and weekly usage tracking, reserve pace, review usage, tooltips, threshold notifications, and cache fallback
- Tech focus: shell tooling, Waybar integration, CLI-driven observability, lightweight desktop workflow improvements

## How I approach open source

- Start from a real operational or workflow problem
- Prefer tools that stay fast, inspectable, and easy to operate
- Keep the UX practical for engineers who live in the terminal
- Use open source projects to sharpen reliability, observability, and developer tooling skills
