import boto3
import os
import re
import sys

#AWS API
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
Region = os.environ.get("AWS_DEFAULT_REGION")

#Tag Function
def tag_reg(instanceid,tag_key,tag_value):
                       response = client.create_tags(
                       Resources=[instanceid,],
                       Tags=[
                              {
                                'Key': tag_key,
                                'Value': tag_value
                               },
                            ]
                       )

#Apply Tag for instance
User_Input = input('Are you going to apply Tag for AWS ' + Region + ' ?   Y/N: ')
if User_Input == 'Y' :
        p = client.describe_instance_status()['InstanceStatuses']
        Instance_Num = (len(p))
        for i in range(0,Instance_Num):
                instanceid=client.describe_instance_status()['InstanceStatuses'][i]['InstanceId']
                instance = ec2.Instance(instanceid)
                Req_Tag = ['DataClassification','Environment','ApplicationName','ResourceOwner','CiscoMailAlias','SecurityCompliance','DataTaxonomy']
                #Apply Tag for DataClassification
                print ('Applying Tag for ' + instanceid)
                tag_reg(instanceid,"DataClassification","Cisco Restricted")
                #Apply Tag for Environment
                if Region == 'us-east-2':
                          tag_reg(instanceid,"Environment","Prod")
                else:
                          tag_reg(instanceid,"Environment","NonProd")
                #Apply Tag for ApplicationName
                tag_reg(instanceid,"ApplicationName","devnet-platform-kubernetes")
                #Apply Tag for ResourceOwner
                tag_reg(instanceid,"ResourceOwner","Cisco DevNet Platforms")
                #Apply Tag for CiscoMailAlias
                tag_reg(instanceid,"CiscoMailAlias","fgiannet@cisco.com")
                #Apply Tag for SecurityCompliance
                tag_reg(instanceid,"SecurityCompliance","Yes")
                #Apply Tag for DataTaxonomy
                tag_reg(instanceid,"DataTaxonomy","Cisco Operations Data")
                print ('Applying Tag  for ' + instanceid + ' is completed')
