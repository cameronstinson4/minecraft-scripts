import boto3
import json


def create_response(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')

    instances = list(ec2.instances.filter(InstanceIds=[InstanceId]))

    if (len(instances) != 1):
        raise Exception(f'Instance: {InstanceId} not found')
    
    instance = instances[0]
    message = ''

    # AWS instance state codes reference:
    # 0 : pending
    # 16 : running
    # 32 : shutting-down
    # 48 : terminated
    # 64 : stopping
    # 80 : stopped

    print(instance.state)

    if (instance.state['Name'] == 'running'):
        # shut er down
        instance.stop()
        message = "Initiated stop server command"

    elif (instance.state['Name'] == 'stopped'):
        # start er up
        instance.start()
        message = "Initiated start server command"

    else:
        # pending, shutting down, terminated, or stopping
        message = "Server is busy starting, shutting down, terminating, or stopping. Please try again later"
    
    return create_response(None, message)