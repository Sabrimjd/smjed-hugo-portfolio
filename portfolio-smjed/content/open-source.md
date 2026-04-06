---
title: "Open Source"
aliases: ["opensource"]
draft: false
---

<style>
  .oss-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }

  .oss-card {
    position: relative;
    border: 1px solid rgba(120, 120, 120, 0.25);
    border-radius: 14px;
    overflow: hidden;
    background: rgba(120, 120, 120, 0.06);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.08);
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    cursor: pointer;
  }

  .oss-card:hover,
  .oss-card:focus-within {
    transform: translateY(-4px);
    box-shadow: 0 24px 48px rgba(0, 0, 0, 0.14);
    border-color: rgba(120, 120, 120, 0.4);
  }

  .oss-card__overlay {
    position: absolute;
    inset: 0;
    z-index: 1;
  }

  .oss-card img {
    display: block;
    width: 100%;
    aspect-ratio: 16 / 10;
    object-fit: cover;
    background: #0f1115;
  }

  .oss-card__body {
    padding: 1.1rem 1.15rem 1.2rem;
  }

  .oss-card__body h3 {
    margin: 0 0 0.5rem;
  }

  .oss-card__body p {
    margin: 0 0 0.85rem;
    line-height: 1.6;
  }

  .oss-card__body ul {
    margin: 0 0 1rem 1.15rem;
  }

  .oss-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 0 0 0.9rem;
  }

  .oss-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.22rem 0.55rem;
    border-radius: 999px;
    border: 1px solid rgba(120, 120, 120, 0.24);
    background: rgba(120, 120, 120, 0.1);
    font-size: 0.78rem;
    line-height: 1.1;
    white-space: nowrap;
  }

  .oss-card__links {
    position: relative;
    z-index: 2;
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
  }

  .oss-card__links a {
    text-decoration: none;
  }

  .oss-mini-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0 2rem;
  }

  .oss-mini-card {
    position: relative;
    border: 1px solid rgba(120, 120, 120, 0.22);
    border-radius: 12px;
    padding: 1rem;
    background: rgba(120, 120, 120, 0.04);
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    cursor: pointer;
  }

  .oss-mini-card:hover,
  .oss-mini-card:focus-within {
    transform: translateY(-3px);
    box-shadow: 0 16px 32px rgba(0, 0, 0, 0.12);
    border-color: rgba(120, 120, 120, 0.35);
  }

  .oss-mini-card__overlay {
    position: absolute;
    inset: 0;
    z-index: 1;
  }

  .oss-mini-card h3 {
    margin: 0 0 0.45rem;
    font-size: 1rem;
  }

  .oss-mini-card p {
    margin: 0 0 0.8rem;
    line-height: 1.55;
    font-size: 0.96rem;
  }

  .oss-mini-card a:not(.oss-mini-card__overlay) {
    position: relative;
    z-index: 2;
  }
</style>

I treat open source as an extension of my SRE and platform engineering work: build tools around real operational pain points, keep them practical, and make them useful beyond my own environment.

<div class="oss-grid">
  <article class="oss-card">
    <a class="oss-card__overlay" href="https://github.com/Sabrimjd/SSHPlex" target="_blank" rel="noopener" aria-label="Open SSHplex on GitHub"></a>
    <img src="https://raw.githubusercontent.com/Sabrimjd/SSHPlex/main/demo/demo.gif" alt="SSHplex demo" />
    <div class="oss-card__body">
      <h3>SSHplex</h3>
      <div class="oss-badges">
        <span class="oss-badge">Python</span>
        <span class="oss-badge">TUI</span>
        <span class="oss-badge">SSH</span>
        <span class="oss-badge">NetBox</span>
        <span class="oss-badge">Consul</span>
      </div>
      <p>Modern SSH connection multiplexing for infrastructure teams that need to move quickly across large fleets.</p>
      <ul>
        <li>Multi-source inventory from NetBox, Ansible, Consul, and static lists</li>
        <li>Broadcast commands and persistent sessions</li>
        <li>Three mux backends: tmux standalone, tmux + iTerm2, and native iTerm2 on macOS</li>
      </ul>
      <div class="oss-card__links">
        <a href="https://github.com/Sabrimjd/SSHPlex" target="_blank" rel="noopener">GitHub</a>
        <a href="/posts/building_sshplex/">Blog post</a>
      </div>
    </div>
  </article>

  <article class="oss-card">
    <a class="oss-card__overlay" href="https://github.com/Sabrimjd/openclaw-audit-tui" target="_blank" rel="noopener" aria-label="Open OpenClaw Audit TUI on GitHub"></a>
    <img src="https://raw.githubusercontent.com/Sabrimjd/openclaw-audit-tui/main/screenshots/screenshot3.png" alt="OpenClaw Audit TUI screenshot" />
    <div class="oss-card__body">
      <h3>OpenClaw Audit TUI</h3>
      <div class="oss-badges">
        <span class="oss-badge">TypeScript</span>
        <span class="oss-badge">Audit</span>
        <span class="oss-badge">TUI</span>
        <span class="oss-badge">OpenClaw</span>
        <span class="oss-badge">Observability</span>
      </div>
      <p>Terminal UI for auditing OpenClaw sessions, tool usage, model behavior, and live events.</p>
      <ul>
        <li>Global timeline, tree view, and rich session inspection</li>
        <li>Advanced filters for events, tools, roles, and errors</li>
        <li>Real-time streaming to channels like Discord, Telegram, and Slack</li>
      </ul>
      <div class="oss-card__links">
        <a href="https://github.com/Sabrimjd/openclaw-audit-tui" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </article>

  <article class="oss-card">
    <a class="oss-card__overlay" href="https://github.com/Sabrimjd/hypr-codexbar" target="_blank" rel="noopener" aria-label="Open Hypr CodexBar on GitHub"></a>
    <img src="https://raw.githubusercontent.com/Sabrimjd/hypr-codexbar/master/assets/waybar-tooltip.png" alt="Hypr CodexBar screenshot" />
    <div class="oss-card__body">
      <h3>Hypr CodexBar</h3>
      <div class="oss-badges">
        <span class="oss-badge">Shell</span>
        <span class="oss-badge">Waybar</span>
        <span class="oss-badge">Hyprland</span>
        <span class="oss-badge">CLI</span>
        <span class="oss-badge">Developer UX</span>
      </div>
      <p>Small Waybar module for Hyprland and Omarchy that makes Codex usage windows readable at a glance.</p>
      <ul>
        <li>5-hour and weekly usage tracking with reserve pace</li>
        <li>Review usage, tooltips, threshold notifications, and cache fallback</li>
        <li>Built for lightweight developer observability directly from the desktop bar</li>
      </ul>
      <div class="oss-card__links">
        <a href="https://github.com/Sabrimjd/hypr-codexbar" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </article>
