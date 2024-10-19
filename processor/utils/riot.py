import requests
import json
import gzip
from io import BytesIO

S3_BUCKET_URL = "https://vcthackathon-data.s3.us-west-2.amazonaws.com"


def get_players(league):
    print(f"\nProcessing League {league} players")
    
    players = []
    
    remote_file = f"{S3_BUCKET_URL}/{league}/esports-data/players.json.gz"
    response = requests.get(remote_file, stream=True)
    
    if response.status_code == 200:
        gzip_bytes = BytesIO(response.content)
        with gzip.GzipFile(fileobj=gzip_bytes, mode="rb") as gzipped_file:
            players = json.load(gzipped_file)
    elif response.status_code == 404:
        # Ignore
        print(f"File not found {remote_file}")
    else:
        print(response)
        print(f"Failed to download {remote_file}")
        
    print(f"League {league} players processed")
    
    return players

def get_mapping_data(league):
    print(f"\nProcessing League {league} mapping_data")
    
    mapping_data = []
    
    remote_file = f"{S3_BUCKET_URL}/{league}/esports-data/mapping_data.json.gz"
    response = requests.get(remote_file, stream=True)
    
    if response.status_code == 200:
        gzip_bytes = BytesIO(response.content)
        with gzip.GzipFile(fileobj=gzip_bytes, mode="rb") as gzipped_file:
            mapping_data = json.load(gzipped_file)
    elif response.status_code == 404:
        # Ignore
        print(f"File not found {remote_file}")
    else:
        print(response)
        print(f"Failed to download {remote_file}")
        
    print(f"League {league} mapping_data processed")
    
    return mapping_data