import boto3
from utils import create_response


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')

    instances = list(ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [
                     'running', 'stopped', 'pending', 'shutting-down', 'stopping']}]))

    if (len(instances) == 0):
        raise Exception(f'No instances found')

    result = {}

    for instance in instances:
        print(instance)
        result[instance.instance_id] = {
            "status": instance.state['Name'],
            "public_ip_address": instance.public_ip_address,
            "instance_type": instance.instance_type
        }

    return create_response(None, result)
