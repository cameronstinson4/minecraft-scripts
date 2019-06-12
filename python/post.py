import boto3
import json
from utils import create_response

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')

    request_body = event

    if (request_body['secret'] != secret_password):
        return create_response('Incorrect secret. Please enter a valid secret to alter server settings', None)

    instance_id = request_body['instance_id']
    instances = list(ec2.instances.filter(InstanceIds=[instance_id]))

    if (len(instances) != 1):
        return create_response(f'Instance: {instance_id} not found', None)

    instance = instances[0]
    message = ''

    # AWS instance state codes reference:
    # 0 : pending
    # 16 : running
    # 32 : shutting-down
    # 48 : terminated
    # 64 : stopping
    # 80 : stopped

    if (instance.state['Name'] == 'running'):
        # shut er down
        instance.stop()
        message = f'Initiated stop server command on {instance_id}'

    elif (instance.state['Name'] == 'stopped'):
        # start er up
        instance.start()
        message = f'Initiated start server command on {instance_id}'

    else:
        # pending, shutting down, terminated, or stopping
        message = f'Server is busy starting, shutting down, terminating, or stopping. Please try again later'

    return create_response(None, message)
