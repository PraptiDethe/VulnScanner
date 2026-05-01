# 🔍 VulnScanner

A Python-based web vulnerability scanner built as part of the **Computer Networks & Security (CNS)** lab — Third Year Engineering, Sem-VI @ Vidyalankar Institute of Technology.

VulnScanner detects common web vulnerabilities through both a **Flask web UI** and a **CLI interface**.

---

## 🧩 Features

| Module | Description |
|---|---|
| **SQL Injection** | Error-based & time-based blind SQLi via form fuzzing |
| **XSS** | Reflected XSS via form inputs and URL parameters |
| **Security Headers** | Checks for missing HSTS, CSP, X-Frame-Options, and more |
| **Subdomain Enumeration** | DNS-based wordlist enumeration of subdomains |
| **Reporting** | Console (color-coded) and JSON output modes |

---

## 📁 Project Structure

```
VulnScanner/
├── app.py                  # Flask web application
├── main.py                 # CLI entry point
├── requirements.txt
├── templates/
│   └── index.html          # Frontend UI
└── scanner/
    ├── engine.py           # Core HTTP engine (form parser, session)
    ├── sqli.py             # SQL injection scanner
    ├── xss.py              # XSS scanner
    ├── headers.py          # Security header checker
    ├── subdomain.py        # Subdomain enumerator
    └── report.py           # Report generator
```

---

## ⚙️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/VulnScanner.git
cd VulnScanner

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Web UI (Flask)
```bash
python app.py
```
Open `http://localhost:5000` in your browser, enter a target URL, and click Scan.

### CLI
```bash
# Basic scan
python main.py http://target-url.com

# With subdomain enumeration
python main.py http://target-url.com --subdomains

# Output as JSON report
python main.py http://target-url.com --output json
```

---

## 🛡️ Disclaimer

> **This tool is intended strictly for educational and authorized security testing purposes.**  
> Only scan systems you own or have explicit permission to test.  
> The author is not responsible for any misuse of this tool.

---

## 🏫 Academic Context

- **Institute:** Vidyalankar Institute of Technology  
- **Course:** Computer Networks & Security Lab (CNS)  
- **Year:** TE Sem-VI — 2025–26  
- **Branch:** Computer Engineering (AI/ML & Data Analytics)

---

## 📦 Dependencies

```
flask
requests
beautifulsoup4
lxml
colorama
```

---

## 📄 License

MIT License — free to use for educational purposes.
