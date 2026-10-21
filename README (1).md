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

## Quick Start

```bash
# Clone the repository
git clone https://github.com/[your-username]/automated-network-security-monitor.git
cd automated-network-security-monitor

# Install dependencies (Kali Linux already includes nmap)
sudo apt install nmap python3
pip install -r requirements.txt   # if applicable

# Run a scan
python3 scanner.py
```

See [01-setup.md](docs/01-setup.md) for full setup instructions.

## Example Output

```
[paste a sanitized sample of your scanner output here]
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

This tool is for educational and defensive purposes. Only scan networks you own or have explicit written permission to test. The author is not responsible for misuse.

## License

[MIT / your choice] (add a `LICENSE` file)
