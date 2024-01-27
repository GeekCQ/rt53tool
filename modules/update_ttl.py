"""
Updates the TTL for DNS records in a specific hosted zone in AWS Route 53.
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
        record_sets = client.list_resource_record_sets(HostedZoneId=args.zone_id)
        changes = []
        for record_set in record_sets['ResourceRecordSets']:
            if args.record_name and not record_set['Name'].startswith(args.record_name):
                continue
            if record_set['Type'] in ['NS', 'SOA']:
                continue
            record_set['TTL'] = args.ttl
            changes.append({'Action': 'UPSERT', 'ResourceRecordSet': record_set})

        if changes:
            if args.dry_run:
                print("Dry run - Changes to be made:")
                for change in changes:
                    print(change)
            else:
                client.change_resource_record_sets(
                    HostedZoneId=args.zone_id,
                    ChangeBatch={'Changes': changes}
                )
                print("TTL updated successfully.")
        else:
            print("No records to update.")
    except Exception as e:
        print(f"Error updating TTL: {e}")
