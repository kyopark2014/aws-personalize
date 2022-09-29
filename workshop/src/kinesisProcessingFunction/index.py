import os
import json
import boto3
import base64

personalize_events = boto3.client(service_name='personalize-events')
trackingId = os.environ['TRACKING_ID']

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            # Kinesis data is base64 encoded so decode here
            payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')

            # push_event_to_Personalize(json.loads(payload))
            body = json.loads(payload)
            response = personalize_events.put_events(
                trackingId = trackingId,
                userId = body['USER_ID'],
                sessionId = body['USER_ID'],
                eventList = [{
                    'eventType': body['EVENT_TYPE'].upper(),
                    'sentAt': str(int(body['TIMESTAMP'])/1000),
                    'itemId': body['ITEM_ID']
                }]
            )
            
        return 'Successfully processed {} records.'.format(len(event['Records']))
    except Exception as e:
        raise e
    
