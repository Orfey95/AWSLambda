import boto3

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket_list = []
    for bucket in s3.buckets.all():
        bucket_list.append(bucket.name)
    response = {
        'statusCode': 200
    }
    return {
        'message': response,
        'body': bucket_list
    }
