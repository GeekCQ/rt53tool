"""
Generates a report of DNS records in a specific hosted zone in AWS Route 53.
This module is part of the rt53tool project.

Author: tmlgcq
Date: 2024-01-27
Version: 1.0.0
"""

import boto3

def main(args):
    session = boto3.Session(profile_name=args.profile)
    client = session.client('route53')
    
    try:
        response = client.list_resource_record_sets(HostedZoneId=args.zone_id)
        print("Zone Report:")
        for record_set in response['ResourceRecordSets']:
            print_record(record_set)
    except Exception as e:
        print(f"Error generating report: {e}")

def print_record(record_set):
    print(f"Name: {record_set['Name']}")
    print(f"Type: {record_set['Type']}")
    print(f"TTL: {record_set['TTL']}")
    for record in record_set.get('ResourceRecords', []):
        print(f"Value: {record['Value']}")
    print()
