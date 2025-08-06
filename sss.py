import boto3

ssm = boto3.client('ssm', region_name='us-east-1')
response = ssm.describe_instance_information()

managed_ids = [i['InstanceId'] for i in response['InstanceInformationList']]
print("Managed instances:", managed_ids)

if 'i-0e8a0cd8fe146fd81' in managed_ids:
    print(" Инстанс управляется через SSM")
else:
    print(" Инстанс НЕ управляется через SSM")