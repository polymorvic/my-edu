import os
import boto3

ACCOUNT_ID = "770e83120e820600c5f9e43ea91bcce1"
ACCESS_KEY = "5bb4705e2882005e151b3beda0bb6f24"
SECRET_KEY = "0bc04dca9f65884b6f7a4697f6cfc9d52cd058f640da566615c0aaaf5244b926"
BUCKET_NAME = "driving-licence"
LOCAL_FOLDER = r"C:\Users\polymorvic\Downloads\multimedia_do_pytan"


s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="auto",
)

def upload_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            key = os.path.relpath(full_path, folder)

            s3.upload_file(full_path, BUCKET_NAME, key)
            print("Uploaded:", key)

upload_folder(LOCAL_FOLDER)