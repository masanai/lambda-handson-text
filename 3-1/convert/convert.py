import json
import datetime
import boto3
import pytz

s3 = boto3.resource('s3')
bucket = 'lambda-handson-<自身の氏名>-output'

def doconvert(header, records):
    
    filecontents = ''
    
    # ヘッダの加工
    header = header + ",AVAILABLE_DATE"
    print(header)
    filecontents = header + "\n"
    
    # データの加工
    for record in records:
        buf = record.split(",")
        data = buf[0] + "," + buf[1] + ","
        data = data + "1,"
        data = data + datetime.datetime.now().strftime('%Y%m%d')
        print(data)
        filecontents = filecontents + data + "\n"

    # ファイル名を設定してS3にアップロード
    jst = pytz.timezone('Asia/Tokyo')
    jst_now = datetime.datetime.now(tz=jst)
    key = jst_now.strftime('%Y%m%d%H%M%S') + '-output.csv'
    obj = s3.Object(bucket, key)
    obj.put( Body=filecontents )
