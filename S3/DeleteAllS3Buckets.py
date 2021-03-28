import boto3

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket_list = []
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
    response = {
        'statusCode': 200
    }
    return {
        'message': response
    }
