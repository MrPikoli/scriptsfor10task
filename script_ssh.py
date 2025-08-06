import boto3

client = boto3.client('ssm',region_name='us-east-1')
instance_id = 'i-0e8a0cd8fe146fd81'
ssh_user = 'ubuntu'
new_public_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoYeJXFvA4zQb6O8gjk9eBT0d6EAvfDenO9pyB08a5LjpZtgRoMcUbdvGrEVyf99wc63W0LY7orZPIXVhPPSCTV/q3dr+qDFyP5qHTWfGExf1JkD8irTaGIbnsAmQLq/ZxKOqRxXD6sSYFMVYkdQFZECnJbO0CFr4b1Tb+uP87lD3gZPnSplEYlkLjzkhy2Tp6tv2mZ0FIEGdYko04diJs0LkOZl6Pokz5mGi9FFsx7bgxFduwghPVywRfpVV1ST0x5ZtHWibluLRmSp1/srrNX62PpLGiSUh5DtKZFYorJRMFV1fav5oG+mzbN+mDuVbKlXVEX66BcO16fLa6Qwb/ k3'
command = f'echo "{new_public_key}" > /home/{ssh_user}/.ssh/authorized_keys'

response = client.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': [command]},
)
command_id = response['Command']['CommandId']


