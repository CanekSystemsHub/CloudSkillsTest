import boto3
import sys

try:
    def main():
        create_s3bucket(bucket_name)

except Exception as e:
    print(e)

def create_s3bucket(bucket_name):
    s3_bucket=boto3.client(
        's3',
    )

    bucket = s3_bucket.create_s3bucket(
        Bucket=bucket_name,
        ACL='Private',
    )

    print(bucket)

bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()
