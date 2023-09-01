# Event-Driven-data-processing

# Event Driven data processing with AWS Lambda, SNS and SQS

## Project Description
This project demonstrates how to set up an event-driven data processing system using AWS Lambda, SNS (Simple Notification Service), and SQS (Simple Queue Service). 
It is designed for scenarios where files arrive on an ad-hoc basis in an S3 bucket, and you want to perform transformations on them before loading them into a data target.

## Architecture Overview
Architecture Diagram

<img width="528" alt="image" src="https://github.com/salmah52/Event-Driven-data-processing-/assets/44398948/104b8579-7c6c-4515-9b6f-2c567d9b09e1">


The architecture consists of several components, including S3, EventBridge, SNS, SQS, and Lambda functions. EventBridge is used to detect new files in the S3 bucket and trigger an event that is sent to an SNS Topic. The SNS Topic is connected to an SQS Queue, which acts as a buffer for messages. Lambda functions process these messages, perform data transformations, and load the data into the target destination.

## Overview of the Architecture
The architecture consists of several components:

- Amazon S3: This is where your files arrive and are stored. S3 is a scalable object storage service offered by AWS.

- Amazon EventBridge Rule: You create an EventBridge Rule to detect when a new file is added to your S3 bucket. EventBridge is a serverless event bus that makes it easy to connect different AWS services.

- Amazon SNS Topic: When the EventBridge Rule detects a new file, it triggers an event that is sent to an Amazon SNS Topic. SNS (Simple Notification Service) is a messaging service that can distribute notifications to a variety of destinations.

- Amazon SQS Queue: The SNS Topic is connected to an Amazon SQS (Simple Queue Service) Queue. The SQS Queue acts as a buffer to store the events (messages) until they are processed by your Lambda functions.

- AWS Lambda Function: You write one or more Lambda functions that are triggered by the SQS Queue. These Lambda functions process the files or perform the necessary transformations and load the data into your desired data target, such as a database or another storage service.

  

## Workflow

1. Permissions and IAM RolesStep
2. Create an AWS Lambda Function
3.  Create an Amazon SNS Topic
4.  Create an Amazon SQS Queue
5.  Create an Amazon EventBridge Rule Configure Amazon EventBridge Rule Target
6.   Subscribe SNS Topic to SQS Queue
7.   Permissions and IAM Roles
8.   Test

## Next Steps:
Depending on your specific use case and requirements, you can consider further enhancements to the project, such as:

- Implementing error handling and retry mechanisms for better fault tolerance.
- Adding additional processing logic to meet specific business needs.
- Integrating with downstream systems to deliver processed data.
-Implementing more advanced event-driven architectures using AWS services like AWS Step Functions or Amazon EventBridge.

## Conclusion
This project provides a foundation for building robust event-driven data processing pipelines on AWS, demonstrating how AWS Lambda, SNS, and SQS can be utilized to efficiently process files arriving in an S3 bucket while ensuring scalability and flexibility.

*Happy data engineering!*

