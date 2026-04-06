---
title: "Open Source"
aliases: ["opensource"]
draft: false
---

Je vois l'open source comme une extension directe de mon travail en SRE et en ingenierie de plateforme : partir de vrais problemes operationnels, construire des outils concrets, puis les rendre utiles au-dela de mon propre contexte.

## Projets mis en avant

### SSHplex

Un outil moderne de multiplexage de connexions SSH pour les equipes infrastructure qui doivent agir vite sur un grand nombre d'hotes.

- GitHub : [SSHPlex](https://github.com/Sabrimjd/SSHPlex)
- Article : [Building SSHplex](/posts/building_sshplex/)
- Probleme adresse : des workflows d'acces distant historiques couteux et trop de gestion manuelle des hotes
- Fonctionnalites cles : inventaire multi-sources via NetBox, Ansible, Consul et listes statiques ; broadcast de commandes ; sessions persistantes
- Modes de multiplexage : tmux standalone, tmux + iTerm2 et iTerm2 natif sur macOS
- Focus technique : Python, Textual, tmux, iTerm2, CI/CD, packaging

### OpenClaw Audit TUI

Une interface terminal dediee a l'audit des sessions OpenClaw, a l'usage des outils, au comportement des modeles et aux evenements en direct.

- GitHub : [openclaw-audit-tui](https://github.com/Sabrimjd/openclaw-audit-tui)
- Probleme adresse : un manque de visibilite sur l'activite des agents, les evenements de session et les traces d'audit
- Fonctionnalites cles : timeline globale, vue arborescente, inspection detaillee des sessions, filtres avances et diffusion temps reel vers Discord, Telegram ou Slack
- Focus technique : OpenTUI React, UX terminal, audit d'evenements, visibilite temps reel pour les operations

### Hypr CodexBar

Un petit module Waybar pour Hyprland et Omarchy qui rend les fenetres d'usage Codex lisibles en un coup d'oeil.

- GitHub : [hypr-codexbar](https://github.com/Sabrimjd/hypr-codexbar)
- Probleme adresse : des fenetres d'usage et un rythme de consommation difficiles a suivre au quotidien
- Fonctionnalites cles : suivi sur 5 heures et a la semaine, reserve pace, usage review, tooltips, notifications de seuil et fallback sur cache
- Focus technique : outillage shell, integration Waybar, observabilite orientee CLI, amelioration legere des workflows desktop

## Ma facon d'aborder l'open source

- Partir d'un probleme operationnel ou d'un irritant concret
- Privilegier des outils rapides, lisibles et faciles a exploiter
- Garder une experience pratique pour les ingenieurs qui vivent dans le terminal
- Utiliser ces projets pour renforcer mes competences en fiabilite, observabilite et outillage developpeur
