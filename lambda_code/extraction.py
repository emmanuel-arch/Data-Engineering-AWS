import json
import logging
import requests 
import datetime
import pandas as pd
import s3_file_operations as s3_ops

url = 'https://api.coincap.io/v2/exchanges'
bucket = 'de-masterclass'

def lambda_handler(event, context):
    # TODO implement
    try:
        r = requests.get(url)
        
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
    
    # Convert the json response to a pandas DataFrame
    exchange_data =  pd.DataFrame(r.json().get('data', []))

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
    
    # Write exchanges_data to S3
    s3_ops.write_data_to_s3(exchange_data,
                            bucket_name=bucket,
                            key=f"exchanges/{year}/{month}/{date}/{hour}/{minute}/Exchanges.csv")
    
    
    print(f"Successfully Extracted:, {exchange_data.shape[0]} Exchange Records.....")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data Successfully Extracted and Saved to AWS S3!')
    }
