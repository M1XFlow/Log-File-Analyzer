import re
from collections import defaultdict

def read_log_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines

def detect_failed_logins(log_lines):
    failed_attempts = defaultdict(int)
    pattern = r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)'

    for line in log_lines:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

    return failed_attempts

def detect_sudo_usage(log_lines):
    sudo_events = [line for line in log_lines if 'sudo' in line]
    return sudo_events

# Replace 'auth.log' with your actual log file path
log_lines = read_log_file('auth.log')

failed_logins = detect_failed_logins(log_lines)
for ip, count in failed_logins.items():
    if count > 5:
        print(f"Suspicious IP: {ip} with {count} failed attempts")

sudo_logs = detect_sudo_usage(log_lines)
print(f"Found {len(sudo_logs)} sudo events.")
