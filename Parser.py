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