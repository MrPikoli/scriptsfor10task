import boto3

client = boto3.client('ec2')

response = client.terminate_instances(
	InstanceIds=[
        'i-0e8a0cd8fe146fd81',
    ],
)