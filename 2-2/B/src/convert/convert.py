import json
import datetime

def lambda_handler(event, context):
    # ヘッダの加工
    header = event["header"] + ",AVAILABLE_DATE"
    print(header)
    
    #データの加工
    for record in event["records"]:
        buf = record.split(",")
        data = buf[0] + "," + buf[1] + ","
        data = data + "1,"
        data = data + datetime.datetime.now().strftime('%Y%m%d')
        print(data)
