import json
import boto3

def lambda_handler(event, context):
    # Initialize SNS client
    sns_client = boto3.client('sns')

    for record in event['Records']:
        # Extract S3 bucket and object key from the event
        s3_bucket = record['s3']['bucket']['name']
        s3_object_key = record['s3']['object']['key']

        # Process the file (replace with your processing logic)
        try:
            # Your processing logic goes here
            # For example, you can read the file content or perform transformations
            # For simplicity, let's assume you're printing the object key
            processed_data = f"Processing file in bucket: {s3_bucket}, key: {s3_object_key}"
            print(processed_data)

            # Publish a message to an SNS topic (replace 'YourSNSTopicArn' with your SNS topic ARN)
            sns_client.publish(
                TopicArn='arn:aws:sns:us-east-1:693939771894:FileProcessingTopic',
                Message=processed_data
            )
        except Exception as e:
            # Handle any errors that may occur during processing
            print(f"Error processing file in bucket: {s3_bucket}, key: {s3_object_key}: {str(e)}")

# Your Lambda function will continue running and processing events as they occur.
