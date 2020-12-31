import json
import zipfile
import requests
import boto3
from datetime import date
import os


# import requests


def lambda_handler(event, context):
    
    key = 'c3d-C_VorrjDQY9ywxyY'
    today = date.today()
    today = str(today.year) + str(today.month) + str(today.day - 3)
    print(today)
    url = 'https://www.quandl.com/api/v3/databases/AS500/download?download_type={}&api_key={}'.format(today, key)
    
    temp_dir = '/tmp/'
    r = requests.get(url, allow_redirects=True)
    print(r.status_code)
    if r.status_code != 200:
        return {
        "statusCode": 400,
        "body": json.dumps({
            "message": "Could Not Find Data",
            }),
        } 
        
    
    open('/tmp/today_stock.zip', 'wb').write(r.content)
    
    print('1', os.listdir('/tmp'))
    
    
    with zipfile.ZipFile('/tmp/today_stock.zip', 'r') as zip_ref:
        zip_ref.extractall('/tmp/')
        
    print('2', os.listdir('/tmp'))
    
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket = 'big-data-class1', Key = 'batch-job/today_stock{}.csv'.format(today), Body = open('/tmp/' + today + '.csv', 'r').read())
                                                                                                     
                                                                                                     
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data Uploaded to S3 Successfully",
        }),
    }
