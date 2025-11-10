import json
import boto3 

def get_id_from_arn(arn):
    arn_split = arn.split(":")
    instance_id = arn_split[-1].split("/")[-1]
    return instance_id

def lambda_handler(event, context):
    
    instance_arn= event['resources'][0]
    print("Recieved instance ARN from cloudwatch: ",instance_arn)
    
    instance_id = get_id_from_arn(instance_arn)
    print("Parsed instance id from ARN: ",instance_id)

    ec2_client = boto3.client('ec2')
    
    volume_details = ec2_client.describe_volumes(
    VolumeIds=[
        instance_id
    ]
    )
    volume_type = volume_details['Volumes'][0]['VolumeType']
    print("Fetched volume type from instance: ",instance_id,"type: ",volume_type)

    if volume_type == "gp3":
        print("Volume type is gp3, no action required. Exiting gracefully !!!")
    else:
        print("Volume type is not gp3, converting to gp3")
        response = ec2_client.modify_volume(
        VolumeId=instance_id,
        VolumeType='gp3'
        )
        return response

   
