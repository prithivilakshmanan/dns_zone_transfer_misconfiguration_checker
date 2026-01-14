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

<!-- =============================== -->
<!-- Installation Section (Linux)   -->
<!-- =============================== -->

## 🚀 Installation (Linux)

```bash
git clone https://github.com/prithivilakshmanan/dns_zone_transfer_misconfiguration_checker.git
cd dns_zone_transfer_misconfiguration_checker
```

### 1️⃣ Scan Single Domain
```bash
python3 dns_zone_misconfig_checker.py -d domain.com
```
<img width="624" height="269" alt="1" src="https://github.com/user-attachments/assets/b8d197dd-31f5-4312-97bb-301df567479c" />

### 2️⃣ Scan Multiple Domains

```bash
python3 dns_zone_misconfig_checker.py -t domains.txt
```

<img width="838" height="386" alt="2" src="https://github.com/user-attachments/assets/9a51e16a-ca7d-4dc1-85a6-3ec980de5ed3" />



