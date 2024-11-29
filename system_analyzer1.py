#!/usr/bin/python3

import sys
import os

LOG_FILE = "/var/log/secure"
REPORT_FILE = "sudo_report.txt"

# Function Definitions
def read_log_file(filename):
    """Function to read and return contents of log file"""
    try:
        log_file = open(filename, "r")
        contents = log_file.readlines()
        log_file.close()
        return contents
    except FileNotFoundError:
        print("Error: Cannot find log file:", filename)
        return None
    except PermissionError:
        print("Error: No permission to read file:", filename)
        return None
        
def print_report(logins, failed, commands_report):
    """Function to print the complete analysis report"""
    print("\n====== System Log Analysis Report ======")

    # Print successful logins
    print("\n=== 1. Successful SSH Logins ===")
    if len(logins) == 0:
        print("No successful logins found.")
    else:
        users = {}
        for login in logins:
            user = login[0]
            ip = login[1]
            if user not in users:
                users[user] = []
            if ip not in users[user]:
                users[user].append(ip)
                
        for user in users:
            print(f"\nUser: {user}")
            print("Login IPs:")
            for ip in users[user]:
                print(f"  - {ip}")

    # Print failed login attempts
    print("\n=== 2. Failed Login Attempts ===")
    if len(failed) == 0:
        print("No failed login attempts found.")
    else:
        ips = {}
        for attempt in failed:
            ip = attempt[1]
            if ip not in ips:
                ips[ip] = 0
            ips[ip] += 1
            
        print("\nAttempts by IP:")
        for ip in ips:
            print(f"IP: {ip} - {ips[ip]} attempts")

    # Print most frequently run sudo commands
    print("\n=== 3. Most Frequently Run Sudo Commands ===")
    if len(commands_report) == 0:
        print("No sudo commands found.")
    else:
        for command in commands_report:
            print(command)       
