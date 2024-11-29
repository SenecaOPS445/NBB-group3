#!/usr/bin/python3

import sys
import os

LOG_FILE = "/var/log/secure"
REPORT_FILE = "sudo_report.txt"



def find_successful_logins(log_lines):
    """Function to find successful SSH logins"""
    logins = []
    
    if log_lines is None:
        return logins
        
    for line in log_lines:
        if "Accepted password for" in line:
            parts = line.split()
            user = parts[parts.index("for") + 1]
            ip = parts[parts.index("from") + 1]
            logins.append([user, ip])
    return logins

def find_failed_logins(log_lines):
    """Function to find failed login attempts"""
    failed = []
    
    if log_lines is None:
        return failed
        
    for line in log_lines:
        if "Failed password for" in line:
            parts = line.split()
            user = parts[parts.index("for") + 1]
            ip = parts[parts.index("from") + 1]
            failed.append([user, ip])
    return failed


def main():
    # Check if log file provided as argument
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = "/var/log/secure"

    # Read log file
    print(f"Analyzing log file: {log_file}")
    log_contents = read_log_file(log_file)
    
    # Analyze logs
    successful_logins = find_successful_logins(log_contents)
    failed_logins = find_failed_logins(log_contents)
    most_frequent_commands = get_most_frequent_sudo_commands(log_contents)
    
    # Print comprehensive report
    print_report(successful_logins, failed_logins, most_frequent_commands)

if _name_ == "_main_":
    main()
