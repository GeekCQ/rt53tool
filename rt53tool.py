#!/usr/bin/env python3
"""
Route 53 Management Tool (rt53tool)

Author: tmlgcq
Date: 2024-01-27
Version: 1.0.0

This script provides a command-line interface for managing AWS Route 53 records.
It enables various actions such as listing hosted zones, showing current records,
updating TTL, adding, updating, deleting records, and generating reports.

The script uses submodules for each specific action, making it modular and easy to maintain.
Each action is handled by a separate module, and this script coordinates the overall process.

Usage:
    python rt53tool.py --profile PROFILE_NAME --action ACTION --zone-id ZONE_ID [OTHER OPTIONS]

Replace PROFILE_NAME with your AWS CLI profile name, ACTION with the desired action,
and ZONE_ID with the hosted zone ID. Additional options depend on the chosen action.

"""

import argparse
import sys
from modules import list_zones, show_current, update_ttl, add_record, delete_record, update_record, generate_report

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Manage AWS Route 53 records")
    parser.add_argument("--profile", help="AWS CLI profile name", required=True)
    parser.add_argument("--action", help="Action to perform (list-zones, show-current, update-ttl, add-record, delete-record, update-record, generate-report)", required=True)
    parser.add_argument("--zone-id", help="Hosted zone ID")
    parser.add_argument("--ttl", type=int, help="TTL value in seconds")
    parser.add_argument("--record-name", help="Specific record name to work with")
    parser.add_argument("--record-type", help="Record type (A, CNAME, etc.)")
    parser.add_argument("--record-value", help="Record value (IP address, CNAME value, etc.)")
    parser.add_argument("--dry-run", action='store_true', help="Dry run to preview changes without applying them")

    args = parser.parse_args()

    # Execute the specified action
    if args.action == "list-zones":
        list_zones.main(args)
    elif args.action == "show-current":
        show_current.main(args)
    elif args.action == "update-ttl":
        update_ttl.main(args)
    elif args.action == "add-record":
        add_record.main(args)
    elif args.action == "delete-record":
        delete_record.main(args)
    elif args.action == "update-record":
        update_record.main(args)
    elif args.action == "generate-report":
        generate_report.main(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
