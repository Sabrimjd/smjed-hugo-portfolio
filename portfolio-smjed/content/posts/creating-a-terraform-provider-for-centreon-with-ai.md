---
title: "AI Transformed My Journey as a System Engineer: Developing a Terraform Provider for Centreon"
date: 2025-02-25
tags: ["Go", "Terraform", "Github", "Github Actions", "CICD", "Open Source"]
---

As a day-to-day Terraform user with a decent foundation in Python, I never imagined that developing a Terraform provider would significantly impact my system engineering skills. Yet, leveraging AI tools enabled me to build a provider for Centreon API V2 and step into the Go ecosystem—an essential leap for my work at Kindred.

## Overview

For years, there was a significant gap in available tools: the only existing Centreon Terraform provider was built around the legacy CLAPI, which had not been updated in over five years. While there was also a V1 (distinct from CLAPI), it lacked the features needed for modern infrastructure management. My need for an up-to-date solution at Kindred pushed me to create a new provider based on the latest Centreon API V2, ensuring future-proof functionality and seamless integration with current workflows.

## AI-Powered Development Workflow

The AI-driven process was central to my success. Here’s how I leveraged it:

- **Using OpenAPI Documentation as Context:** I provided the Centreon API documentation to the AI, which generated integration code complete with logging, unit tests, and robust error handling.
- **GitHub Copilot & Insider Agent Mode:** Enhanced by the latest insider agent mode and the Claude Sonnet 3.5 model, GitHub Copilot in VSCode helped me interactively ask questions about code segments. This allowed me to understand the generated code, manage follow-up queries effectively, and reframe prompts when needed.
- **Iterative Testing:** I continuously asked the AI for explanations and tested the code, refining it until it met the necessary standards. This “managing the AI as a worker” approach was a game changer, providing clarity and a much-needed boost in confidence.

## Tools and Technologies

This project integrated a variety of tools to create a solid foundation for developing the provider:

- **GitHub & GitHub Actions:** Handled source control, CI/CD workflows, and automated testing.
- **Terraform Provider SDK V2:** Served as the framework for building provider-specific functionalities.
- **Go:** Became my primary language, with AI assistance bridging the gap from my Python background.
- **Linters & Makefiles:** Ensured code quality and streamlined the build process.
- **Unit Tests:** Played a critical role in ensuring the reliability and maintainability of the provider.
- **Tags and Releases:** Automated versioning and release management to maintain a clear project history.
- **Documentation & Contributing Workflow:** Established guidelines for external contributions and issue management.

I used the [Terraform Provider Scaffolding Framework](https://github.com/hashicorp/terraform-provider-scaffolding-framework) as my base repository for CI/CD, among other practices. However, I intentionally skipped the copyright tool offered by HashiCorp—since it would transfer code ownership to HashiCorp—to keep the project completely open source.

## Challenges and Lessons Learned

The journey was not without its challenges:

- **Prompt Engineering:** Crafting the right prompts was key. At times, follow-up questions led to context drift, requiring me to reset the conversation and guide the AI back on track.
- **Managing Context:** A larger context improved code coherence but sometimes resulted in an overload of follow-up queries that needed to be pruned.
- **Tool Limitations:** While GitHub Copilot in VSCode was a powerful assistant, occasional misalignments or unexpected bugs required me to intervene and adjust the AI's output.

Each challenge became a valuable lesson, improving the quality of the provider and deepening my technical expertise in Go and CI/CD integrations.

## Conclusion

Developing a Terraform provider for Centreon API V2 using AI was a practical, hands-on experience that significantly expanded my technical skill set. By combining modern AI tools with best practices and robust testing methodologies, I was able to fill a long-standing gap in the Centreon ecosystem and produce a provider that meets modern standards. This project not only improved my proficiency in Go and open source development but also reinforced the value of AI as an essential tool for system engineers.

---
*Originally published on the HuGO blog.*
