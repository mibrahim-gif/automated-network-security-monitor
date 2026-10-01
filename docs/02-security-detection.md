
---

# `docs/02-security-detection.md`


```markdown
# 02 - Security Detection

## Objective

Identify potentially risky network services discovered during Nmap scanning.

The goal is to demonstrate basic security detection and risk classification using Python.

## Detection Process

The scanner performs the following process:

```text
Nmap Scan
    |
    v
XML Results
    |
    v
Python XML Parser
    |
    v
Open Ports
    |
    v
Security Detection Rules
    |
    v
Security Findings
