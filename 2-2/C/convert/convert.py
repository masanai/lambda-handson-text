import json
import datetime
import boto3

s3 = boto3.resource('s3')
bucket = 'lambda-handson-＜自身の作成したバケット名＞-output'

def lambda_handler(event, context):

    filecontents = ''

    # ヘッダの加工
    header = event["header"] + ",AVAILABLE_DATE"
    print(header)
    filecontents = header + "\n"
    
    # データの加工
    for record in event["records"]:
        buf = record.split(",")
        data = buf[0] + "," + buf[1] + ","
        data = data + "1,"
        data = data + datetime.datetime.now().strftime('%Y%m%d')
        print(data)
        filecontents = filecontents + data + "\n"
        
    # ファイル名を設定してS3にアップロード
    key = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-output.csv'
    obj = s3.Object(bucket, key)
    obj.put( Body=filecontents )
