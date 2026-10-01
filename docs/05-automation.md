# 05 - Automation

## Objective

The automation component uses Linux cron to execute the security scanner on a recurring schedule.

The goal is to demonstrate how a security monitoring process can operate automatically without requiring an analyst to manually start each scan.

---

## Automation Workflow

```text
                 Linux Cron
                     |
                     v
              Python Scanner
                     |
                     v
                   Nmap
                     |
                     v
             XML Scan Results
                     |
                     v
            Security Analysis
                     |
          +----------+----------+
          |                     |
          v                     v
       Alerts                Reports
          |                     |
          +----------+----------+
                     |
                     v
              Analyst Review
```

---

## Why Automation?

Manual security scans require an analyst to remember to execute the scanner.

Automating the process provides:

* Consistent monitoring
* Repeatable scans
* Reduced manual effort
* Scheduled security checks
* Historical security reports
* Faster detection of network changes

Automation is particularly useful when security monitoring needs to occur on a regular schedule.

---

## Linux Cron

Cron is a Linux scheduling mechanism that allows commands and scripts to execute automatically at specified times.

The current user's scheduled jobs can be viewed with:

```bash
crontab -l
```

The cron configuration can be edited with:

```bash
crontab -e
```

---

## Test Schedule

During development, the scanner can be scheduled to run every five minutes.

Example:

```text
*/5 * * * * cd /home/kali/security-automation-lab && /usr/bin/python3 scanner.py >> /home/kali/security-automation-lab/logs/cron.log 2>&1
```

This configuration runs the scanner every five minutes.

The command changes into the project directory before executing the scanner.

This is important because the scanner uses project-relative directories such as:

```text
scans/
reports/
alerts/
logs/
```

---

## Daily Schedule

For a less frequent monitoring schedule, the scanner can run once per day.

Example:

```text
0 9 * * * cd /home/kali/security-automation-lab && /usr/bin/python3 scanner.py >> /home/kali/security-automation-lab/logs/cron.log 2>&1
```

This executes the scanner every day at approximately 9:00 AM.

The appropriate schedule depends on the environment and monitoring requirements.

---

## Cron Logging

The scheduled command redirects its output to:

```text
logs/cron.log
```

This provides a basic record of the automated execution process.

The log can be reviewed with:

```bash
cat logs/cron.log
```

For larger environments, centralized logging would be preferable.

---

## Verifying Automation

The configured cron jobs can be checked using:

```bash
crontab -l
```

The cron service can be checked using:

```bash
systemctl status cron
```

If the service needs to be started:

```bash
sudo systemctl start cron
```

After the scheduled task executes, generated reports can be reviewed with:

```bash
ls -lt reports/
```

The newest report should appear at the top of the listing.

---

## Automated Monitoring Example

A typical automated workflow looks like this:

```text
09:00
 |
 v
Cron starts scanner
 |
 v
Nmap scans target
 |
 v
Python parses results
 |
 v
Security rules evaluated
 |
 +-------> Risky service detected
 |              |
 |              v
 |          Alert generated
 |
 v
Baseline comparison
 |
 +-------> New port detected
 |              |
 |              v
 |          Change recorded
 |
 v
Security report generated
 |
 v
Scan complete
```

This demonstrates how individual security tools can be combined into an automated monitoring workflow.

---

## Security Operations Use Case

Automated scanning can help identify changes that might otherwise go unnoticed.

For example, a new service may be installed between scheduled scans:

```text
Previous Scan
    |
    v
22/tcp
631/tcp
```

A later automated scan discovers:

```text
22/tcp
631/tcp
8080/tcp
```

The baseline comparison identifies:

```text
[NEW] Port 8080 detected
```

The generated report provides information that an analyst can investigate.

---

## Operational Security Considerations

Security automation should be implemented carefully.

Important considerations include:

### Authorized Targets

Only scan systems and networks that are owned or explicitly authorized for testing.

### Scan Frequency

Scanning too frequently can create unnecessary network traffic and system load.

### Log Protection

Security logs and reports may contain sensitive information and should be protected appropriately.

### Credential Protection

Credentials, API keys, passwords, and tokens should never be hard-coded into scripts.

### Automation Failures

Scheduled jobs should be monitored so that failures do not silently stop security monitoring.

### File Permissions

Generated security reports, logs, and baseline files should have appropriate permissions.

### Absolute Paths

Scheduled tasks should use reliable paths because cron may execute commands with a different working directory than an interactive terminal.

---

## Current Limitations

The current automation implementation uses local Linux cron.

It does not currently provide:

* Centralized scheduling
* Distributed scanning
* Cloud-based execution
* Email notifications
* Slack or Teams notifications
* SIEM integration
* Automated incident ticket creation
* Automated remediation

The current implementation is intentionally lightweight and demonstrates the fundamentals of security automation.

---

## Future Improvements

Future versions could integrate additional automation capabilities.

### Email Alerting

Send an email when a high-priority security finding is detected.

### Slack or Teams Integration

Send security alerts directly to a security operations channel.

### SIEM Integration

Forward findings to a SIEM for centralized monitoring and correlation.

### Cloud Automation

Run the monitoring process using cloud infrastructure such as AWS.

Potential integrations include:

* AWS CloudWatch
* AWS Lambda
* AWS Security Hub
* AWS EventBridge

### Automated Ticketing

Create an incident or remediation ticket when an unexpected network change is detected.

### CI/CD Integration

Security tests could be integrated into a CI/CD pipeline to identify security issues before code or infrastructure changes are deployed.

---

## Project Architecture

The completed automation workflow can be summarized as:

```text
                 +----------------+
                 |  Linux Cron    |
                 +-------+--------+
                         |
                         v
                 +---------------+
                 | Python Scanner |
                 +-------+-------+
                         |
                         v
                    +--------+
                    |  Nmap  |
                    +---+----+
                        |
                        v
                  XML Scan Data
                        |
                        v
                +---------------+
                | Security Rules|
                +-------+-------+
                        |
              +---------+---------+
              |                   |
              v                   v
       Baseline Check       Risk Detection
              |                   |
              +---------+---------+
                        |
                        v
                +---------------+
                | Alerts/Report |
                +---------------+
```

This architecture demonstrates the integration of **Linux administration, Python automation, network security monitoring, detection engineering, baseline monitoring, and scheduled security operations**.

---

## Security Disclaimer

This project is intended for educational purposes and authorized security testing.

Only automate scans against systems and networks that you own or have explicit permission to monitor.
