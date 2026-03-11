# pyright: reportAttributeAccessIssue=false
import boto3

# # let's use Amazon S3
# s3 = boto3.resource('s3')

# # print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

# # Upload a enw file
# with open('c:C:\Users\user\OneDrive\Desktop', 'rb') as data:
#     s3.Bucket('mndeni-bucket-2026').put_object(Key='sources.png', Body=data)


#Creating Queues 

# Get the service resource
sqs = boto3.resource('sqs', region_name='eu-north-1')

# Create the queue. this returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='queue1')
# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='queue1')

#print out each queue name, which is part of its ARN
# for queue in sqs.queues.all():
#     print(queue.url)

# Create a new message
# response = queue.send_message(MessageBody='Hello from Python!')

# response = queue.send_message(MessageBody='Hello from Python!', MessageAttributes={
#     'Author': {
#         'StringValue': 'John Doe',
#         'DataType': 'String'
#     }
# })

# # You can now access identifiers and attributes
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

# Process message by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)
    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))

    # let the queue know that the message is processed    message.delete()
    message.delete()
