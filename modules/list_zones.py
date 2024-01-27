"""
Lists all hosted zones in AWS Route 53.
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
        response = client.list_hosted_zones()
        for zone in response['HostedZones']:
            print(f"ID: {zone['Id']}, Name: {zone['Name']}")
    except Exception as e:
        print(f"Error listing hosted zones: {e}")
