import csv
import requests
import os

# URL where DELETE requests will be sent
delete_url = "https://core.subsplash.com/media/v1/media-items/"

# Read Bearer token from environment variable
bearer_token = os.environ.get("BEARER_TOKEN")

# Read CSV and send DELETE requests with Bearer token authorization
def send_delete_requests():
    with open('bulkdelete.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header if present
        
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        
        for row in csv_reader:
            if row:  # Check if the row is not empty
                uuid = row[0]  # Assuming the ID is in the first column
                delete_response = requests.delete(delete_url + uuid, headers=headers)
                
                if delete_response.status_code == 204:
                    print(f"Deleted ID {uuid}")
                elif delete_response.status_code == 200:
                    print(f"Deleted ID {uuid}")
                else:
                    print(f"Failed to delete ID {uuid}. Status code: {delete_response.status_code}")

if __name__ == "__main__":
    send_delete_requests()
