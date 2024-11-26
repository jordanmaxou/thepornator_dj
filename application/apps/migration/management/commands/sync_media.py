import os
from urllib.parse import urlparse
import mimetypes

import paramiko
from stat import S_ISDIR
from minio import Minio
from minio.error import S3Error

from django.core.management.base import BaseCommand


def upload_to_minio(minio_client, minio_bucket_name, local_path, minio_path):
    try:
        minio_client.fput_object(
            minio_bucket_name,
            minio_path,
            local_path,
            content_type=mimetypes.guess_type(local_path, strict=False)[0],
        )
        print(f"File {local_path} uploaded to MinIO: {minio_path}")
    except S3Error as e:
        print(f"Upload to minio failed : {e}")


def is_folder(item) -> bool:
    return S_ISDIR(item.st_mode)


def copy_recursive(
    sftp, remote_path, minio_client, minio_bucket_name, local_temp_path="_tmp"
):
    os.makedirs(local_temp_path, exist_ok=True)

    for item in sftp.listdir_attr(remote_path):
        remote_item_path = os.path.join(remote_path, item.filename)
        local_item_path = os.path.join(local_temp_path, item.filename)

        if is_folder(item):
            os.makedirs(local_item_path, exist_ok=True)
            copy_recursive(
                sftp, remote_item_path, minio_client, minio_bucket_name, local_item_path
            )
        else:
            sftp.get(remote_item_path, local_item_path)
            minio_path = os.path.relpath(
                remote_item_path, "thepornator/assets"
            ).replace("\\", "/")
            print(f"minio_path = {minio_path}")
            upload_to_minio(
                minio_client, minio_bucket_name, local_item_path, minio_path
            )


class Command(BaseCommand):
    help = "Copy files from the pornator ftp server to local minio"

    def handle(self, *args, **options):
        FTP_HOST = os.environ.get("FTP_HOST")
        FTP_USER = os.environ.get("FTP_USER")
        FTP_PASSWORD = os.environ.get("FTP_PASSWORD")
        FTP_DIRECTORY = "thepornator/assets/img"

        MINIO_ENDPOINT = urlparse(os.environ.get("MINIO_ENDPOINT_URL"))
        MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
        MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
        MINIO_BUCKET_NAME = os.environ.get("MINIO_BUCKET_NAME")

        try:
            minio_client = Minio(
                f"{MINIO_ENDPOINT.hostname}:{MINIO_ENDPOINT.port}",
                access_key=MINIO_ACCESS_KEY,
                secret_key=MINIO_SECRET_KEY,
                secure=False,
            )

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(FTP_HOST, username=FTP_USER, password=FTP_PASSWORD)
            with ssh.open_sftp() as sftp:
                copy_recursive(sftp, FTP_DIRECTORY, minio_client, MINIO_BUCKET_NAME)
        finally:
            ssh.close()
