import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region='eu-north-1'):
    """Create an S3 bucket in a specified region
    
    if a region is not specified , the bucket is created in the S3 default region(eu-north-1)
     :param bucket_name: Bucket to create
      :param region: string region to create bucket in, e.g., 'us-west-2'
      :return True if bucket created, else False
      """
    
    # Create bucket 
    try:
        bucket_config = {
            'CreateBucketConfiguration':{
                'LocationConstraint': region
            }
        }
        s3_client = boto3.client('s3', region_name=region)
        if region != 'eu-north-1':
            bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket= bucket_name, **bucket_config)
        return True
    except ClientError as e:
        logging.error(e)
        return False
    
# calling a function to create a bucket
created = create_bucket('original-images-mndeni')
created = create_bucket('processed-images-mndeni')
if created:
    print("Bucket created successfully.")
else:
    print("Failed to create bucket.")