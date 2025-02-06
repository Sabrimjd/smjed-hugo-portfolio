---
title: "My Resume"
type: "resume"
---

## Summary

> I'm a freelance System/Network/DevOps engineer with a lifelong passion for IT. From tinkering with code at an early age to architecting complex, high-availability infrastructures for enterprise clients, my journey in technology has been driven by curiosity, creativity, and a relentless desire to learn.

## Experience

### Company Name | Job Title | Dates of Employment

*   Describe your responsibilities and accomplishments using action verbs.
*   Quantify your achievements whenever possible (e.g., "Increased sales by 20%").
*   Highlight your key skills and contributions.

*Example:*

### Kindred France | System engineer | 2021 - Present

*   Led and implemented the automatic deployment of VM and application with CI/CD, acchieving multiple deployment per day.
    *   Used Jenkins for pipelining with Git
    *   Used Ansible to deploy the VM initliazation roles and the needed apps
    *   Used Terraform to deploy accross 10 datacenter with 4 different provider (OpenStack, Proxmox, Vsphere, Netbox) using the same template file
    *   Used Netbox as a Source of truth to link everything together and document the whole infrastructure.
    *   Used Consul to automaticaly feed a the services pools for HaProxy and Prometheus
    *   Used Vault for storing credentials
*   Accountable for the french security scope, leading the needed fix of vulnerabilities.
*   Implemented the whole Elastic Stack that manages a 200TB of logs with 10 nodes and Kafka for :
    *   SIEM
    *   Logging (Network, Apps, System)
    *   EDR
    *   Springboot monitoring with APM
    *   Network monitoring
    *   Uptime and SLA/SLOs with Synthetics
*   Integrated a fully highly available Proxmox cluster arround 4 racks and 2 datacenter using CEPH
    *   Managed the networking with 4 * 25GB per host (with 30 host total)
    *   Automatic deployment with PXE
*   Multi datacenter Squid proxy with EBGP

#### Business owner and/or implementor of

* Elastic Stack
  * Logstash
  * Kibana
  * ElasticSearch
  * Java APM
  * Elastic Agents
  * Sending logs to splunk
* Couchbase
* Kafka
* Proxmox
* Hashicorp
  * Vault
  * Terraform
  * Consul
  * Jenkins
* Remote Desktop Manager
* Proxy Squid
* Redis

Other skills aquired :

* Fortinet
  * FortiGate
  * FortiAnalyzer
  * FortiAuthentificator
  * FortiManager
* F5 BigIP / HaProxy
* Nftables / Iptables
* Juniper JunOS
* Netbox
* Packer
* PostgreSQL
* Microsoft SQL
* Bitbucket / Jira / Confluence

### VINC | System engineer | 2019 - 2021

*   Archictured the new plateform with new BGP routers and Firewalls
*   Managed Proxmox cluster arround 2 datacenters
*   Responsible for SLA and communication with clients for production accident
*   Implementation of websites arround client needs
*   Implemented a new DNS stack with high availability in mind


### Multi-Visp / Azuria | System administrator | 2017 - 2019

*   Installed complete new racks in Telehouse2
*   Cable management between two rooms
*   Installed managed wifi equipmenents
*   Implemented high availability multi datacenter VPN services

### Education

**Louis Armand | BAC**

*   Learned the basics of
    *   Networking
    *   Firewalling
    *   Electricity


**Louis Armand | BTS**

*   Learned basics of
    *   Algorithm with Python
    *   Web development with PHP
    *   Distributed Storage
    *   Routing with OSPF

**ESGI | Master degree**


### Personal Website | Developed a personal website to showcase my skills and experience | Hugo, HTML, CSS, JavaScript

*   Designed and developed a responsive website using Hugo, HTML, CSS, and JavaScript.
*   Implemented a blog to share my thoughts on software development and technology.
*   Deployed the website to Netlify.

## Contact Information

*   Email: contact@smjed.net
