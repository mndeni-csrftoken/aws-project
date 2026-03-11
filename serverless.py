import boto3
import os
from PIL import Image 
from io import BytesIO
import uuid
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table('ImageMetadata') # type: ignore

PROCESSED_BUCKET = 'processed-images-<mndeni>'

def lambda_handler(event,context):
    # Get s3 event info
    record = event['Records'][0]
    source_bucket = record['s3']['bucket']['name']
    source_key = record['s3']['object']['key']

    # Download image from s3
    obj = s3.get_object(Bucket=source_bucket, Key=source_key)
    img_data = obj['Body'].read()

    # Open and resize image
    img =Image.open(BytesIO(img_data))
    img.thumbnail((200,200)) #200x200 thumbnail

    # save thumbnail to bytes in memory
    buffer =BytesIO()
    img.save(buffer, format='JPEG')
    buffer.seek(0)

    #Generate unique key for processed image
    processed_key = f'thumbnails/{os.path.basename(source_key)}'

    # upload thumbnail to processed bucket
    s3.put_object(
        Bucket=PROCESSED_BUCKET,
        KEY=processed_key,
        Body=buffer,
        ContentType='image/jpeg'
    )
    # save metadata to dynamodb
    image_id = str(uuid.uuid4())
    table.put_item(
        Item={
            'imageId': image_id,
            'originalBucket': source_bucket,
            'originalKey': source_key,
            'processedBucket': PROCESSED_BUCKET,
            'processedKey': processed_key,
            'timestamp': datetime.utcnow().isoformat()
        }
    )

    return {
        'statusCode': 200,
        'body': f'Processed image saved to {PROCESSED_BUCKET}/{processed_key} with metadata stored in DynamoDB'
    }