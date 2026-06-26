---
description: >-
  Notes on how I set up a honeypot and analysed real hacking traffic from around
  the world.
---

# Cowrie Honeypot Blue Lab

## Setup:



* Used Cowrie as my honeypot software.
* Used DigitalOcean to set up a small droplet running Cowrie.
* Used Docker for creating and managing a container for Cowrie.
* Used Pandas for data & log analysis.&#x20;
* Assigned a public IP and was attacked for 27 hours, collecting logs.

***

## Tool Breakdown:



Cowrie:

* Cowrie is a SSH honeypot that's not a real machine but simulates a vulnerable Linux machine on the Internet, attracting hackers.
* It logs behaviour and attacks performed without hackers knowing.
* It doesn't let them actually access a real system and is used to collect real attack data to analyse attacker TTPs (Tactics, Techniques and Procedures) for analysis and understanding.



Honeypot Concept:

* Honeypots are important for attracting attacks without causing real damage, helping to study and identify attack patterns, techniques and an attacker's mindset.&#x20;
* This can help strengthen defences in real systems by utilising knowledge of how hackers operate in a real attack.&#x20;
* Honeypots are designed to appear vulnerable to attackers, but they won't allow access to a real system preventing any real risk.



Docker for Containerisation:

* Containerisation is packaging an application and dependencies (e.g., libraries, tools, configs etc.) into one unit. This can help it run anywhere, including in our DigitalOcean droplet. &#x20;
* Docker creates and manages containers.&#x20;
* It took Cowrie and created a package containing it along with its dependencies.
* This helps it run the same on any appropriate location.&#x20;
* Without Docker, I would've had to manually install the tools required for Cowrie like Python, libraries and other dependencies.&#x20;
* Quick deploying of Cowrie, saving time on installation and configuration.&#x20;



Pandas for Data & Log Analysis:

* Pandas is a Python library used for analysing data.
* Can apply filters, grouping, calculations and export data.&#x20;
* Used to load the honeypot logs, organise data from the attack, identify patterns and key statistics.&#x20;
* Similar to Excel except Pandas code lets us analyse a lot more logs with similar effort but Excel would require manual input of all the data.&#x20;

***

## Steps:



1. Got the honeypot logs in .txt format. Looks messy at this stage.
2. Writing a Python script to extract data into a CSV (Comma-Separated Values) file. This is a type of text file that is organised in rows (separated by new lines) and columns (separated by commas):&#x20;

```python
## Gonna be called Parser.py
print('ip,username,password')
import re

with open('honeypotlogs.txt', 'r') as f:
    lines = f.readlines()
    
attacks = []

for line in lines:
    if 'login attempt' in line:
        match = re.search(r"login attempt \[b'(.+?)'/b'(.+?)'\]", line)
        
        if match:
            username = match.group(1)
            password = match.group(2)
            
            ip_match = re.search(r'\[HoneyPotSSHTransport,\d+,(\d+\.\d+\.\d+\.\d+)\]', line)
            
            if ip_match:
                ip = ip_match.group(1)
            else:
                ip = 'unknown'
                
            print(ip + "," + username + "," + password)
            attacks.append({'ip': ip, 'username': username, 'password': password})

print("Total: " + str(len(attacks)) + " attacks")

```



Script Explanation:

* Line 2: "print('ip,username,password')":

Header of the CSV so that Pandas knows what the columns will be called when analysing.&#x20;

* Line 3: "import re":

Used to import the Python "regular expression" library. This will help us identify patterns in string text.&#x20;



* Line 5: "with open('honeypotlogs.txt', 'r') as f:":

Opens the log file in read mode and assigned to variable f for use later. "with" ensures the file closes when done.&#x20;



* Line 8: "attacks = \[]":

Creating an empty list called attacks to append to later.



* Line 12: "match = re.search(r"login attempt \\\[b'(.+?)'/b'(.+?)'\\]", line)":

Uses the search() method from the re library to look for the pattern specified for every line in the loop. "login attempt" is the string to look for. Escape "\[" to look for it in the .txt file. (.+?) means capture antyhing in this part of the .txt but "be lazy" and stop early to prevent capturing too much unwanted string (with the help of "?").&#x20;

The thing in the \[] is a regex with single quotes to denote it. This regex matches the string output in the honeypot logs text file.&#x20;



* Line 14: "if match:":

Checks to see if a match with the regex was actually found. If it wasn't found then it would be Boolean false and wouldn't continue with the if statement.



* Line 15: "username = match.group(1)":

Maps the first extracted group, denoted by the first (.+?) in the regex, to the username variable.&#x20;



* Line 17: "ip\_match = re.search(r'\\\[HoneyPotSSHTransport,\d+,(\d+\\.\d+\\.\d+\\.\d+)\\]', line)":

```
[HoneyPotSSHTransport,1,130.12.182.185] Connection lost
```

This is our real log line. We escape "\[" to be able to pick it up in the regex. "\d+," means match one or more digits until we reach the comma. Do the same for the rest of the line, capturing the IP. Here, we also do "\\." to escape the dot and capture it to extract the IP and a complete string. Each of these matches will be groups.&#x20;



* Lines 19-22:&#x20;

