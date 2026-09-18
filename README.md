---
description: >-
  Important information for the Cowrie honeypot deployment project by Maahir
  Shah.
---

# README

## SSH Honeypot Analysis

Real threat intelligence from deploying a 27-hour SSH honeypot. Logged 176 attacks from 16 unique IPs and analysed attacker behaviour and TTPs.

### Quick Start

#### Installation

```bash
pip install pandas
```

#### Running The Key Scripts

```bash
# Parse the raw honeypot logs
python Parser.py

# Display basic statistics
python Analyser.py

# Attacker profiling 
python Profiler.py
```

### Project Overview

This project demonstrates:

* Deploying a honeypot (Cowrie v2.9.13.dev3) on the cloud (DigitalOcean).
* Real attacker data collection (176 real SSH brute-force attempts).
* Data parsing, formatting and analysis using Python + Pandas.
* Attack patterns and information extraction (attacker profiles, TTPs, attack statistics).

### Files

| File                          | Purpose                             |
| ----------------------------- | ----------------------------------- |
| `Analysis_Report.md` | Full threat analysis repor          |
| `Detailed_Method.md`          | Method for implementing the project |
| `Parser.py`                   | Extract data from raw Cowrie logs   |
| `Analyser.py`                 | Basic statistics and aggregation    |
| `Profiler.py`                  | Attacker profiling   |
| `attacks.csv`                 | Parsed attack data                  |
| `honeypotlogs.txt`            | Raw Cowrie honeypot text logs            |

### Tools & Techniques

* Honeypot: Cowrie SSH Honeypot (v2.9.13.dev3).
* Infrastructure: DigitalOcean (Ubuntu 22.04 LTS) VM droplet.
* Data Analysis: Python, Pandas.
* Parsing: Regex pattern matching.

### Methodology

1. Deployment: 27-hour Cowrie honeypot on a DigitalOcean VM.
2. Data Logs: SSH login attempts logged and downloaded to my local machine for analysis.
3. Parsing: Python regex to extract attacker IP, username and password combinations used.
4. Analysis: Data grouping with Pandas to identify attack patterns.
5. Profiling: Grouping attackers by persistence and technique.

### How to Read This Project

1. Start with `Analysis_Report.md` to understand the purpose of the honeypot and methodology.
2. OPTIONAL: Read through the `Detailed_Method.md` file to implement the honeypot yourself with detailed instructions.&#x20;
3. Run `Parser.py` to parse the raw text log file honeypotlogs.txt.
4. Run `Analyser.py` to see basic statistics from the parsed attack logs.&#x20;
5. Run `Profile.py` to profile and group the attacks.
6. Review `attacks.csv` for raw, formatted log data.
7. Review `honeypotlogs.txt` for raw, unformatted, original log data.

***

### Author

Maahir Shah - Offensive Security Enthusiast and Ethical Hacker.



### License

MIT License - anyone can use this project for learning, research and using my code.
