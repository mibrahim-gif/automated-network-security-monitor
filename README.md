# Automated Network Security Monitor

## Overview

Automated network security monitoring tool built with **Python**, **Nmap**, and **Linux**.

The project performs network service discovery, identifies potentially risky services, compares the current network state against a security baseline, generates alerts and security reports, and runs automated scans using Linux cron.

## Features

- **Service discovery:** Nmap scans identify live hosts, open ports, and running services
- **Risky service detection:** flags services such as Telnet, FTP, SMB, and RDP that commonly lead to compromise
- **Baseline comparison:** compares each scan against a known-good state in `baseline.json`
- **Drift alerts:** reports new ports, closed ports, and risky services
- **Security reports:** generates timestamped findings with severity levels
- **Automation:** runs on a schedule using Linux cron

## Architecture

```
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
```

## Repository Structure

```
automated-network-security-monitor/
├── README.md
├── scanner.py
├── baseline.json
├── .gitignore
└── docs/
    ├── 01-setup.md
    ├── 02-security-detection.md
    ├── 03-baseline-monitoring.md
    ├── 04-reporting.md
    └── 05-automation.md
```


## Example Output

```


<img width="1244" height="814" alt="Screenshot 2026-09-30 at 3 11 30 PM" src="https://github.com/user-attachments/assets/c61db514-9214-4525-9bf3-3d7e7ad460de" />
<img width="948" height="815" alt="Screenshot 2026-10-01 at 12 02 07 AM" src="https://github.com/user-attachments/assets/45d20764-2135-419c-b7a0-328ee4cbec65" />
<img width="952" height="780" alt="Screenshot 2026-10-01 at 12 03 02 AM" src="https://github.com/user-attachments/assets/ba16753e-1efa-4f86-b0c2-5ee003c59f9a" />



```

## Documentation

| Document | Description |
|---|---|
| [01-setup.md](docs/01-setup.md) | Environment, installation, and first run |
| [02-security-detection.md](docs/02-security-detection.md) | What the tool detects, risk rules, and framework mapping |
| [03-baseline-monitoring.md](docs/03-baseline-monitoring.md) | How the baseline works and how drift is detected |
| [04-reporting.md](docs/04-reporting.md) | Alert and report format, severity levels |
| [05-automation.md](docs/05-automation.md) | Scheduling scans with cron and secure operation |

## Security Engineering Concepts Demonstrated

- Network service discovery (MITRE ATT&CK T1046)
- Attack surface monitoring and risk-based detection
- Security baselining and configuration drift detection
- Alerting and reporting with severity classification
- Security automation with Python and Linux cron

## Limitations

- Hosts behind firewalls may not respond to scans
- An open port does not necessarily mean a vulnerability exists
- The tool does not currently check for specific CVEs

## Future Improvements

- CVE lookup for detected service versions
- Email or Slack/Discord alerting
- SIEM integration
- Web dashboard

## Disclaimer

This tool is for educational and defensive purposes. 

## License

[MIT / your choice] (add a `LICENSE` file)
