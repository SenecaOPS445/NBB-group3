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