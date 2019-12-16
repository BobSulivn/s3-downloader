#%%
''' 
Filename: s3-downloader.py
Author: Bob Sullivan @BobSulivn
Purpose: Recursively download all files in a s3 bucket while preserving bucket
         structure on target machine.
Usage: python s3-downloader.py [s3-bucket-name]
'''
#  IMPORTS 
import os
import sys
import boto3

# bucket name we'd like to download from
BUCKET_NAME = sys.argv[1]

# setup s3 resource and bucket we'd like to download from
s3 = boto3.resource('s3')
download_bucket = s3.Bucket(BUCKET_NAME)

# create object iterator for downloads
objects = download_bucket.objects.all()

# loop through each object
for obj in objects:
    # get path and filename for each obj in the bucket
    path, filename = os.path.split(obj.key)
    # set filepath and filename on target system (client)
    download_name = f"./{path}/{filename}"
    try:
        # try to make directories for files within bucket
        os.makedirs(path)
    except FileExistsError:
        pass
    if filename != "":
        # download objects that are not folders in s3
        download_bucket.download_file(obj.key, download_name)

# %%
