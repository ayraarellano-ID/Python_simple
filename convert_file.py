import argparse
import csv
import gzip
import logging
import os
import tempfile

import boto
import json_lines
import tqdm

import boto3
import botocore


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



def upload_to_s3(bucket, key, filename):
	logger.info(f'Uploading {filename} to {bucket}:{key}')
	s3 = boto3.resource('s3')
	bucket = s3.Bucket(bucket)
	bucket.upload_file(filename, key)


def upload_to_s3(bucket, key, filename):
    logger.info(f'Uploading {filename} to {bucket}:{key}')



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', type=str, default='l2h-data')
    parser.add_argument('--dest-bucket', type=str, default='l2h-data')
    parser.add_argument('--key', type=str, default='')
    args = parser.parse_args()

    bucket = args.bucket
    dest_bucket = args.dest_bucket
    key = args.key

    jlfile = os.path.basename(key)
    try:
        #download_from_s3(bucket, key, jlfile)

        dest_file = jlfile.replace('.jl.gz', '.csv')
        dest_key = key.replace('.jl.gz', '.csv')
        convert_from(jlfile, dest_file)
        upload_to_s3(dest_bucket, dest_key, dest_file)
    finally:
        logging.info('Cleaning up')
        os.unlink(jlfile)


if __name__ == '__main__':
    main()
