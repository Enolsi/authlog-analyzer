# AuthLog Analyzer

AuthLog Analyzer is a beginner-friendly Python cybersecurity project that analyzes Linux SSH authentication logs to identify suspicious login activity.

The tool reads authentication log entries, tracks failed and successful SSH login attempts, and detects patterns that may indicate brute-force attacks or potentially compromised accounts.

## Features

* Parses Linux SSH authentication logs
* Detects failed login attempts
* Detects successful logins
* Counts failed attempts by IP address
* Tracks usernames targeted by each IP
* Tracks users associated with successful logins
* Detects possible brute-force activity after multiple failed attempts
* Warns when an IP has failed login attempts and later logs in successfully

## Example Output

```text
=== AuthLog Analyzer ===
IP: 192.168.1.45
Failed attempts: 3
Users targeted: admin, root
[!] Possible brute-force activity detected

=== Successful logins ===
IP: 192.168.1.45
Successful logins: 1
Users: enolsi
[!] Warning: this IP had failed attempts before a successful login
```

## Requirements

* Python 3
* Linux or another environment capable of running Python

No external Python libraries are required.

## Usage

Clone the repository:

```bash
git clone <repository-url>
cd authlog-analyzer
```

Run the analyzer:

```bash
python3 analyzer.py
```

By default, the program analyzes the included `sample_auth.log` file.

## Detection Logic

The analyzer uses simple rules to identify suspicious behavior.

An IP address with three or more failed login attempts is flagged as possible brute-force activity.

The analyzer also generates a warning when an IP address appears in both failed and successful login attempts. This may indicate that repeated authentication attempts were eventually successful.

## Project Structure

```text
authlog-analyzer/
├── analyzer.py
├── sample_auth.log
├── README.md
└── .gitignore
```

## What I Learned

This project was created as part of my cybersecurity and Python learning journey. While building it, I practiced:

* Reading and parsing log files with Python
* Working with strings and `split()`
* Using dictionaries and sets
* Writing loops and conditional statements
* Extracting usernames and IP addresses from SSH logs
* Detecting simple security patterns
* Using Git and GitHub for version control

## Disclaimer

This project is intended for educational purposes. The current detection logic is intentionally simple and should not be considered a replacement for professional security monitoring or intrusion detection systems.
