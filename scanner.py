import subprocess
import datetime
import os
import json
import xml.etree.ElementTree as ET

# ==========================================
# CONFIGURATION
# ==========================================

TARGET = "127.0.0.1"
BASELINE_FILE = "baseline.json"

RISKY_PORTS = {
    21: ("FTP", "MEDIUM"),
    23: ("Telnet", "HIGH"),
    445: ("SMB", "MEDIUM"),
    3389: ("RDP", "HIGH")
}

# ==========================================
# SETUP
# ==========================================

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

os.makedirs("scans", exist_ok=True)
os.makedirs("alerts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

output_file = f"scans/scan_{timestamp}.xml"
report_file = f"reports/security_report_{timestamp}.txt"

# ==========================================
# RUN NMAP
# ==========================================

command = [
    "nmap",
    "-sV",
    "-oX",
    output_file,
    TARGET
]

print("=" * 50)
print("AUTOMATED SECURITY SCANNER")
print("=" * 50)

print(f"[+] Target: {TARGET}")
print("[+] Starting Nmap scan...")

result = subprocess.run(command)

if result.returncode != 0:
    print("[-] Nmap scan failed.")
    exit(1)

print("[+] Scan completed.")
print(f"[+] Results saved to: {output_file}")

# ==========================================
# PARSE NMAP RESULTS
# ==========================================

tree = ET.parse(output_file)
root = tree.getroot()

print("\n[+] Analyzing discovered services...\n")

findings = []
current_ports = []

for port in root.findall(".//port"):

    port_number = int(port.get("portid"))
    protocol = port.get("protocol")

    state = port.find("state")

    if state is not None and state.get("state") == "open":

        current_ports.append(port_number)

        service = port.find("service")

        service_name = "unknown"

        if service is not None:
            service_name = service.get("name", "unknown")

        print(
            f"[OPEN] "
            f"{port_number}/{protocol} - "
            f"{service_name}"
        )

        # Check for risky services

        if port_number in RISKY_PORTS:

            name, severity = RISKY_PORTS[port_number]

            finding = {
                "port": port_number,
                "protocol": protocol,
                "service": name,
                "severity": severity
            }

            findings.append(finding)

            print(
                f"[ALERT] "
                f"{severity}: "
                f"{name} detected!"
            )

# ==========================================
# LOAD BASELINE
# ==========================================

if os.path.exists(BASELINE_FILE):

    with open(BASELINE_FILE, "r") as file:
        baseline = json.load(file)

else:

    baseline = {
        "target": TARGET,
        "open_ports": []
    }

baseline_ports = set(baseline["open_ports"])
current_ports_set = set(current_ports)

# ==========================================
# COMPARE AGAINST BASELINE
# ==========================================

new_ports = current_ports_set - baseline_ports
closed_ports = baseline_ports - current_ports_set

print("\n" + "=" * 50)
print("BASELINE COMPARISON")
print("=" * 50)

if new_ports:

    print("[!] NEW PORTS DETECTED:")

    for port in sorted(new_ports):
        print(f"    [+] {port}/tcp")

else:

    print("[+] No new ports detected.")

if closed_ports:

    print("[+] PORTS NO LONGER OPEN:")

    for port in sorted(closed_ports):
        print(f"    [-] {port}/tcp")

# ==========================================
# CREATE / UPDATE BASELINE
# ==========================================

if not baseline["open_ports"]:

    baseline["open_ports"] = sorted(current_ports)

    with open(BASELINE_FILE, "w") as file:
        json.dump(baseline, file, indent=4)

    print("\n[+] Initial security baseline created.")

# ==========================================
# SAVE SECURITY ALERTS
# ==========================================

if findings:

    alert_file = "alerts/alerts.log"

    with open(alert_file, "a") as file:

        file.write("\n")
        file.write(f"Scan: {timestamp}\n")

        for finding in findings:

            file.write(
                f"[{finding['severity']}] "
                f"{finding['port']}/"
                f"{finding['protocol']} "
                f"{finding['service']}\n"
            )

    print("\n[!] Security findings detected.")
    print(f"[+] Alerts saved to: {alert_file}")

else:

    print("\n[+] No configured high-risk services detected.")

# ==========================================
# GENERATE SECURITY REPORT
# ==========================================

with open(report_file, "w") as report:

    report.write("=" * 60 + "\n")
    report.write("AUTOMATED SECURITY ASSESSMENT REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Scan Date: {timestamp}\n")
    report.write(f"Target: {TARGET}\n\n")

    # Open ports

    report.write("OPEN PORTS\n")
    report.write("-" * 60 + "\n")

    if current_ports:

        for port in sorted(current_ports):
            report.write(f"{port}/tcp\n")

    else:

        report.write("No open ports detected.\n")

    # Security findings

    report.write("\nSECURITY FINDINGS\n")
    report.write("-" * 60 + "\n")

    if findings:

        for finding in findings:

            report.write(
                f"[{finding['severity']}] "
                f"{finding['port']}/"
                f"{finding['protocol']} "
                f"{finding['service']}\n"
            )

    else:

        report.write(
            "No configured high-risk services detected.\n"
        )

    # Baseline changes

    report.write("\nBASELINE CHANGES\n")
    report.write("-" * 60 + "\n")

    if new_ports:

        for port in sorted(new_ports):
            report.write(
                f"NEW PORT: {port}/tcp\n"
            )

    else:

        report.write("No new ports detected.\n")

    if closed_ports:

        for port in sorted(closed_ports):
            report.write(
                f"CLOSED PORT: {port}/tcp\n"
            )

    # Recommendations

    report.write("\nRECOMMENDATIONS\n")
    report.write("-" * 60 + "\n")

    report.write(
        "1. Verify that exposed services are authorized.\n"
    )

    report.write(
        "2. Disable unnecessary network services.\n"
    )

    report.write(
        "3. Investigate newly exposed ports.\n"
    )

    report.write(
        "4. Maintain regular security scanning "
        "and baseline monitoring.\n"
    )

# ==========================================
# COMPLETE
# ==========================================

print(
    f"\n[+] Security report generated: "
    f"{report_file}"
)

print("\n[+] Security scan complete.")
