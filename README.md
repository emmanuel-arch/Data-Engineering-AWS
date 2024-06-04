# Data Engineering on AWS Masterclass

The main goal of this Masterclass is to utilizie data engineering skills to power an analytics workload on AWS Cloud plartform, 

We are going to be building a digital currency monitoring platform that we can monitor through a one pager dashboard in near realtime. 

### Learning Objectives

1. Designing a sample Real world data Platform on AWS
2. Designing an Architecture Diagram
3. Injesting Data from REST  using AWS Lambda
4. Staging Data using AWS Simple Strorage Service (S3)
5. Designing a simple Postgres engine data warehouse using AWS RDS
6. Job scheduling using AWS EventBridge
7. Visualizing Data using either open source tools or AWS QuickSight


### Workload Requirements

1. Injesting data in near real time - We will need light wwight compute resources for this to run simple python scripts, 
AWS Lambda Serveless Service will be an ideal solution to this
2. We need to stage this data somewhere for the next pipeline task to pick it up. AWS S3 Object storage will be ideal for this
3. Wee need to get the extracted data and Load it into a simple Data Warehouse. We will use lambda for this as well and connect it to a postgres SQL DB to mimic our data warehouse. 
4. We will need to visualize this data.....
5. We will need to connect all this stages and automate it using schedulers that we can trigger the start and the rest flows. We will use AWS EventBridge Service to achieve this.
6. 


# DATA INJESTION

### A. Working with AWS Lambda

We will be reading Exchanges Data from CoinCap API, we will use AWS Serverless compute service called **AWS Lambda** to help in achieving this

1. Navigate to your AWS Management Console and search for AWS Lambda service, make sure you in the ***Ireland Region (eu-west-1)***
2. Create a Lambda Function on AWS, use the following specifications
    - Use Arthur From Scratch Approach
    - Runtime: **Python 3.11**
    - Architecture: **x86_64**
    - Execution Role: ***Create a new role with basic Lambda permissions***

3. To use Python Libraries such as Pandas for data wrangling, we need to add a Layer to our Lambda Function for this;
    - Scroll down to the layers section and click on **Add a Layer**
    - Select **AWS Layer**
    - From the Drop down, select **AWSSDKPandas-Python311** then select the latest version

4. Paste the script ***extraction.py*** under lambda_code in this repository to extract data from the CoinCap API, the script is well documented
5. Make sure to create a new python file from the lambda file project folder called ***s3_file_operations.py***  to help us in writing data to an s3 bucket.
   You can find the script under the **utils** folder in this repository.
6. To Increase our Timeout Limit, Navigate to the ***Configuration*** section, Click on Edit, Set **15 minutes** maximum timeout and click on save.
7. We are Also going to need to grant Lambda permissions to access AWS S3 Service, we do this by attaching and ***AmazonS3FullAccess*** Policy to our execution Role.


### B. Creating an S3 Bucket
1. Head on to your AWS Management Console and search for AWS s3
2. Click on create a new Bucket, name your bucket with a unique name eg ***de-masterclass-XX*** XX - can be your name initials
3. Disable ACLs (Access Control Lists)
4. Turn off ***Block all Public Access check box - Not Recommended though***
5. Enable Versioning 
6. Encryption: ***Server-side encryption with Amazon S3 managed keys (SSE-S3)***
7. Bucket Key: ***Enabled***
8. Finally Click on Create Bucket

Access your S3 Bucket and inside of it create create a  folder called exchanges

Once Everything is Well Set Up, we can test our Lambda Function by Invoking it via the TEST Button,
You can view through the output logs if you have any Error. 
Finally we can navigate to our S3 Bucket to see if our dataset has been saved there. 








