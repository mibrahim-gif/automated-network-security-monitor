# 01 - Project Setup

## Objective

Set up the Automated Network Security Monitor in Kali Linux and verify that the required tools are available.

## Technologies

- Kali Linux
- Python 3
- Nmap
- Linux
- Git/GitHub
- Cron

## Project Architecture

```text
Kali Linux
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
Security Detection
     |
     v
Baseline Comparison
     |
     +---------> Alerts
     |
     +---------> Security Reports
