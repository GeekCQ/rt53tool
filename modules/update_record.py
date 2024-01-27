"""
Updates an existing DNS record in a specific hosted zone in AWS Route 53.
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
        change_batch = {
            'Changes': [{
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': args.record_name,
                    'Type': args.record_type,
                    'TTL': args.ttl,
                    'ResourceRecords': [{'Value': args.record_value}]
                }
            }]
        }
        if args.dry_run:
            print("Dry run - Change to be made:")
            print(change_batch)
        else:
            client.change_resource_record_sets(HostedZoneId=args.zone_id, ChangeBatch=change_batch)
            print("Record updated successfully.")
    except Exception as e:
        print(f"Error updating record: {e}")
