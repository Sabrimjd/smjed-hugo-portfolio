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
    border: 1px solid rgba(120, 120, 120, 0.25);
    border-radius: 14px;
    overflow: hidden;
    background: rgba(120, 120, 120, 0.06);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.08);
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
    border: 1px solid rgba(120, 120, 120, 0.22);
    border-radius: 12px;
    padding: 1rem;
    background: rgba(120, 120, 120, 0.04);
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
</style>

Je vois l'open source comme une extension directe de mon travail en ingenierie SRE et plateforme : partir de vrais problemes operationnels, construire des outils concrets, puis les rendre utiles au-dela de mon propre contexte.

<div class="oss-grid">
  <article class="oss-card">
    <img src="https://raw.githubusercontent.com/Sabrimjd/SSHPlex/main/demo/demo.gif" alt="Demo SSHplex" />
    <div class="oss-card__body">
      <h3>SSHplex</h3>
      <div class="oss-badges">
        <span class="oss-badge">Python</span>
        <span class="oss-badge">TUI</span>
        <span class="oss-badge">SSH</span>
        <span class="oss-badge">NetBox</span>
        <span class="oss-badge">Consul</span>
      </div>
      <p>Un outil moderne de multiplexage de connexions SSH pour les equipes infrastructure qui doivent agir vite sur un grand nombre d'hotes.</p>
      <ul>
        <li>Inventaire multi-sources via NetBox, Ansible, Consul et listes statiques</li>
        <li>Broadcast de commandes et sessions persistantes</li>
        <li>Trois modes de multiplexage : tmux standalone, tmux + iTerm2 et iTerm2 natif sur macOS</li>
      </ul>
      <div class="oss-card__links">
        <a href="https://github.com/Sabrimjd/SSHPlex" target="_blank" rel="noopener">GitHub</a>
        <a href="/posts/building_sshplex/">Article</a>
      </div>
    </div>
  </article>

  <article class="oss-card">
    <img src="https://raw.githubusercontent.com/Sabrimjd/openclaw-audit-tui/main/screenshots/screenshot3.png" alt="Capture OpenClaw Audit TUI" />
    <div class="oss-card__body">
      <h3>OpenClaw Audit TUI</h3>
      <div class="oss-badges">
        <span class="oss-badge">TypeScript</span>
        <span class="oss-badge">Audit</span>
        <span class="oss-badge">TUI</span>
        <span class="oss-badge">OpenClaw</span>
        <span class="oss-badge">Observabilite</span>
      </div>
      <p>Une interface terminal dediee a l'audit des sessions OpenClaw, a l'usage des outils, au comportement des modeles et aux evenements en direct.</p>
      <ul>
        <li>Timeline globale, vue arborescente et inspection detaillee des sessions</li>
        <li>Filtres avances sur les evenements, les outils, les roles et les erreurs</li>
        <li>Diffusion temps reel vers Discord, Telegram, Slack et autres canaux</li>
      </ul>
      <div class="oss-card__links">
        <a href="https://github.com/Sabrimjd/openclaw-audit-tui" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </article>

  <article class="oss-card">
    <img src="https://raw.githubusercontent.com/Sabrimjd/hypr-codexbar/master/assets/waybar-tooltip.png" alt="Capture Hypr CodexBar" />
    <div class="oss-card__body">
      <h3>Hypr CodexBar</h3>
      <div class="oss-badges">
        <span class="oss-badge">Shell</span>
        <span class="oss-badge">Waybar</span>
        <span class="oss-badge">Hyprland</span>
        <span class="oss-badge">CLI</span>
        <span class="oss-badge">Dev UX</span>
      </div>
      <p>Un petit module Waybar pour Hyprland et Omarchy qui rend les fenetres d'usage Codex lisibles en un coup d'oeil.</p>
      <ul>
        <li>Suivi sur 5 heures et a la semaine avec reserve pace</li>
        <li>Usage review, tooltips, notifications de seuil et fallback sur cache</li>
        <li>Une approche legere pour rendre l'usage developpeur plus observable depuis le desktop</li>
      </ul>
      <div class="oss-card__links">
        <a href="https://github.com/Sabrimjd/hypr-codexbar" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </article>
</div>

## Autres projets

<div class="oss-mini-grid">
  <article class="oss-mini-card">
    <h3>openclaw-session-audit</h3>
    <p>Surveille les sessions OpenClaw et diffuse les evenements vers n'importe quel canal pour sortir l'audit du terminal.</p>
    <div class="oss-badges">
      <span class="oss-badge">TypeScript</span>
      <span class="oss-badge">Audit</span>
      <span class="oss-badge">Streaming</span>
    </div>
    <a href="https://github.com/Sabrimjd/openclaw-session-audit" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <h3>discord-audit-stream</h3>
    <p>Un hook Discord pour OpenClaw qui surveille les fichiers de session et envoie tous les evenements dans un workflow de discussion.</p>
    <div class="oss-badges">
      <span class="oss-badge">TypeScript</span>
      <span class="oss-badge">Discord</span>
      <span class="oss-badge">Hooks</span>
    </div>
    <a href="https://github.com/Sabrimjd/discord-audit-stream" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <h3>terraform-provider-centreon</h3>
    <p>Un provider Terraform en Go pour l'API Centreon V2 afin de gerer la configuration de monitoring comme du code.</p>
    <div class="oss-badges">
      <span class="oss-badge">Go</span>
      <span class="oss-badge">Terraform</span>
      <span class="oss-badge">Monitoring</span>
    </div>
    <a href="https://github.com/Sabrimjd/terraform-provider-centreon" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <h3>Proton-Email-Migration-Tracker</h3>
    <p>Un outil personnel pour suivre une migration Gmail vers ProtonMail avec categorisation et visibilite sur l'avancement.</p>
    <div class="oss-badges">
      <span class="oss-badge">TypeScript</span>
      <span class="oss-badge">Email</span>
      <span class="oss-badge">Web UI</span>
    </div>
    <a href="https://github.com/Sabrimjd/Proton-Email-Migration-Tracker" target="_blank" rel="noopener">GitHub</a>
  </article>

  <article class="oss-mini-card">
    <h3>bayes-hmailserver</h3>
    <p>Un projet d'auto-apprentissage bayesien pour hMailServer, construit autour d'un cas concret de filtrage mail et d'automatisation.</p>
    <div class="oss-badges">
      <span class="oss-badge">Python</span>
      <span class="oss-badge">Mail</span>
      <span class="oss-badge">Automation</span>
    </div>
    <a href="https://github.com/Sabrimjd/bayes-hmailserver" target="_blank" rel="noopener">GitHub</a>
  </article>
</div>

## Ma facon d'aborder l'open source

- Partir d'un probleme operationnel ou d'un irritant concret
- Privilegier des outils rapides, lisibles et faciles a exploiter
- Garder une experience pratique pour les ingenieurs qui vivent dans le terminal
- Utiliser ces projets pour renforcer mes competences en fiabilite, observabilite et outillage developpeur

Vous pouvez voir davantage de projets publics sur [mes depots GitHub](https://github.com/Sabrimjd?tab=repositories).
