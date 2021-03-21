import boto3
import os

s3 = boto3.resource('s3')
AWS_DEFAULT_REGION = "eu-central-1"
os.environ["AWS_DEFAULT_REGION"] = AWS_DEFAULT_REGION


def lambda_handler(event, context):
    buckets_array = str(event['queryStringParameters']['name']).split(',')
    for bucket in buckets_array:
        s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={'LocationConstraint': AWS_DEFAULT_REGION}
        )
    response = {
        'statusCode': 200
    }
    return {
        'message': response,
        'body': buckets_array
    }
