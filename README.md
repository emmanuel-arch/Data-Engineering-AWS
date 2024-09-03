Data Engineering on AWS Masterclass

The primary objective of this Masterclass is to enhance data engineering skills essential for powering an analytics workload on the AWS Cloud platform. For data scientists, understanding the backend processes that drive data-driven decisions is crucial. 
### Learning Objectives

1. Designing a real-world data platform on AWS with a focus on scalability and efficiency.
2. Creating a comprehensive architecture diagram to visualize the entire data pipeline.
3. Ingesting data from REST APIs using AWS Lambda, a serverless compute service ideal for lightweight data extraction.
4. Staging data efficiently with AWS Simple Storage Service (S3) to ensure seamless data flow.
5. Building a simple, yet robust, Postgres data warehouse using AWS RDS to store and query data.
6. Automating job scheduling with AWS EventBridge to manage data pipeline workflows.
7. Visualizing data using either open-source tools or AWS QuickSight, transforming raw data into actionable insights.

### Workload Requirements

1. **Near Real-Time Data Ingestion**: Lightweight compute resources are necessary to run Python scripts for data ingestion. AWS Lambda, with its serverless architecture, is perfectly suited for this task.
2. **Data Staging**: AWS S3 will be used as the staging area for storing ingested data before further processing.
3. **Data Warehousing**: Extracted data will be loaded into a Postgres SQL database using AWS Lambda, simulating a data warehouse environment.
4. **Data Visualization**: The staged and processed data will be visualized to derive insights, using tools such as AWS QuickSight or equivalent.
5. **Automation**: To ensure efficiency, all stages will be connected and automated using AWS EventBridge, allowing for scheduled execution of the data pipeline.

---

# Data Ingestion

### A. Working with AWS Lambda

In this section, we'll read exchange data from the CoinCap API, leveraging AWS Lambda for serverless computing—a crucial skill in the toolkit of any data scientist looking to build scalable data solutions.

1. **AWS Lambda Setup**:
    - Navigate to the AWS Management Console and select the AWS Lambda service. Ensure you are in the ***Ireland Region (eu-west-1)***.
    - Create a new Lambda function using the following specifications:
        - **Runtime**: Python 3.11
        - **Architecture**: x86_64
        - **Execution Role**: Create a new role with basic Lambda permissions.

2. **Adding Python Libraries**:
    - To use libraries like Pandas for data manipulation, add a layer to the Lambda function:
        - Scroll to the layers section, click on **Add a Layer**.
        - Choose **AWS Layer**, then select **AWSSDKPandas-Python311** and the latest version.

3. **Data Extraction Script**:
    - Paste the script from `extraction.py` under the `lambda_code` folder in this repository. This script handles data extraction from the CoinCap API.
    - Create a new Python file named `s3_file_operations.py` in the Lambda project folder. This script, found under the `utils` folder, assists in writing data to an S3 bucket.

4. **Lambda Configuration**:
    - Increase the timeout limit by navigating to the ***Configuration*** section, setting it to **15 minutes**, and saving the changes.
    - Grant Lambda permissions to access AWS S3 by attaching the ***AmazonS3FullAccess*** policy to the execution role.

### B. Creating an S3 Bucket

1. **AWS S3 Setup**:
    - In the AWS Management Console, search for S3 and create a new bucket with a unique name, e.g., ***de-masterclass-XX*** (where XX are your initials).
    - Adjust settings as follows:
        - Disable ACLs (Access Control Lists).
        - Turn off ***Block all Public Access*** (Not Recommended, but may be necessary).
        - Enable versioning.
        - Set encryption to ***Server-side encryption with Amazon S3 managed keys (SSE-S3)***.
        - Enable the Bucket Key.

2. **Folder Structure**:
    - Inside your S3 bucket, create a folder named `exchanges`.

3. **Testing the Setup**:
    - Invoke your Lambda function using the TEST button and review the output logs for any errors.
    - Verify that the dataset is successfully saved in your S3 bucket.

---

This project not only deepens your understanding of AWS services but also enhances your data engineering capabilities—skills that are invaluable in your data science career. By the end of this Masterclass, you’ll be equipped to design and implement efficient data pipelines that can process and analyze data in real-time, making you a more versatile and effective data scientist.

---

