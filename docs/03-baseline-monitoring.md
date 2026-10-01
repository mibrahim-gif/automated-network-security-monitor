# 03 - Baseline Monitoring

## Objective

The baseline monitoring component detects changes in network services by comparing the current Nmap scan against an established security baseline.

This allows the security monitor to identify unexpected changes to the monitored system, including newly opened ports and ports that were previously available but are no longer detected.

---

## What Is a Security Baseline?

A security baseline represents the expected state of a monitored system.

For this project, the baseline records the network ports that are expected to be open on the target system.

The baseline is stored in:

```text
baseline.json
```

Example:

```json
{
    "target": "127.0.0.1",
    "open_ports": []
}
```

During the initial scan, the scanner records the currently detected open ports and uses them as the baseline for future comparisons.

---

## Baseline Monitoring Workflow

```text
                 Nmap Scan
                     |
                     v
             Current Open Ports
                     |
                     v
            Compare With Baseline
                     |
              +------+------+
              |             |
              v             v
          New Ports     Closed Ports
              |             |
              +------+------+
                     |
                     v
              Security Alert
                     |
                     v
              Security Report
```

---

## How the Comparison Works

The scanner maintains two sets of network ports:

```text
Baseline Ports
Current Scan Ports
```

The two sets are compared to identify changes.

### New Ports

A port is considered new when it appears in the current scan but was not present in the baseline.

```text
New Ports = Current Ports - Baseline Ports
```

For example:

```text
Baseline:
22
631

Current:
22
631
8080
```

The result is:

```text
New Port: 8080
```

---

### Closed Ports

A port is considered closed when it existed in the baseline but is no longer detected in the current scan.

```text
Closed Ports = Baseline Ports - Current Ports
```

For example:

```text
Baseline:
22
631
8080

Current:
22
631
```

The result is:

```text
Closed Port: 8080
```

---

## Example: Detecting a New Port

The project can use a temporary HTTP server to simulate a change in the network environment.

Start a local HTTP server:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

The service listens on:

```text
127.0.0.1:8080
```

The port can be verified using:

```bash
sudo nmap -sV -p 8080 127.0.0.1
```

Expected result:

```text
8080/tcp open  http
```

When the security scanner runs, it can compare the current state against the established baseline.

If port `8080` was not previously present, it can be reported as a new port.

---

## Example Detection

Suppose the baseline contains:

```text
22/tcp
631/tcp
```

A later scan detects:

```text
22/tcp
631/tcp
8080/tcp
```

The scanner identifies:

```text
[NEW] Port 8080 detected
```

This indicates that the monitored network state has changed.

The change is then available for further investigation.

---

## Example: Detecting a Closed Port

After testing the HTTP service, the service can be stopped.

The next scan may detect:

```text
22/tcp
631/tcp
```

while the baseline still contains:

```text
22/tcp
631/tcp
8080/tcp
```

The scanner can then identify:

```text
[CLOSED] Port 8080 no longer detected
```

This demonstrates that the monitoring system can detect changes in both directions.

---

## Security Investigation

A newly detected port does not automatically mean that malicious activity has occurred.

An analyst should investigate the reason for the change.

For example:

```text
New Port Detected
       |
       v
Identify Service
       |
       v
Identify Process
       |
       v
Determine Why It Was Opened
       |
       v
Verify Authorization
       |
       v
Review Configuration
       |
       v
Document Finding
```

Questions an analyst could ask include:

1. Which application opened the port?
2. Was the service intentionally installed?
3. Is the service authorized?
4. Which process owns the port?
5. Is authentication enabled?
6. Is the service properly configured?
7. Is the service exposed beyond the intended network?
8. Does the service require additional security controls?

---

## Security Value

Unexpected network changes can occur because of:

* New software installations
* Application deployments
* Configuration changes
* Administrative activity
* Temporary services
* Firewall changes
* Unauthorized services
* Potential security incidents

Baseline monitoring provides an automated way to identify these changes so that they can be investigated.

The purpose of the system is to provide visibility and generate security signals for further analysis.

---

## Relationship to Security Operations

The baseline monitoring process represents a simplified security monitoring workflow:

```text
Known Good State
       |
       v
Continuous Monitoring
       |
       v
Detect Change
       |
       v
Generate Alert
       |
       v
Analyst Investigation
       |
       v
Validate / Remediate
```

This demonstrates practical security operations concepts including:

* Network monitoring
* Configuration monitoring
* Change detection
* Security alerting
* Security investigation
* Automated security operations

---

## Current Limitations

The current implementation primarily monitors network ports and services.

It does not currently monitor:

* Running processes
* User accounts
* Installed software
* Firewall configuration
* File integrity
* System configuration
* Authentication events
* Cloud resources

Therefore, this implementation should be considered a **network-service baseline** rather than a complete host-security baseline.

---

## Future Improvements

Potential improvements include:

* Historical baseline storage
* SQLite database
* File integrity monitoring
* Process monitoring
* Installed package monitoring
* User-account monitoring
* Firewall configuration monitoring
* Cloud configuration monitoring
* Automated baseline approval
* SIEM integration
* AWS CloudWatch integration
* AWS Security Hub integration

---

## Security Disclaimer

This project is intended for educational purposes and authorized security testing.

Only monitor systems and networks that you own or have explicit permission to test.
