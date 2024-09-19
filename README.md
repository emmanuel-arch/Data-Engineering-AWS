

# Data Engineering Masterclass on AWS

This project is designed to enhance my data engineering skills by building and deploying a scalable data pipeline on AWS. It focuses on ingesting, staging, storing, and visualizing data efficiently. Understanding how these backend processes work is vital for data scientists, as it enables better insights from analytics workloads on the cloud.

## Learning Objectives

The following core objectives will guide this project:

1. **Data Pipeline Architecture**: Create a visual representation of the entire data pipeline using draw.io, providing a clear view of the flow of data from ingestion to visualization.
2. **Data Ingestion from APIs**: Utilize AWS Lambda for serverless data extraction from REST APIs, ideal for lightweight compute tasks.
3. **Efficient Data Staging**: Use AWS Simple Storage Service (S3) as an intermediary for staging ingested data.
4. **Data Storage in AWS RDS**: Establish a simple Postgres-based data warehouse using AWS RDS to enable efficient querying and storage of data.
5. **Data Visualization**: Use draw.io to visualize the data pipeline, showcasing how data is processed from source to insights.

---

## Overview of the Data Pipeline
![Data Pipeline Overview](./images/Data-Pipeline.png)
### Architecture Overview
The data pipeline consists of several AWS services working in tandem to extract, stage, store, and process data in near real-time:

1. **AWS Lambda** for executing Python scripts that ingest data from APIs.
2. **AWS S3** for staging raw data before further processing.
3. **AWS RDS (Postgres)** to act as the data warehouse for structured storage.
4. **Draw.io** to visualize the pipeline architecture.

---

## Data Ingestion Workflow

### Step 1: AWS Lambda for Serverless Data Extraction

This project uses AWS Lambda to read exchange data from the CoinCap API. AWS Lambda is an excellent serverless compute service ideal for this use case due to its scalability and cost-efficiency. Here's how the Lambda function is set up:

1. **Lambda Setup**:
    - Navigate to the AWS Management Console and select the Lambda service in the ***Ireland Region (eu-west-1)***.
    - Create a new Lambda function:
      - **Runtime**: Python 3.11
      - **Architecture**: x86_64
      - **Execution Role**: Create a new role with basic Lambda permissions.
    
2. **Adding Required Libraries**:
    - To use external libraries like `Pandas`, add a layer to your Lambda function:
      - In the function, scroll to **Layers** and click **Add a Layer**.
      - Choose **AWS Layers** and select **AWSSDKPandas-Python311**.

3. **Data Extraction Script**:
    - The `extraction.py` script handles the data extraction process, pulling data from the Rick and Morty API.
    - The `s3_file_operations.py` script, found under the `utils` folder, writes the extracted data to your S3 bucket.

4. **Lambda Configuration**:
    - Increase the function timeout to **15 minutes** under the ***Configuration*** section.
    - Attach the ***AmazonS3FullAccess*** policy to Lambda's execution role to enable access to S3.

### Step 2: Creating an S3 Bucket for Data Staging

Data from AWS Lambda will be staged in an S3 bucket before loading it into the data warehouse. Here's how to set it up:

1. **AWS S3 Setup**:
    - Create an S3 bucket with a unique name (e.g., `de-masterclass-birgen`) where `birgen` represents your initials.
    - Enable the following settings:
      - Disable ACLs (Access Control Lists).
      - Turn off ***Block all Public Access*** (use with caution).
      - Enable bucket versioning.
      - Set encryption to ***Server-Side Encryption (SSE-S3)*** with Amazon S3 managed keys.

2. **Folder Structure**:
    - Within your S3 bucket, create a folder named `exchanges` to store the ingested data.

3. **Testing the Setup**:
    - Invoke your Lambda function via the TEST button in the AWS Lambda console and check the output logs.
    - Verify that the dataset has been saved to your S3 bucket.

---

## Data Warehousing in AWS RDS (Postgres)

### Step 3: Setting Up a Postgres Database in AWS RDS

After the data is ingested and staged in S3, the next step is to store it in a Postgres database hosted on AWS RDS. This will act as a basic data warehouse where you can query and manipulate the data.

1. **RDS Setup**:
    - In the AWS Management Console, navigate to RDS and create a Postgres instance.
    - Choose a **t3.micro** instance for cost efficiency, and configure it to use a **Multi-AZ deployment** for availability.
    - Set up security groups to allow your Lambda function to communicate with the RDS instance.

2. **Loading Data into RDS**:
    - Create a Lambda function that extracts data from S3 and inserts it into your Postgres database.
    - Update the function’s environment variables to include the RDS connection string.

3. **Querying the Data**:
    - Once the data is loaded into RDS, you can run SQL queries using AWS DataGrip or pgAdmin to ensure the data has been correctly inserted.

---

## Data Pipeline Visualization Using Draw.io
![Entity Relationship Diagram](./images/Entity-Relationship-Diagram.png)
### Step 4: Visualizing the Data Pipeline Architecture

Now that the data has been ingested, staged, and stored, it's time to create a visual representation of the entire pipeline using draw.io. This final step ties everything together and helps you visualize the flow of data from extraction to warehousing.

1. **Architecture Diagram**:
    - Use [draw.io](https://app.diagrams.net/) to create an end-to-end architecture diagram.
    - The diagram should include the following elements:
      - **Rick and Morty API** (data source)
      - **AWS Lambda** (for serverless data ingestion)
      - **AWS S3** (for data staging)
      - **AWS RDS (Postgres)** (for data storage)
    - Add arrows to represent the data flow between components, ensuring a clear and intuitive visualization of the pipeline.

2. **Refining the Diagram**:
    - Use color codes and annotations to highlight key components.
    - Include a legend to clarify the role of each AWS service and data flow.
    - Export the diagram as an image or PDF for documentation purposes.

---

## Conclusion

This Data Engineering Masterclass on AWS has significantly enhanced my skills in building scalable, serverless data pipelines. I have gained hands-on experience with AWS Lambda, S3, and RDS, as well as the ability to visualize complex data architectures using draw.io. These skills are invaluable for building robust and efficient data-driven solutions, further enriching my data science career.

By completing this project, I am now equipped to design, implement, and maintain sophisticated data pipelines that can handle real-time data ingestion, processing, and visualization.

