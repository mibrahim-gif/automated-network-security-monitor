# Automated Network Security Monitor

## Overview

Automated network security monitoring tool built with Python, Nmap, and Linux.

The project performs network service discovery, identifies potentially risky services, compares the current network state against a security baseline, generates alerts and security reports, and runs automated scans using Linux cron.

## Architecture

```text
Kali Linux
    │
    ▼
Python Automation
    │
    ▼
Nmap Service Scan
    │
    ▼
Security Detection
    │
    ▼
Baseline Comparison
    │
    ├── New Ports
    ├── Closed Ports
    └── Risky Services
    │
    ▼
Alerts + Security Reports
    │
    ▼
Cron Automation
