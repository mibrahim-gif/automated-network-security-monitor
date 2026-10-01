# 02 - Security Detection

## Objective

The security detection component analyzes Nmap scan results and identifies network services that may require additional security review.

The goal of this component is to demonstrate how security automation can transform raw network scan data into actionable security findings.

---

## Detection Workflow

```text
Nmap Scan
    |
    v
XML Scan Results
    |
    v
Python XML Parser
    |
    v
Open Ports & Services
    |
    v
Security Detection Rules
    |
    v
Security Findings
    |
    v
Alerts & Reports
```

---

## How Detection Works

The Python scanner executes Nmap with service detection enabled.

Nmap generates an XML file containing information about the target system, including:

* Open ports
* Port protocols
* Service names
* Service versions
* Port states

The Python script parses this XML data and extracts the services discovered during the scan.

The extracted ports are then compared against predefined security detection rules.

---

## Security Detection Rules

The current implementation monitors several commonly encountered network services:

| Port | Service | Risk Level |
| ---- | ------- | ---------- |
| 21   | FTP     | Medium     |
| 23   | Telnet  | High       |
| 445  | SMB     | Medium     |
| 3389 | RDP     | High       |

These classifications are simplified rules created for this laboratory project. They are not intended to represent a complete vulnerability assessment.

---

## FTP - Port 21

FTP is commonly used for file transfers.

Depending on its configuration, FTP may transmit authentication information and data without encryption.

The scanner therefore identifies FTP as a service that should receive additional security review.

### Security considerations

* Is FTP required?
* Is anonymous access enabled?
* Is encrypted file transfer available?
* Is the service exposed outside the intended network?
* Is the software version current?

---

## Telnet - Port 23

Telnet provides remote access to systems but does not provide encryption by default.

The scanner classifies Telnet as a high-priority finding because credentials and session information may potentially be exposed.

### Security considerations

* Replace Telnet with SSH where possible.
* Restrict network access.
* Review authentication configuration.
* Remove the service if it is unnecessary.

---

## SMB - Port 445

SMB is commonly used for Windows file and printer sharing.

An exposed SMB service should be reviewed to ensure appropriate authentication, authorization, patching, and network segmentation controls are in place.

### Security considerations

* Verify that SMB is required.
* Restrict access through firewall rules.
* Review share permissions.
* Ensure systems are patched.
* Monitor for unauthorized access.

---

## RDP - Port 3389

RDP provides remote access to Windows systems.

The scanner flags RDP so that its exposure and configuration can be reviewed.

### Security considerations

* Restrict RDP access.
* Use strong authentication.
* Use MFA where available.
* Avoid unnecessary internet exposure.
* Monitor authentication attempts.

---

## Example Detection

If Nmap discovers:

```text
23/tcp open telnet
```

the scanner can generate a finding similar to:

```text
[HIGH] Telnet detected on port 23
```

The finding is recorded in the security alert log and included in the generated security report.

---

## Detection vs. Vulnerability Assessment

An important security principle demonstrated by this project is that **detecting an open port does not automatically mean that a vulnerability exists**.

For example:

```text
Port 3389 Open
      |
      v
RDP Detected
      |
      v
Requires Investigation
```

Additional information should be evaluated, including:

* Software version
* Service configuration
* Authentication controls
* Network exposure
* Firewall rules
* Known CVEs
* Patch status
* Compensating controls

The scanner identifies potential security concerns rather than automatically declaring a system vulnerable or compromised.

---

## Alert Generation

Security findings are written to:

```text
alerts/alerts.log
```

Security findings are also included in the generated reports stored in:

```text
reports/
```

This provides both an alerting mechanism and a historical record of detected security events.

---

## Example Security Finding

A scan that identifies multiple services might produce findings such as:

```text
Security Findings:

[MEDIUM] FTP detected on port 21
[HIGH] Telnet detected on port 23
[MEDIUM] SMB detected on port 445
[HIGH] RDP detected on port 3389
```

An analyst can then investigate each finding and determine whether the service is authorized and appropriately secured.

---

## Security Operations Use Case

This detection process represents a simplified version of a security monitoring workflow:

```text
Network Discovery
       |
       v
Service Identification
       |
       v
Security Rule Matching
       |
       v
Alert Generation
       |
       v
Analyst Investigation
       |
       v
Remediation / Documentation
```

This workflow demonstrates concepts used in security operations and security engineering, including:

* Network monitoring
* Detection engineering
* Security automation
* Alert generation
* Baseline comparison
* Security investigation

---

## Limitations

The current detection engine uses predefined port-based rules.

It does not currently perform a complete vulnerability assessment.

For example, detecting port 22 does not determine whether SSH is vulnerable, and detecting port 3389 does not determine whether RDP is exploitable.

A complete assessment would require additional information and security tools.

---

## Future Improvements

Potential improvements include:

* CVE enrichment
* CVSS scoring
* Software-version analysis
* MITRE ATT&CK mapping
* Threat-intelligence enrichment
* More detailed detection rules
* SIEM integration
* Email notifications
* Slack or Microsoft Teams notifications
* Automated remediation workflows

---

## Security Disclaimer

This project is intended for educational purposes and authorized security testing.

Only scan systems and networks that you own or have explicit permission to test.