Group(1) will be the IP we extracted in Line 17, because it has the round brackets around it denoting the first and only group. This only happens if a match is found. If it isn't then the ip variable is assigned "unknown".



* Line 25: "attacks.append({'ip': ip, 'username': username, 'password': password})"

Creating a dictionary with key and value of IP, Username tried and Password tried and appending it to the Attacks list.



3. Ran the parser.py and got output. Pasted into a .csv file (called attacks.csv) for easier Pandas analysis. Wrote another Python script (Analyser.py) to analyse the data:

```python
import pandas as pd

data = pd.read_csv('attacks.csv')

print("First 10 attacks:")
print(data.head(10))

print("\nColumns:")
print(data.columns.tolist())

print("\nTotal attacks: " + str(len(data)))

print("\nUnique attacker IPs: " + str(data['ip'].nunique()))
print("\nTop attacking IPs:")
print(data['ip'].value_counts().head(10))
```



Script Explanation:

* Line 1: "import pandas as p":

Importing the Pandas library as "p" for shorthand.&#x20;



* Line 3: "data = p.read\_csv('attacks.csv')":

Loading the attacks.csv file as a table with the help of the CSV formatting created by Pandas and stores it as a table in the dataframe called "data".



* Line 9: "print(data.columns.tolist())":

data.columns is a Pandas object that shows column names. The .tolist() Pandas method being applied to it converts it to a list to make it easier to read.&#x20;



* Line 13: "print(f"Unique attacker IPs: {data\['ip'].nunique()}")":

.nunique() is a Pandas method that counts the number of unique values for the object it's called on - data\['ip']. In this case, it counts the number of unique IP addresses in the IP column of the table to find the number of unique attackers.&#x20;



* Line 15: "print(data\['ip'].value\_counts().head(10))":

Gets the 'ip' column of the dataframe that I called "data". it counts how many times each IP address appears and then returns only the top 10 results (i.e., the 10 most attacking IPs).&#x20;



4. Initial analysis of data complete. Moving onto clustering and profiling the attackers with this python script:

```python
## Gonna be called Profiler.py 

import pandas as pd

data = pd.read_csv('attacks.csv')

print("-" * 50)
print("ATTACKER PROFILING & CLUSTERING")
print("-" * 50)

print("\n\n1. CREDENTIAL PATTERNS BY ATTACKER IP:")
print("-" * 60)

for ip in data['ip'].value_counts().index:
    attacks_from_ip = data[data['ip'] == ip]
    creds = attacks_from_ip[['username', 'password']].values.tolist()
    if len(attacks_from_ip) == 1:
        print("\nIP: " + str(ip) + " (" + str(len(attacks_from_ip)) + " attack)")
    else:
        print("\nIP: " + str(ip) + " (" + str(len(attacks_from_ip)) + " attacks)")

    print("Credentials tried:")
    for username, password in creds:
        if pd.notna(username) and pd.notna(password):
            print(username + "/" + password)

print("\n\n2. MOST COMMONLY TRIED USERNAMES:")
print("-" * 60)

print(data['username'].value_counts().head(10))

print("\n\n3. MOST COMMONLY TRIED PASSWORDS:")
print("-" * 60)

print(data['password'].value_counts().head(10))

print("\n\n4. POTENTIALLY COORDINATED ATTACKS (same credentials from multiple IPs):")
print("-" * 60)

data['cred_pair'] = data['username'] + "/" + data['password']
coord = data.groupby('cred_pair')['ip'].nunique().sort_values(ascending=False)
for cred, num_ips in coord.head(10).items():
    if num_ips > 1:
        print(cred + " Tried from " + str(num_ips) + " different IPs")
```



Script Explanation:



* Line 15: "attacks\_from\_ip = data\[data\['ip'] == ip]":

For every one of the most attacking IPs, this goes through every line in the CSV and keeps the rows that match those IPs.



* Line 16: "creds = attacks\_from\_ip\[\['username', 'password']].values.tolist()":

Gets the two columns for username and password from the attacks\_from\_ip set of values from line 16. It finds the values and then converts them all to a list called creds which has the credential pairs tried out by the most attacking IPs.



* Line 40: "data\['cred\_pair'] = data\['username'] + "/" + data\['password']":

A new column for data is being created called 'cred\_pair' and the values in this column are in the format of \[username]/\[password] for all username and password pairs tested.



* Line 41: "coord = data.groupby('cred\_pair')\['ip'].nunique().sort\_values(ascending=False)":

Data is grouped based on the credentials used. The IPs that test the same credentials are put in the same group (by selecting only the 'ip' column). Then, the number of unique IPs are counted for each group with nunique(). The values are then sorted in descending order so the creds that were tested the most are at the top with a count of how many distinct IPs tried those creds.



* Lines 42-44:

num\_ips is the second part of the output from line 40 (i.e., the count of many distinct IPs tried those creds). cred is each item in coord.items() (i.e., each pair of credentials). If num\_ips > 1 then it prints how many times the specific credential pairs were tried (has to be bigger than 1 so that it's coordinated. Coordinated means they are using the same/similar tools or guides or methods of attack. If multiple IPs are trying the same credential pairs, it signals that common usernames/passwords should not be set and since they're tested often, they're popular amongst hackers for trying out.&#x20;

5. Finished up with writing a report on findings and summarising the attacks against the honeypot.
