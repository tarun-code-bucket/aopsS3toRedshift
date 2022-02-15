#!/bin/bash
pip3 install boto3
python ./scripts/getDataFromS3.py $Bucket_Name $File_Name