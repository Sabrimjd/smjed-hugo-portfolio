---
title: "Mon CV"
type: "resume"
---

## Résumé

> Je suis un Site Reliability Engineer avec une solide expérience DevOps, centré sur les plateformes Kubernetes, l'observabilité, l'automatisation et la construction de systèmes fiables qui permettent aux équipes d'aller vite sans perdre en maîtrise opérationnelle.

## Contributions Open Source

🌟 **SSHplex**
> Développement et maintenance d'une interface terminal open source dédiée au multiplexage de connexions SSH, pensée pour les équipes infrastructure qui ont besoin de découverte rapide des hôtes, d'opérations en masse et de sessions persistantes.
- Dépôt GitHub : [SSHPlex](https://github.com/Sabrimjd/SSHPlex)
- Article : [Building SSHplex](/posts/building_sshplex/)
- Combine NetBox, Ansible, Consul et des listes statiques comme sources de vérité pour les hôtes et les équipements
- Propose trois modes de multiplexage : tmux standalone, tmux + iTerm2 et iTerm2 natif sur macOS
- Offre le broadcast de commandes et des sessions persistantes pour remplacer des solutions historiques coûteuses

## Expérience

### <a href="https://www.kindredgroup.com/"><img src="/img/Kindred.webp" alt="Kindred France" style="height: 30px; padding-right: 10px; vertical-align: middle;"></a> Kindred France | Site Reliability Engineer | 2021 - Présent

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

*   Évolution interne d'un poste d'ingénieur système vers un rôle de SRE, avec un accent de plus en plus fort sur la fiabilité de plateforme, l'observabilité et le diagnostic.
*   Gestion et amélioration des workflows d'observabilité autour de Kubernetes, avec Thanos, Loki, Grafana et Vector comme technologies centrales.
*   Création d'un outil HouseKeeping pour diagnostiquer les ressources Grafana obsolètes ou cassées et améliorer l'hygiène quotidienne de la plateforme.
*   Création d'un Search Query Exporter pour diagnostiquer les lenteurs de requêtes et établir des SLO sur Thanos, Loki et Splunk.
*   Conception d'un framework de dashboards SLO pour Kindred afin de standardiser la visibilité sur les niveaux de service et de faciliter l'adoption du reporting de fiabilité par les équipes.
*   Construction d'un Grafana AI Agent avec des garde-fous adaptés aux exigences d'entreprise, notamment un comportement sensible au RBAC et des flux de diagnostic basés sur MCP.
*   Renforcement récent de mon expertise sur les charts Helm, Argo CD, les images de conteneurs, Jenkins, GitLab, Splunk, AWS CloudWatch et CUR2.

#### Stack actuelle et domaines de responsabilité

| Domaine | Composants/Outils |
|---------|-------------------|
| Observabilité | Grafana, Loki, Thanos, Vector, Splunk, AWS CloudWatch |
| Ingénierie de plateforme | Kubernetes, Helm, Argo CD, Images de conteneurs |
| CI/CD & Automatisation | Jenkins, GitLab CI, Terraform, Ansible |
| Données & Stockage | Kafka, Redis, PostgreSQL, Microsoft SQL, Couchbase |
| Programmation & IA | Go, Python, Bash, IA, MCP |

#### Impact précédent au sein de la même entreprise

*   Pilotage du déploiement automatisé des VM et des applications via CI/CD, permettant plusieurs mises en production par jour.
*   Utilisation de Terraform pour déployer sur 10 datacenters et 4 fournisseurs (OpenStack, Proxmox, vSphere, NetBox) à partir de templates partagés.
*   Utilisation d'Ansible pour l'initialisation des VM et le déploiement applicatif, avec Consul pour alimenter les pools de services de HAProxy et Prometheus.
*   Mise en place et exploitation d'une plateforme Elastic Stack de grande ampleur gérant 200 TB de logs sur 10 noeuds avec Kafka pour le SIEM, le logging, l'EDR, l'APM et le suivi d'uptime.
*   Intégration d'un cluster Proxmox hautement disponible sur 4 racks et 2 datacenters avec Ceph, incluant l'automatisation PXE et un réseau 25 Gb par hôte.
*   Responsable du périmètre sécurité France, avec pilotage des remédiations de vulnérabilités et du durcissement de la production.

### <a href="https://www.vinc.fr/"><img src="/img/Vinc.png" alt="VINC" style="height: 30px; padding-right: 10px; vertical-align: middle;"></a> VINC | Ingénieur Système | 2019 - 2021

<div class="skills-container">
    <a href="/tags/proxmox" class="skill-badge">Proxmox</a>
    <a href="/tags/dns" class="skill-badge">DNS</a>
    <a href="/tags/ha" class="skill-badge">Haute Disponibilité</a>
</div>

*   Architecture de la nouvelle plateforme avec nouveaux routeurs BGP et Firewalls
*   Gestion de cluster Proxmox sur 2 datacenters
*   Responsable des SLA et communication avec les clients lors d'incidents de production
*   Implémentation de sites web selon les besoins clients
*   Implémentation d'une nouvelle stack DNS avec haute disponibilité

### Multi-Visp / Azuria | Administrateur Système | 2017 - 2019

<div class="skills-container">
    <a href="/tags/network" class="skill-badge">Infrastructure Réseau</a>
    <a href="/tags/vpn" class="skill-badge">VPN</a>
    <a href="/tags/datacenter" class="skill-badge">Gestion Datacenter</a>
    <a href="/tags/wifi" class="skill-badge">WiFi</a>
</div>

*   Installation complète de nouvelles baies dans Telehouse2
*   Gestion du câblage entre deux salles
*   Installation d'équipements wifi managés
*   Implémentation de services VPN haute disponibilité multi-datacenter

### Formation

**Louis Armand | BAC**

*   Apprentissage des bases de
    *   Réseau
    *   Pare-feu
    *   Électricité

**Louis Armand | BTS**

*   Apprentissage des bases de
    *   Algorithme avec Python
    *   Développement web avec PHP
    *   Stockage distribué
    *   Routage avec OSPF

**ESGI | Master**

*   Projet de fin d'études
    *  Déploiement d'une Stack Elastic avec ML
    *  Détection automatique d'anomalies avec signature JA3
    *  Import de la base de données JA3er pour blocage automatique depuis le routeur JunOS L3
    *  Limitation de débit / blocage dynamique du trafic au niveau L7

### Site Personnel | Développement d'un site personnel pour présenter mes compétences et expérience | Hugo, HTML, CSS, JavaScript

*   Conception et développement d'un site web responsive utilisant Hugo, HTML, CSS et JavaScript
*   Implémentation d'un blog pour partager mes réflexions sur le développement logiciel et la technologie

## Informations de Contact

*   Email: contact@smjed.net
