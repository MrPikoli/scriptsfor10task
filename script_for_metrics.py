import boto3
import datetime

def get_cloudwatch_metrics(cloudwatch, instance_id, metric_name, start_time, end_time):
    response = cloudwatch.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/EC2',
                        'MetricName': metric_name,
                        'Dimensions': [
                            {
                                'Name': 'InstanceId',
                                'Value': instance_id
                            }
                        ]
                    },
                    'Period': 300,
                    'Stat': 'Average',
                },
                'ReturnData': True
            },
        ],
        StartTime=start_time,
        EndTime=end_time
    )
    return response['MetricDataResults'][0]['Values']


instance_id = 'i-0e8a0cd8fe146fd81'
client = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch',region_name='us-east-1')
response = client.describe_instances(
InstanceIds=[
        instance_id
    ],
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("private {}\npublic {}\ninstance type {}\nos {}\narch {}\nstate {}\nlaunch {}".
              format(instance['PrivateIpAddress'], instance['PublicIpAddress'],
                     instance['InstanceType'], instance['PlatformDetails'], instance['Architecture'],
                     instance['State']['Name'], instance['LaunchTime']))


        for device in instance['BlockDeviceMappings']:
            volume_id = device['Ebs']['VolumeId']
            volume_response = client.describe_volumes(VolumeIds=[volume_id])
            volume_size = volume_response['Volumes'][0]['Size']
            print(f"Размер диска {volume_size} GB")

#metric_name = 'CPUUtilization'
start_time = datetime.datetime(2025, 8, 6, 9, 57, 0)
end_time = datetime.datetime(2025, 8, 6, 10, 20, 0)

cpu_utilization_values = get_cloudwatch_metrics(cloudwatch, instance_id, 'CPUUtilization', start_time, end_time)
disk_read_bytes = get_cloudwatch_metrics(cloudwatch, instance_id, 'DiskReadBytes', start_time, end_time)
disk_write_bytes = get_cloudwatch_metrics(cloudwatch, instance_id, 'DiskWriteBytes', start_time, end_time)
network_in = get_cloudwatch_metrics(cloudwatch, instance_id, 'NetworkIn', start_time, end_time)
network_out = get_cloudwatch_metrics(cloudwatch, instance_id, 'NetworkOut', start_time, end_time)

print(f"{'CPUUtilization'} каждые 5 минут: {cpu_utilization_values}")
print(f"{'DiskReadBytes'} каждые 5 минут: {disk_read_bytes}")
print(f"{'DiskWriteBytes'} каждые 5 минут: {disk_write_bytes}")
print(f"{'NetworkIn'} каждые 5 минут: {network_in}")
print(f"{'NetworkOut'} каждые 5 минут: {network_out}")
