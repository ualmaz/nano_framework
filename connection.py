import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='197791515',
                             db='post_get_request',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

