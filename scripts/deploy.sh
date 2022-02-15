#!/bin/bash
pip insatall boto3
python ./scripts/getDataFromS3.py $Bucket_Name $File_Name