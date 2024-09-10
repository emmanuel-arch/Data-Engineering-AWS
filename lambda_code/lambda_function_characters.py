import requests
import json
import pandas as pd
import datetime
import s3_file_operations as s3_ops

def lambda_handler(event, context):
    # TODO implement
    print("Starting extraction")

    page = 1
    has_next = True  # changed from 'next' to 'has_next'

    # s3 bucket details
    bucket = "de-masterclass-zindua"
    all_data = []

    while has_next:
        print(f"Extracting page {page} Data.....")

        response = requests.get(f"https://rickandmortyapi.com/api/character?page={str(page)}")

        data = response.json().get('results', [])
        all_data.extend(data)

        # checking if the value of next url is null for the loop to stop
        if response.json().get('info', {}).get("next") is not None: 
            page += 1
        else:
            has_next = False  # changed to stop the loop

    character_df = pd.DataFrame(all_data)

    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print("All data fully extracted", character_df.shape)

    # Save Data to s3
    # Get the current timestamp
    timestamp = datetime.datetime.now()

    # Extract year, month, day, hour, and minute from the datetime object
    year = str(timestamp.year)
    month = str(timestamp.month).zfill(2)  
    date = str(timestamp.day).zfill(2)  
    hour = str(timestamp.hour).zfill(2) 
    minute = str(timestamp.minute).zfill(2)

    # Write exchanges_data to S3
    s3_ops.write_data_to_s3(character_df,
                            bucket_name=bucket,
                            key=f"Rick&Morty/character/{year}/{month}/{date}/{hour}/{minute}/character.csv")

    print("Data successfully saved to S3")
    
    # Return statement outside the loop
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Emmanuel Birgen!')
    }
