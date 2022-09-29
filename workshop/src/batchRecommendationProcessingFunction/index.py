
import boto3,json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('personalize-batch')
movie_table = dynamodb.Table('Movie')

def lambda_handler(event, context):
    print(event)
    userId = event['pathParameters']['id']
    response = table.get_item(
        Key={
            'user-id' : int(userId)
        }
    )

    #print(response['Item']['item-list'])
    movie_list = response['Item']['item-list']
    score_set = response['Item']['score-list']
    score_list = list(score_set)

    batch_keys = {
        movie_table.name: {
            'Keys': [{'id': movie} for movie in movie_list],
            'ProjectionExpression': 'id, #name, category, imageUrl',
            'ExpressionAttributeNames': {'#name': 'name'}
        }
    }
    bat_response = dynamodb.batch_get_item(RequestItems=batch_keys)
    recommendations = bat_response['Responses']['Movie']


    for recommendation in recommendations:
        i=0;
        for movie in movie_list:
            if recommendation['id'] == movie:
                recommendation['score'] = score_list[i]
            i = i+1

    response = {
        'movies': recommendations
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response)
    }