</div>

## More Projects

<div class="oss-mini-grid">
  <article class="oss-mini-card">
    <a class="oss-mini-card__overlay" href="https://github.com/Sabrimjd/openclaw-session-audit" target="_blank" rel="noopener" aria-label="Open openclaw-session-audit on GitHub"></a>
    <h3>openclaw-session-audit</h3>
    <p>Monitor OpenClaw sessions and stream events to any channel for audit visibility beyond the terminal.</p>
    <div class="oss-badges">
      <span class="oss-badge">TypeScript</span>
      <span class="oss-badge">Audit</span>
      <span class="oss-badge">Streaming</span>
    </div>
    <a href="https://github.com/Sabrimjd/openclaw-session-audit" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <a class="oss-mini-card__overlay" href="https://github.com/Sabrimjd/discord-audit-stream" target="_blank" rel="noopener" aria-label="Open discord-audit-stream on GitHub"></a>
    <h3>discord-audit-stream</h3>
    <p>Discord audit stream hook for OpenClaw that monitors session files and pushes all events into a chat workflow.</p>
    <div class="oss-badges">
      <span class="oss-badge">TypeScript</span>
      <span class="oss-badge">Discord</span>
      <span class="oss-badge">Hooks</span>
    </div>
    <a href="https://github.com/Sabrimjd/discord-audit-stream" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <a class="oss-mini-card__overlay" href="https://github.com/Sabrimjd/terraform-provider-centreon" target="_blank" rel="noopener" aria-label="Open terraform-provider-centreon on GitHub"></a>
    <h3>terraform-provider-centreon</h3>
    <p>A Go-based Terraform provider for Centreon API V2 that turns monitoring configuration into infrastructure as code.</p>
    <div class="oss-badges">
      <span class="oss-badge">Go</span>
      <span class="oss-badge">Terraform</span>
      <span class="oss-badge">Monitoring</span>
    </div>
    <a href="https://github.com/Sabrimjd/terraform-provider-centreon" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <a class="oss-mini-card__overlay" href="https://github.com/Sabrimjd/Proton-Email-Migration-Tracker" target="_blank" rel="noopener" aria-label="Open Proton-Email-Migration-Tracker on GitHub"></a>
    <h3>Proton-Email-Migration-Tracker</h3>
    <p>A personal migration helper for tracking Gmail to ProtonMail progress with categorization and workflow visibility.</p>
    <div class="oss-badges">
      <span class="oss-badge">TypeScript</span>
      <span class="oss-badge">Email</span>
      <span class="oss-badge">Web UI</span>
    </div>
    <a href="https://github.com/Sabrimjd/Proton-Email-Migration-Tracker" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <a class="oss-mini-card__overlay" href="https://github.com/Sabrimjd/bayes-hmailserver" target="_blank" rel="noopener" aria-label="Open bayes-hmailserver on GitHub"></a>
    <h3>bayes-hmailserver</h3>
    <p>Bayesian auto-learning for hMailServer, built around a practical mail filtering and automation use case.</p>
    <div class="oss-badges">
      <span class="oss-badge">Python</span>
      <span class="oss-badge">Mail</span>
      <span class="oss-badge">Automation</span>
    </div>
    <a href="https://github.com/Sabrimjd/bayes-hmailserver" target="_blank" rel="noopener">GitHub</a>
  </article>
</div>

## How I approach open source

- Start from a real operational or workflow problem
- Prefer tools that stay fast, inspectable, and easy to operate
- Keep the UX practical for engineers who live in the terminal
- Use open source projects to sharpen reliability, observability, and developer tooling skills

You can browse more of my public work on [my GitHub repositories](https://github.com/Sabrimjd?tab=repositories).
