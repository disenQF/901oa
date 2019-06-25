import pymysql

conn = pymysql.Connect(
    host='121.199.63.71',
    user='root',
    password='root',
    port=3306,
    db='91_api_db',
    charset='utf8'
)

print('ok')