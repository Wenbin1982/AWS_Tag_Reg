import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')

for i in range(0,(len(client.list_buckets()['Buckets']))):
            Bucket_Name = client.list_buckets()['Buckets'][i]['Name']
            print('Apply Tag for Bucket ' + Bucket_Name)
            if Bucket_Name != 'dnacoperations-dev-serverlessdeploymentbucket-xesjv5dao614' and \
                    Bucket_Name != 'escosystem-prod-serverlessdeploymentbucket-1d4c94vwaynmk' and \
                    Bucket_Name != 'escosystem-staging-serverlessdeploymentbucket-rky6iifgkvy8' and \
                    Bucket_Name != 'raffle-dev-serverlessdeploymentbucket-1nqpog59y8v5i':
                bucket_tagging = s3.BucketTagging(Bucket_Name)
                bucket_tagging.put(Tagging = {'TagSet': [{'Key': 'DataClassification', 'Value': 'Cisco Public'},
                                         {'Key': 'Environment', 'Value': 'Prod'},
                                         {'Key': 'ApplicationName', 'Value': 'Cisco DevNet Platform'},
                                         {'Key': 'ResourceOwner', 'Value': 'Cisco DevNet'},
                                         {'Key': 'CiscoMailAlias', 'Value': 'devnet-cloud-engineering@cisco.com'},
                                         {'Key': 'SecurityCompliance', 'Value': 'Yes'},
                                         {'Key': 'DataTaxonomy', 'Value': 'Cisco Operations Data'},
                                         ]})
