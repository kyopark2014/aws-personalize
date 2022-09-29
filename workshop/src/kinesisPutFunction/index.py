import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

kinesis = boto3.client("kinesis")

def put_record(name, data, partition_key):
    try:
        response = kinesis.put_record(
            StreamName=name,
            Data=json.dumps(data),
            PartitionKey=partition_key)
    except ClientError:
        logger.exception("Couldn't put record in stream %s.", name)
        raise
    else:
        return response

def lambda_handler(event, context):
    print(event)
    
    kinesis_stream = 'demogoprime-kinesis-stream-prd'
    partition_key = event["PartitionKey"]
    data = event["Data"]
    
    response = put_record(kinesis_stream, data, partition_key)
    
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            "Content-Type" : "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Allow" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Headers" : "*"
        },
        'body': json.dumps(response)
    }
    
