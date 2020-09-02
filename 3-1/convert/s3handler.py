import json
import boto3
import datetime
import os

import convert

s3 = boto3.resource('s3')
s3_cli = boto3.client('s3')

def lambda_handler(event, context):
    
    # S3 のファイルをtmpにダウンロード
    tmpfname = '/tmp/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-tmp.csv'
    inbucket = event['Records'][0]['s3']['bucket']['name']
    inkey = event['Records'][0]['s3']['object']['key']
    bucket = s3.Bucket(inbucket)
    bucket.download_file(inkey, tmpfname)

    # ファイルを読み込んで　convertの引数を生成
    header = ''
    records = []
    with open(tmpfname) as f:
        header = f.readline()
        header = header.replace("\n", "")
        record = f.readline() 
        while record:
            record = record.replace("\n", "")
            records.append(record)   
            record = f.readline()
    
    # 変換処理を呼び出した後、tmpファイルを削除
    convert.doconvert(header, records)
    os.remove(tmpfname)
