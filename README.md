
# Route 53 Management Tool (rt53tool)

**rt53tool** is a versatile command-line tool designed for efficiently managing AWS Route 53 records. It allows users to interact directly with Route 53 services, providing functionalities such as listing hosted zones, showing current DNS records, updating TTL values, adding, updating, and deleting DNS records, and generating detailed reports of DNS configurations.

## Why This Tool? ##

Many of you might relate to the challenges of using the AWS CLI, especially during critical times like troubleshooting a production outage at three in the morning. Managing DNS and Route 53 is one of those tasks that, for me, fits into the category of "set it up securely and let Infrastructure as Code (IAC) do the rest." It's crucial but not something I interact with daily anymore.

This tool began its life as a Bash script. However, as it grew, the complexity of maintaining nested logic and handling external parsing requirements became rediculous. To circumvent these challenges and avoid managing an unwieldy 'timesaver' script, I shifted to Python and adopted a modular and extensible design. This approach allows for the easy evolution of the script's functionality, making it more manageable and adaptable to changing needs. My goal was to create a tool that offers a more user-friendly and efficient way to interact with AWS Route 53, especially during those critical moments when every second counts.

## Key Features:
- **List Hosted Zones**: Quickly retrieve all hosted zones within your AWS Route 53.
- **Show Current Records**: Display current DNS records within a specific hosted zone.
- **Update TTL**: Modify TTL values for specific DNS records, enhancing your DNS management capabilities.
- **Add/Update Records**: Easily add new DNS records or update existing ones.
- **Delete Records**: Safely remove unwanted DNS records from your hosted zones.
- **Generate Reports**: Get comprehensive reports of your DNS setups for analysis and auditing.
- **Dry Run Mode**: --dry-run is your friend at 3am.

## Designed for Flexibility:
- **Modular Architecture**: Each functionality is encapsulated in its own module, making the tool scalable and easy to extend.
- **Dry Run Option**: Preview changes without applying them, ensuring you're confident with the modifications before they go live.

## Contributing/Bugs/Etc.
If you have ideas for additional functionality or find a problem, please open an issue.  For bugs, feel free to submit a PR if you are able.

## Getting Started:
Check out the `README.md` for detailed usage instructions, requirements, and setup guide.

## Disclaimer

This project is a work in progress (WIP). Best efforts are made to test the tool, but users should be aware that damage can occur if used improperly. Users should have their AWS CLI setup for their environment and possess the appropriate permissions in AWS to perform the actions intended with this tool.

## Requirements

- Python 3
- Dependencies listed in `requirements.txt`

## Usage

Clone the repository:

```
https://github.com/tmlgcq/rt53tool.git
cd rt53tool
```

Install required libraries:

```
pip install -r requirements.txt
```

Run the tool:

```
python rt53tool.py --profile PROFILE_NAME --action ACTION --zone-id ZONE_ID [OTHER OPTIONS]
```

Replace `PROFILE_NAME` with your AWS CLI profile name, `ACTION` with the desired action, and `ZONE_ID` with the hosted zone ID. Additional options depend on the chosen action.

## License

This project is licensed under the Apache License 2.0
