import boto3

ec2 = boto3.client('ec2', region_name='us-east-1') # Replace with your desired region

instance_ids = []

response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            instance_ids.append(instance['InstanceId'])

if instance_ids:
    ec2.stop_instances(InstanceIds=instance_ids)
    waiter = ec2.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=instance_ids)
    print('All running instances have been stopped.')
else:
    print('No running instances found.')
