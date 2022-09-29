import os
import json
import boto3
from operator import itemgetter

campaignArn = os.environ['CAMPAIGN_ARN']
personalizeRt = boto3.client('personalize-runtime')
dynamodb = boto3.resource('dynamodb')

movie_table = dynamodb.Table('Movie')

def get_personalize_recommendations(userId):
    response = personalizeRt.get_recommendations(
        campaignArn = campaignArn,
        userId = userId,
        numResults = 3
    )
    
    return response
    
def lambda_handler(event, context):
    userId = event['pathParameters']['id']
    response = get_personalize_recommendations(userId)
    movie_list = response['itemList']
    
    item_ids = []
    
    for movie in movie_list:
        item_ids.append(movie['itemId'])
        
    batch_keys = {
        movie_table.name: {
            'Keys': [{'id': movie['itemId']} for movie in movie_list],
            'ProjectionExpression': 'id, #name, category, imageUrl',
            'ExpressionAttributeNames': {'#name': 'name'}
        }
    }
    
    response = dynamodb.batch_get_item(RequestItems=batch_keys)
    recommendations = response['Responses']['Movie']
    
    for recommendation in recommendations:
        for movie in movie_list:
            if recommendation['id'] == movie['itemId']:
                recommendation['score'] = movie['score']
                
    recommendations = sorted(recommendations, key=itemgetter('score'), reverse=True)
    
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
