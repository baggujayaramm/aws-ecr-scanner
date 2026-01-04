import boto3

def ec2_instances():
    ec2_client=boto3.client('ec2',region_name=
    'us-east-1',aws_access_key_id='',aws_secret_access_key='')
    response=ec2_client.describe_instances()
   # print(response)
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            tags = instance.get('Tags', [])
        for tag in tags:
            if tag['Key'] == 'Name':
                print(tag['Value'])

        
ec2_instances()