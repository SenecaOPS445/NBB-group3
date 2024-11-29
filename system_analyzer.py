#!/usr/bin/python3

import sys
import os

LOG_FILE = "/var/log/secure"
REPORT_FILE = "sudo_report.txt"

def get_most_frequent_sudo_commands(log_lines):
    """Function to find the most frequently run sudo commands"""
    command_frequency = {}
    if log_lines is None:
        return command_frequency
    
    for line in log_lines:
        if "COMMAND=" in line:
            command = line.split("COMMAND=")[1].strip()
            command_frequency[command] = command_frequency.get(command, 0) + 1
    
    commands_report = [
        f"{count} {command}\n" for command, count in sorted(command_frequency.items(), key=lambda x: x[1], reverse=True)
    ]
    
    return commands_report
