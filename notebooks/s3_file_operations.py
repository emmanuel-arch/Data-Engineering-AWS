import pandas as pd
import boto3
import os
from io import StringIO
import io
from botocore.exceptions import ClientError


# s3 bucket details
bucket_name = os.getenv("BUCKET_NAME")


def write_data_to_s3(dataframe, bucket_name, key):
    # Convert the dataframe to a string
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False)

    # Creating an S3 client object
    s3 = boto3.client('s3')

    try:
        # Writing the data to S3
        s3.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=key)
        print(f"Data saved to S3 with bucket_name: {bucket_name} and key: {key}")
        return True
    except ClientError as e:
        print(e)
        return False