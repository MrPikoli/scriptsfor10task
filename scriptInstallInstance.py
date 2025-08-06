
import boto3

client = boto3.client('ec2')

response = client.run_instances(

    ImageId='ami-020cba7c55df1f615',
    InstanceType='t2.micro',
    KeyName='kkeys',
    MaxCount = 1,
    MinCount = 1,
)

instance_id = response['Instances'][0]['InstanceId']
print(f"Создан инстанс с ID: {instance_id}")
