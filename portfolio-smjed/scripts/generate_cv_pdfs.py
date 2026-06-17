#!/usr/bin/env python3
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "static" / "files"
OUT.mkdir(parents=True, exist_ok=True)

ACCENT = colors.HexColor("#2563eb")
TEXT = colors.HexColor("#111827")
MUTED = colors.HexColor("#4b5563")
BORDER = colors.HexColor("#d1d5db")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22,
    leading=26, textColor=TEXT, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Role", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5,
    leading=14, textColor=MUTED, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11.5,
    leading=14, textColor=ACCENT, spaceBefore=10, spaceAfter=5,
    uppercase=True,
))
styles.add(ParagraphStyle(
    name="Job", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10.5,
    leading=13, textColor=TEXT, spaceBefore=7, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="Body", parent=styles["Normal"], fontName="Helvetica", fontSize=9.2,
    leading=12.2, textColor=TEXT, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["Normal"], fontName="Helvetica", fontSize=8.3,
    leading=10.5, textColor=MUTED,
))
styles.add(ParagraphStyle(
    name="CVBullet", parent=styles["Body"], leftIndent=0, firstLineIndent=0, spaceAfter=2,
))


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def bullets(items):
    return ListFlowable(
        [ListItem(p(item, "CVBullet"), bulletColor=ACCENT, leftIndent=10) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=12,
        bulletFontSize=5,
        bulletOffsetY=1,
    )


def tech_table(rows):
    data = [[p(f"<b>{k}</b>", "Small"), p(v, "Small")] for k, v in rows]
    table = Table(data, colWidths=[4.2 * cm, 12.2 * cm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, BORDER),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def build(path, lang):
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=1.4*cm, leftMargin=1.4*cm, topMargin=1.25*cm, bottomMargin=1.25*cm)
    story = []

    if lang == "en":
        story += [
            p("Sabri Mjahed", "Name"),
            p("Senior Site Reliability Engineer / Freelance Infrastructure & Observability Consultant", "Role"),
            p("Paris area, France · contact@smjed.net · https://smjed.net · GitHub: Sabrimjd", "Small"),
            Spacer(1, 6),
            p("Profile", "Section"),
            p("Senior freelance SRE with 10 years of experience operating infrastructure that cannot quietly fail. Focus areas: high-volume observability, Kubernetes platform engineering, on-prem Proxmox/Ceph clusters, automation, and practical AI-assisted SRE tooling."),
            p("Core skills", "Section"),
            tech_table([
                ("Observability", "Grafana, Loki, Thanos, Vector, Prometheus, AWS CloudWatch, SLO frameworks"),
                ("Platform engineering", "Kubernetes, Helm, Argo CD, container image lifecycle, GitLab CI, Jenkins"),
                ("Infrastructure", "Proxmox, Ceph, OpenStack, vSphere, NetBox, HAProxy, Consul, BGP, firewalls"),
                ("Automation & code", "Terraform, Ansible, Go, Python, Bash, MCP, AI-assisted operations"),
                ("Data & storage", "Kafka, Redis, PostgreSQL, Microsoft SQL Server, Couchbase"),
            ]),
            p("Experience", "Section"),
            p("Kindred France - Site Reliability Engineer / System Engineer · 2021 - Present", "Job"),
            bullets([
                "Progressed from System Engineer to SRE, shifting focus from infrastructure automation to platform reliability, observability, diagnostics and performance.",
                "Operated multi-cluster observability workflows around Kubernetes with Grafana, Loki, Thanos and Vector as core technologies.",
                "Built internal tools to diagnose stale Grafana resources, query slowness and dashboard/config drift across observability platforms.",
                "Designed SLO dashboard frameworks to standardize service-level visibility and make reliability reporting easier to adopt.",
                "Operated multi-cluster observability at multi-TB/day ingestion across logs, metrics and traces, with Kafka pipelines feeding SIEM, logging, EDR, APM and uptime monitoring.",
                "Used Terraform to deploy across 10 datacenters and 4 providers: OpenStack, Proxmox, vSphere and NetBox.",
                "Integrated a highly available Proxmox cluster across 4 racks and 2 datacenters with Ceph, PXE automation and 25 Gb networking per host.",
                "Built Graphia, a domain-specific SRE agent for Grafana diagnosis with RBAC-aware behaviour, MCP-based flows and enterprise safeguards.",
            ]),
            p("VINC - System Engineer · 2019 - 2021", "Job"),
            bullets([
                "Architected a new platform with BGP routers, firewalls and high-availability DNS.",
                "Managed Proxmox clusters across 2 datacenters.",
                "Handled SLA follow-up and client communication during production incidents.",
            ]),
            p("Multi-Visp / Azuria - System Administrator · 2017 - 2019", "Job"),
            bullets([
                "Installed complete racks in Telehouse2 and handled datacenter cabling between rooms.",
                "Installed managed Wi-Fi equipment and implemented high-availability multi-datacenter VPN services.",
            ]),
            p("Open source", "Section"),
            p("SSHplex - Open source terminal UI for SSH connection multiplexing. Combines NetBox, Ansible, Consul and static host lists as sources of truth, supports tmux/iTerm2 backends, broadcast commands and persistent sessions."),
        ]
    else:
        story += [
            p("Sabri Mjahed", "Name"),
            p("Senior Site Reliability Engineer / Consultant freelance infrastructure & observabilité", "Role"),
            p("Région parisienne, France · contact@smjed.net · https://smjed.net · GitHub: Sabrimjd", "Small"),
            Spacer(1, 6),
            p("Profil", "Section"),
            p("SRE freelance senior avec 10 ans d'expérience sur des infrastructures qui ne peuvent pas tomber en silence. Domaines principaux : observabilité haut volume, ingénierie de plateforme Kubernetes, clusters Proxmox/Ceph on-prem, automatisation et outillage SRE assisté par IA."),
            p("Compétences clés", "Section"),
            tech_table([
                ("Observabilité", "Grafana, Loki, Thanos, Vector, Prometheus, AWS CloudWatch, frameworks SLO"),
                ("Plateforme", "Kubernetes, Helm, Argo CD, cycle de vie des images container, GitLab CI, Jenkins"),
                ("Infrastructure", "Proxmox, Ceph, OpenStack, vSphere, NetBox, HAProxy, Consul, BGP, firewalls"),
                ("Automatisation & code", "Terraform, Ansible, Go, Python, Bash, MCP, opérations assistées par IA"),
                ("Données & stockage", "Kafka, Redis, PostgreSQL, Microsoft SQL Server, Couchbase"),
            ]),
            p("Expérience", "Section"),
            p("Kindred France - Site Reliability Engineer / Ingénieur système · 2021 - Présent", "Job"),
            bullets([
                "Évolution d'un poste d'ingénieur système vers un rôle SRE, avec un focus sur fiabilité de plateforme, observabilité, diagnostic et performance.",
                "Exploitation de workflows d'observabilité multi-cluster autour de Kubernetes avec Grafana, Loki, Thanos et Vector.",
                "Création d'outils internes pour diagnostiquer les ressources Grafana obsolètes, les lenteurs de requêtes et la dérive de configuration.",
                "Conception de frameworks de dashboards SLO pour standardiser la visibilité service-level et faciliter l'adoption du reporting de fiabilité.",
                "Exploitation d'une plateforme d'observabilité avec ingestion de plusieurs TB/jour sur logs, métriques et traces, pipelines Kafka vers SIEM, logging, EDR, APM et uptime monitoring.",
                "Utilisation de Terraform pour déployer sur 10 datacenters et 4 fournisseurs : OpenStack, Proxmox, vSphere et NetBox.",
                "Intégration d'un cluster Proxmox hautement disponible sur 4 racks et 2 datacenters avec Ceph, automatisation PXE et réseau 25 Gb par hôte.",
                "Construction de Graphia, agent SRE spécialisé pour le diagnostic Grafana avec comportement RBAC-aware, workflows MCP et garde-fous enterprise.",
            ]),
            p("VINC - Ingénieur système · 2019 - 2021", "Job"),
            bullets([
                "Architecture d'une nouvelle plateforme avec routeurs BGP, firewalls et DNS haute disponibilité.",
                "Gestion de clusters Proxmox sur 2 datacenters.",
                "Suivi des SLA et communication client lors d'incidents de production.",
            ]),
            p("Multi-Visp / Azuria - Administrateur système · 2017 - 2019", "Job"),
            bullets([
                "Installation complète de baies dans Telehouse2 et gestion du câblage entre deux salles.",
                "Installation d'équipements Wi-Fi managés et mise en place de VPN haute disponibilité multi-datacenter.",
            ]),
            p("Open source", "Section"),
            p("SSHplex - Interface terminal open source pour le multiplexage de connexions SSH. Combine NetBox, Ansible, Consul et des listes statiques comme sources de vérité, avec backends tmux/iTerm2, broadcast de commandes et sessions persistantes."),
        ]

    doc.build(story)


if __name__ == "__main__":
    build(OUT / "sabri-mjahed-cv-en.pdf", "en")
    build(OUT / "sabri-mjahed-cv-fr.pdf", "fr")
    print(OUT / "sabri-mjahed-cv-en.pdf")
    print(OUT / "sabri-mjahed-cv-fr.pdf")
