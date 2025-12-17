import json
import csv
import sys

def calculate_success_percentage(check_data):
    """Calculate success percentage for a check category."""
    total = check_data.get('Total', 0)
    if total == 0:
        return None
    success = check_data.get('Success', 0)
    return (success / total) * 100

def json_to_csv(json_data):
    """Convert JSON data to CSV format."""
    metadata = json_data.get('metadata', {})
    checks = json_data.get('checks', {})
    
    # Prepare the output row
    row = metadata
    
    # Add success percentages for each check category
    for check_name, check_data in checks.items():
        percentage = calculate_success_percentage(check_data)
        row[f'{check_name}'] = f'{percentage:.2f}' if percentage else ''
    
    return row

def main():
    """ Given JSON input of metadata and checks from PAC 2026, create a CSV row for this """
    # Read JSON from stdin
    try:
        json_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input - {e}", file=sys.stderr)
        sys.exit(1)
    
    # Convert to CSV row
    row = json_to_csv(json_data)
    
    # Write CSV to stdout
    writer = csv.DictWriter(sys.stdout, fieldnames=row.keys())
    writer.writeheader()
    writer.writerow(row)

if __name__ == '__main__':
    main()
