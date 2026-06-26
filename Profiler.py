# Gonna be called Profiler.py

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
