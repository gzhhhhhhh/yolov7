import pymysql.cursors
from datetime import datetime
# 连接数据库
connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='1991002470qq!GZH',
    db='admini',
    charset='utf8'
)
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print("中心点的坐标为：(" + str((c2[0] - c1[0]) / 2 + c1[0]) + "," + str((c2[1] - c1[1]) / 2 + c1[1]) + ")",label)
cursor = connect.cursor()
sql = "CREATE TABLE garbage (img_id varchar(1000),position varchar(1000),label varchar(1000),detect_time varchar(1000),id int primary key auto_increment)"
try:
    cursor.execute(sql)
    connect.commit()
except:
    print("表已存在")
# print('成功创建表格')

# 插入数据
sql = "INSERT INTO garbage (img_id,position,label,detect_time) VALUES('%s','%s','%s','%s')"
data = ("1","1","1","1")
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')