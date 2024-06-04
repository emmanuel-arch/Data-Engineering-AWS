import json
import logging
import requests 
import datetime
import pandas as pd

url = 'https://api.coincap.io/v2/exchanges'

def lambda_handler(event, context):
    # TODO implement
    try:
        r = requests.get(url)
        
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")

    data =  pd.DataFrame(r.json().get('data', []))

    # Save Data to s3
    # Get the current timestamp
    # Convert the string to a datetime object
    timestamp = datetime.datetime.now()

    # Extract year, month, day, hour, and minute from the datetime object
    year = str(timestamp.year)
    month = str(timestamp.month).zfill(2)  
    date = str(timestamp.day).zfill(2)  
    hour = str(timestamp.hour).zfill(2) 
    minute = str(timestamp.minute).zfill(2)

    

    
    print(data.shape)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data Successfully Extracted!')
    }
