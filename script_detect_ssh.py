import boto3
import time

ssm = boto3.client('ssm')
instance_id = 'i-0e8a0cd8fe146fd81'

response = ssm.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={
        'commands': ['cat /home/ubuntu/.ssh/authorized_keys']
    },
)

command_id = response['Command']['CommandId']
time.sleep(2)  # Подождать пару секунд перед получением ответа

output = ssm.get_command_invocation(
    CommandId=command_id,
    InstanceId=instance_id
)

print("Вывод authorized_keys:\n", output['StandardOutputContent'])
