import boto3


ec2 = boto3.client('ec2')


instance = ec2.run_instances(
    ImageId='ami-09378ff823a36fcc5',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1
)

print("Создан экземпляр с ID:", instance['Instances'][0]['InstanceId'])
