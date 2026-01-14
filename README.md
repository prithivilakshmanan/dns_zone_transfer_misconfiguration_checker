# DNS Zone Transfer Misconfiguration Scanner

A Python-based security testing tool to detect **DNS Zone Transfer (AXFR) misconfiguration** during VAPT and bug bounty assessments.

## 🚨 Vulnerability Checked
**DNS Zone Transfer Misconfiguration (AXFR Enabled)**

---

## ✨ Features
- Detects real DNS zone transfer misconfigurations
- Eliminates false positives
- Supports single and bulk domain scanning
- Color-coded results (Green = Secure, Red = Vulnerable)
- CLI-based, automation-friendly
- Report-ready output

---

## 🔧 Prerequisites
- Python 3.x
- dig utility

🚀 Installation (Linux)
1️⃣ Clone the Repository
` git clone https://github.com/prithivilakshmanan/dns_zone_transfer_misconfiguration_checker.git
cd dns_zone_transfer_misconfiguration_checker`

2️⃣ Install Required Dependency

This tool uses the dig utility to perform DNS zone transfer checks.

Kali Linux / Ubuntu / Debian
` sudo apt update
sudo apt install dnsutils -y`
Verify installation:
` dig -v`

▶ Usage
- Scan a Single Domain
` python3 dns_zone_misconfig_checker.py -d domain.com`
- Scan Multiple Domains
` python3 dns_zone_misconfig_checker.py -t domains.txt`

