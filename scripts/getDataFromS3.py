#This script gets the data from the S3 bucket 
# which is then utilised by the DBT to transform and ingest back to Redshift table.
import os
import boto3
import sys
import logging


def getS3Connection():
    # Get S3 connection
    s3Client = boto3.client('s3')
    return s3Client

def getS3Data(bucket_name, file_name):
    # Get S3 data
    logging.info("Call the getS3Connection function.")
    conn = getS3Connection()
    logging.info("Call the download_file function.")
    conn.download_file(bucket_name,file_name, file_name)

def main():
    logging.info("Get the parameters.")
    # with open("../parameters/config.yaml", "r") as cfg:
    #     creds = yaml.load(cfg, Loader=yaml.FullLoader)
    #     access_key = creds["dev"]["aws_access_key"]
    #     secret_key = creds["dev"]["aws_secret_key"]
    #     print(secret_key)
  
    bucket_name = sys.argv[1]
    file_name = sys.argv[2]
    logging.info("Call the getS3Data function.")
    getS3Data(bucket_name, file_name)

if __name__ == "__main__":
    main()
