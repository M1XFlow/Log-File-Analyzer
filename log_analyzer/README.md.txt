# Log file analyszer

A python tool that scans system log files to detect failed login attempts and admin-level commands ('sudo'). 


# Features
- detects brute force login attempts by counting failed passwords.
- Flags IP address with more than 5 failed attempts.
- identifies all sudo (admin) command usage
- Easy to costumize and extend

# How to use
1. clone the repo or download the script.
2. Place your log file (e.g, 'auth.log') in the same folder.
3. Run the script:
  python analyzer.py

# Sample Log Format
Sep 18 14:01:23 server sshd[12345]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Sep 18 14:02:00 server sudo: user : TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=/bin/ls


# Output example
Suspicious IP: 192.168.1.10 with 6 failed attempts
Found 1 sudo events.




## Skills Demonstrated
- Python scripting and automation
- Regular expressions (regex) for pattern matching
- File I/O and log parsing
- Threat detection logic (e.g., brute-force login detection)
- Basic incident response analysis
- Working with dictionaries and data structures