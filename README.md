Overview
This project demonstrates a complete serverless image‑processing pipeline using AWS.
When a user uploads an image to an S3 bucket, a Lambda function automatically:
- Downloads the image
- Generates a 200×200 thumbnail
- Stores the processed image in a secondary S3 bucket
- Saves metadata in DynamoDB
This architecture is scalable, event‑driven, and requires no servers to manage.
