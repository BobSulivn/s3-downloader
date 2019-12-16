#%%
''' IMPORTS '''
import os
import sys
import boto3
print (os.getcwd())
# bucket name we'd like to download from
BUCKET_NAME = sys.argv[1]

# setup s3 resource and bucket we'd like to download from
s3 = boto3.resource('s3')
download_bucket = s3.Bucket(BUCKET_NAME)

# create object iterator for downloads
objects = download_bucket.objects.all()

print(objects)
for obj in objects:
    path, filename = os.path.split(obj.key)
    print(f"path: {path}")
    print(f"filename: {filename}")
    download_name = f"./{path}/{filename}"
    print(download_name)
    try:
        # try to make directories for files within bucket
        os.makedirs(path)
    except FileExistsError:
        pass
    if filename != "":
        download_bucket.download_file(obj.key, download_name)

# %%
