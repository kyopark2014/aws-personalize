import json,os
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

# This fucntion parses the result of personalize batch
def json_parsing(bucket, key):

    # Download the result file to /tmp/directory
    s3.download_file(bucket,key,"/tmp/"+key)
    f = open("/tmp/"+key)
    raw_datas = f.readlines()

    # Reads line by line and update temp-data.json.
    for line in raw_datas:
        f = open('/tmp/temp-data.json','w')
        f.write(line)
        f.close()
        with open('/tmp/temp-data.json', 'r') as f:
            # Reads temp-data.json. Execute put_usrId which is updated Dyanamo Table
            json_data = json.load(f)
            put_usrId(json_data)
        
        
    f.close()

# This fucntion updated Dyanamo Table
def put_usrId(putdata):
    # Get Recommended list. the list includes userId, recomended item lists and scores
    uid = putdata['input']['userId'] 
    itemList = putdata['output']['recommendedItems'] 
    itemScoreFloatList = putdata['output']['scores']

    itemScoreStrList = []
    # Change the type of score lists to string lists to use easily
    for itemScore in putdata['output']['scores']:
        itemScoreStrList.append(str(itemScore))

    # Update DynamoDB table
    response = dynamodb.put_item(
        TableName='personalize-batch',
        Item={
            'user-id': {
                'N': str(uid)
            },
            'item-list': {
                'SS': itemList
            },
            'score-list':{
                'SS': itemScoreStrList
            }
        }
    )



def lambda_handler(event, context):

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        json_parsing(bucket, key)
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

