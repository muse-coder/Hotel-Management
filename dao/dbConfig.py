import pymysql

"""数据源配置信息"""
localSourceConfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'xmw1234567890',
    'db': 'dbdesign',
    'charset': 'utf8',
    'cursorclass' : pymysql.cursors.DictCursor
}



