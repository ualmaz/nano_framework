import re
import socket
from view import about_handler, contact_handler, products_handler

HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s' % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    request_string = str(request)
    print(request_string)

    about_handler(request_string, client_connection)
    contact_handler(request_string, client_connection)
    products_handler(request_string, client_connection)


# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='197791515',
#                              db='post_get_request',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         sql = """
#         INSERT INTO `post_get_request`.`new_table` (`last_name`, `first_name`) VALUES ({0},{1})
#         """.format(request_string)
#         for x in request_string:
#             cursor.execute(sql)
#     connection.commit()
# finally:
#     connection.close()
