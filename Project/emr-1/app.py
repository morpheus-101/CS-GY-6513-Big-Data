import json
import boto3


client = boto3.client('emr', region_name = 'us-east-1')

# pyspark script
S3_BUCKET = 'big-data-class1'
S3_KEY = 'pyspark-scripts/main.py'
S3_URI = 's3://{bucket}/{key}'.format(bucket=S3_BUCKET, key = S3_KEY)

# 



def lambda_handler(event, context):
    print('EVENT:', event)

    input_bucket = event['Records'][0]['s3']['bucket']['name'] # not being used
    input_file_key = event['Records'][0]['s3']['object']['key']

    response = client.run_job_flow(
        Name= 'spark_job_cluster',
        LogUri= 's3://big-data-class1/prefix/logs', # LOGS
        ReleaseLabel= 'emr-6.0.0',
        Instances={
            'MasterInstanceType': 'm5.xlarge',
            'SlaveInstanceType': 'm5.large',
            'InstanceCount': 1,
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
            # 'Ec2SubnetId': 'subnet-XXXXXXXXXXXXXX'
        },
        Applications = [ {'Name': 'Spark'} ],
        # Configurations = [ 
        #     { 'Classification': 'spark-hive-site',
        #       'Properties': { 
        #           'hive.metastore.client.factory.class': 'com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory'}
        #     }
        # ],
        BootstrapActions=[
            {
                'Name': 'Maximize Spark Default Config',
                'ScriptBootstrapAction': {
                    'Path': 's3://support.elasticmapreduce/spark/maximize-spark-default-config',
                }
            },
        ],
        VisibleToAllUsers=True,
        JobFlowRole = 'EMR_EC2_DefaultRole', 
        ServiceRole = 'EMR_DefaultRole',     
        Steps=[
            {
                'Name': 'flow-log-analysis',
                'ActionOnFailure': 'TERMINATE_CLUSTER',
                'HadoopJarStep': {
                        'Jar': 'command-runner.jar',
                        'Args': [ 'state-pusher-script' ]
                }
            },
            {
                'Name': 'setup - copy files',
                'ActionOnFailure': 'CANCEL_AND_WAIT',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['aws', 's3', 'cp', S3_URI, '/home/hadoop/']
                }
            },
            {
                'Name': 'Run Spark',
                'ActionOnFailure': 'CANCEL_AND_WAIT',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': ['spark-submit', '/home/hadoop/main.py',  input_file_key.split('/')[1]]
                }
            }
        ]
    )
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "EMR Job Successfully Started",

        }),
    }