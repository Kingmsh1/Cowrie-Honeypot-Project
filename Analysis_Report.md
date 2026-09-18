---
description: Official report for the Cowrie honeypot.
---

# Report

## Honeypot Analysis Report: SSH Attack Intelligence

### Summary:

A honeypot is a secure machine that appears to be vulnerable to attackers. It is designed to trick attackers into believing they compromised the seemingly-vulnerable machine and instead captures their information. In this context, information such as brute-force attempts and IP addresses was discovered.

Cowrie SSH honeypot was deployed for 27 hours and captured 176 attacks from 16 distinct IP addresses. Analysis revealed different attack profiles ranging from sophisticated, persistent scanners to mass, general scanners using common credentials.

***

### Findings:

#### Attack Distribution

* Total Attacks: 176.
* Unique Attacker IPs: 16.
* Most Persistent Attacker: 192.109.200.220 (63 attacks).
* Attack Concentration: Top 3 most persistent IPs account for 140 attacks.



#### Notable Attack Profiling

Profile A: Sophisticated Persistent Scanners

* IPs: 192.109.200.220 (63), 130.12.182.185 (47), 64.89.161.182 (30).
* Behaviour: Try a wide range of common and uncommon credential combinations.
* Tool(s): Likely an automatic brute-force tool, like Hydra.
* Attack Intensity: Medium-High (diverse wordlists, systematic & wide wordlist coverage).

Profile B: General Mass Scanners

* IPs: 130.12.180.51 (5), 47.253.5.130 (3), 217.154.69.208 (3), 47.81.57.6 (3).
* Behaviour: Repeated attempts with the same, shared credential combinations indicative of coordination/similar wordlists, low persistence signalled by limited attack count.
* Tool(s): Likely automated scripts or botnets.
* Attack Intensity: Low-Medium (low persistence, repeated unsuccessful attempts, low wordlist coverage).



#### Geographic Attack Distribution

Most Common Attacks Geographically (≥10):

| IP Address      | Location               | Attack Count |
| --------------- | ---------------------- | ------------ |
| 192.109.200.220 | Kerkrade, Netherlands  | 63           |
| 130.12.182.185  | Bavaria, Germany       | 47           |
| 64.89.161.182   | Luxembourg, Luxembourg | 30           |
| 45.148.10.121   | Amsterdam, Netherlands | 10           |

* Attacks originated predominantly from European countries, notably the Netherlands and Germany.
* A handful of attacks originated from Asian countries, like Thailand and Malaysia.&#x20;
* Other countries, such as America, were also the source of very few attacks against the honeypot.



#### Common Attack Vectors

Most frequently attempted credentials:

* admin/admin (tried by 8 different IPs).
* orangepi/orangepi (tried by 5 different IPs).
* root/P (tried by 5 different IPs).

This is indicative of attackers using common, simple wordlists possibly found online or in hacking tutorials. This also suggests a possible botnet using the same default wordlist being deployed by attackers, due to repeated failed attempts.

Thus, complex credential combinations are essential to avoid being prone to simple brute force techniques.&#x20;



#### Red Team Implications

Observations:

* Real attackers continue to attempt and automate simple credential combinations with the help of brute-forcing tools.&#x20;
* Automated tools were evidently used and thus pose a significant security threat.&#x20;
* Botnets pose a significant threat due to simultaneous attack.&#x20;
* Multiple independent attackers try identical credentials (tool convergence)

Actionable Insights:

* Strong credential combinations should be an enforced policy to limit the effectiveness of brute-force.
* Block or close any unnecessary ports/services that could be prone to exploitation.
* Attackers continue to rely on default/shared wordlists. Custom passwords that meet criteria, such as length and character complexity, would likely help defend against this.
* Stronger firewalls through enforcing a lockout policy and restricting SSH remote access to known IPs/blacklisting known botnet IPs.

***

### Methodology, Tools & Techniques:

* Deployment Period: 27 hours.
* Tool: Cowrie 2.9.13 SSH (Ports 2222-2223) Honeypot on DigitalOcean Ubuntu 22.04 LTS VM.&#x20;
* Detection Technique: Log analysis with Python regex + Pandas.
* Key Attacker Statistics: 176 attacks, 16 attacker IPs.

***

### MITRE ATT&CK TTP IDs:

* T1110.004 (Credential Stuffing) demonstrated through repeated SSH authentication attempts using credential stuffing - tried multiple username/password combinations
* T1110.001 (Password Guessing) demonstrated through trying to guess predictable credentials
* T1021.005 (SSH) demonstrated through attempting to target remote SSH services on the honeypot

***

### Conclusion:

This honeypot captured real attacker behaviour and insight into black-hat thinking. The log analysis revealed mostly basic credentials being attempted, likely due to shared wordlists and/or use of botnets. This suggests how some attackers prioritise speed of compromise over sophisticated attack, while others favour a more persistent and concentrated attack. These findings are valuable for understanding realistic attacker TTPs, improving penetration testing engagements.

