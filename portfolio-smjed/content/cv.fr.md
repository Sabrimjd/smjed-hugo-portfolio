---
title: "Mon CV"
type: "resume"
---

## Résumé

> Je suis un ingénieur System/Network/DevOps freelance passionné par l'IT depuis toujours. De mes premiers pas dans le code à la conception d'infrastructures complexes à haute disponibilité pour des clients entreprise, mon parcours dans la technologie a été guidé par la curiosité, la créativité et une volonté constante d'apprendre.

## Contributions Open Source

🌟 **Provider Terraform pour l'API Centreon V2**
> Développement et maintenance d'un provider Terraform personnalisé pour l'API V2 de Centreon, permettant les capacités d'infrastructure as code pour la plateforme de monitoring Centreon.
- Dépôt GitHub : [terraform-provider-centreon](https://github.com/Sabrimjd/terraform-provider-centreon/)
- Réalisation clé dans l'intégration de l'automatisation d'infrastructure et du monitoring
- Démontre une expertise en programmation Go et dans l'écosystème Terraform de HashiCorp

## Expérience

### Kindred France | Ingénieur Système | 2021 - Présent

*   Direction et implémentation du déploiement automatique de VM et d'applications avec CI/CD, permettant plusieurs déploiements par jour.
    *   Utilisation de Jenkins pour le pipeline avec Git
    *   Utilisation d'Ansible pour déployer les rôles d'initialisation VM et les applications nécessaires
    *   Utilisation de Terraform pour déployer sur 10 datacenters avec 4 fournisseurs différents (OpenStack, Proxmox, Vsphere, Netbox) en utilisant le même fichier template
    *   Utilisation de Netbox comme source de vérité pour lier l'ensemble et documenter toute l'infrastructure
    *   Utilisation de Consul pour alimenter automatiquement les pools de services pour HaProxy et Prometheus
    *   Utilisation de Vault pour le stockage des credentials
*   Responsable du périmètre de sécurité français, dirigeant les corrections nécessaires des vulnérabilités
*   Implémentation complète de la Stack Elastic gérant 200TB de logs avec 10 nœuds et Kafka pour :
    *   SIEM
    *   Logging (Réseau, Applications, Système)
    *   EDR
    *   Monitoring Springboot avec APM
    *   Monitoring réseau
    *   Uptime et SLA/SLOs avec Synthetics
*   Intégration d'un cluster Proxmox hautement disponible sur 4 racks et 2 datacenters utilisant CEPH
    *   Gestion du réseau avec 4 * 25GB par hôte (avec 30 hôtes au total)
    *   Déploiement automatique avec PXE
*   Proxy Squid multi-datacenter avec EBGP

#### Responsable technique et/ou implémentation de

| Stack Technologique | Composants/Outils |
|-----------------|------------------|
| Elastic Stack | Logstash, Kibana, ElasticSearch, Java APM, Elastic Agents, Intégration Splunk |
| Hashicorp | Vault, Terraform, Consul, Jenkins |
| Bases de données | Couchbase, Redis, PostgreSQL, Microsoft SQL |
| Virtualisation | Proxmox |
| Files de messages | Kafka |
| Réseau | Proxy Squid |
| Outils | Remote Desktop Manager |

Autres compétences acquises :

| Catégorie | Technologies/Outils |
|----------|-------------------|
| Solutions de Sécurité | FortiGate, FortiAnalyzer, FortiAuthenticator, FortiManager |
| Équilibrage de charge | F5 BigIP, HaProxy |
| Réseau | Nftables, Iptables, Juniper JunOS |
| Infrastructure | Netbox, Packer |
| Outils de Collaboration | Bitbucket, Jira, Confluence |

### VINC | Ingénieur Système | 2019 - 2021

*   Architecture de la nouvelle plateforme avec nouveaux routeurs BGP et Firewalls
*   Gestion de cluster Proxmox sur 2 datacenters
*   Responsable des SLA et communication avec les clients lors d'incidents de production
*   Implémentation de sites web selon les besoins clients
*   Implémentation d'une nouvelle stack DNS avec haute disponibilité

### Multi-Visp / Azuria | Administrateur Système | 2017 - 2019

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
